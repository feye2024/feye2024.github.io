#!/usr/bin/env python3
"""Check the combined personal/Lab Pages artifact without network access."""

import argparse
import ipaddress
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


ORIGIN = "https://feye2024.github.io"
LAB_URL = ORIGIN + "/aire-lab/"
VOID_TAGS = set("area base br col embed hr img input link meta param source track wbr".split())


@dataclass
class Element:
    tag: str
    attrs: dict
    parents: tuple
    text: list = field(default_factory=list)

    @property
    def label(self):
        return " ".join("".join(self.text).split())

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()


class Page(HTMLParser):
    def __init__(self, path, url):
        super().__init__(convert_charrefs=True)
        self.path, self.url = path, url
        self.elements, self.stack = [], []
        self.feed(path.read_text(encoding="utf-8"))
        self.close()
        bases = [e for e in self.elements if e.tag == "base"]
        self.base_url = urljoin(url, next((e.attrs["href"] for e in bases if "href" in e.attrs), ""))
        self.base_target = next((e.attrs["target"] for e in bases if "target" in e.attrs), "_self")

    def handle_starttag(self, tag, attrs):
        element = Element(tag, {k: v or "" for k, v in attrs}, tuple(self.stack))
        self.elements.append(element)
        if tag not in VOID_TAGS:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        for element in self.stack:
            element.text.append(data)

    def target(self, link):
        return (link.attrs.get("target") or self.base_target).lower()


def references(element):
    """Yield (attribute, URL, must_exist) for browser-facing references."""
    attrs = element.attrs
    for attr in ("href", "src", "poster", "action"):
        if attr not in attrs:
            continue
        asset = (
            (attr == "src" and element.tag in {"script", "img", "source", "video", "audio"})
            or attr == "poster"
            or (element.tag == "link" and bool(set(attrs.get("rel", "").lower().split())
                                               & {"stylesheet", "icon", "apple-touch-icon", "manifest", "canonical"}))
        )
        yield attr, attrs[attr], asset
    if "srcset" in attrs and not attrs["srcset"].lstrip().startswith("data:"):
        for candidate in attrs["srcset"].split(","):
            if candidate.strip():
                yield "srcset", candidate.strip().split()[0], True
    if element.tag == "meta":
        if attrs.get("property", "").lower() == "og:url":
            yield "content", attrs.get("content", ""), True
        if attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r"(?:^|;)\s*url\s*=\s*(.+)", attrs.get("content", ""), re.I)
            if match:
                yield "refresh", match.group(1).strip("\"' "), True


def is_loopback(host):
    host = (host or "").lower().rstrip(".")
    if host == "localhost" or host.endswith(".localhost"):
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def check_build(build):
    build = build.resolve()
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    pages = {}
    for relative, url in (("index.html", ORIGIN + "/"),
                          ("aire-lab/index.html", LAB_URL),
                          ("lab/index.html", ORIGIN + "/lab/")):
        path = build / relative
        if not path.is_file():
            errors.append(f"Missing page: {relative}")
            continue
        try:
            pages[relative] = Page(path, url)
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {relative}: {exc}")

    for relative, page in pages.items():
        for element in page.elements:
            for attribute, value, must_exist in references(element):
                context = f"{relative}: <{element.tag}> {attribute}={value!r}"
                try:
                    resolved = urlsplit(urljoin(page.base_url, value))
                    require(not is_loopback(resolved.hostname), f"Local preview URL leaked: {context}")
                    if not must_exist or (resolved.scheme, resolved.netloc) != ("https", "feye2024.github.io"):
                        continue
                    target = (build / unquote(resolved.path).lstrip("/")).resolve()
                    if not target.is_relative_to(build):
                        errors.append(f"Reference escapes build directory: {context}")
                        continue
                    if target.is_dir():
                        target /= "index.html"
                    require(target.is_file(), f"Missing local resource: {context}")
                except ValueError as exc:
                    errors.append(f"Invalid URL: {context}: {exc}")

    home = pages.get("index.html")
    if home:
        links = [e for e in home.elements if e.tag == "a" and e.label == "AIRE Lab"
                 and any(p.tag == "nav" for p in e.parents)]
        require(bool(links), "index.html: AIRE Lab navigation link is missing")
        for link in links:
            require(urljoin(home.base_url, link.attrs.get("href", "")) == LAB_URL,
                    f"index.html: AIRE Lab navigation must point to {LAB_URL}")
            require(home.target(link) == "_blank", "index.html: AIRE Lab must open in a new tab")

    lab = pages.get("aire-lab/index.html")
    if lab:
        require(any(e.tag == "header" and e.has_class("site-header") and "AIRE Lab" in e.label
                    for e in lab.elements), "aire-lab/index.html: independent Lab header is missing")
        links = [e for e in lab.elements if e.tag == "a"
                 and any(p.tag == "nav" and p.has_class("site-nav") for p in e.parents)]
        expected = [(name.title(), "#" + name) for name in ("home", "people", "publications", "opening")]
        require([(e.label, e.attrs.get("href")) for e in links] == expected,
                "aire-lab/index.html: expected Home, People, Publications, Opening section links")
        ids = {e.attrs["id"] for e in lab.elements if "id" in e.attrs}
        for label, href in expected:
            require(href[1:] in ids, f"aire-lab/index.html: {label} target {href} is missing")
        for link in links:
            require(lab.target(link) == "_self", f"aire-lab/index.html: {link.label} must stay in the same tab")
            require(urljoin(lab.base_url, link.attrs.get("href", "")) == LAB_URL + link.attrs.get("href", ""),
                    f"aire-lab/index.html: {link.label} must target a section on the Lab page")

    bridge = pages.get("lab/index.html")
    if bridge:
        redirects = [value for e in bridge.elements for attr, value, _ in references(e) if attr == "refresh"]
        require(redirects == [LAB_URL], f"lab/index.html: legacy redirect must point to {LAB_URL}")

    leaks = []
    for path in build.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(build)
        parts = relative.parts[1:] if relative.parts[0] == "aire-lab" else relative.parts
        name = path.name.lower()
        readme = name.startswith("readme") and path.suffix.lower() in {"", ".md", ".markdown", ".txt", ".rst", ".html"}
        cv_source = path.suffix.lower() == ".tex" and ("cv" in path.stem.lower() or "curriculum" in path.stem.lower())
        if parts[0] in {"docs", "scripts", "lab-site"} or readme or cv_source or name in {
            "gemfile", "gemfile.lock", "run_server.sh", "_config.yml", "_config.yaml"
        }:
            leaks.append(str(relative))
    require(not leaks, "Source/maintainer files leaked into public output: " + ", ".join(leaks[:20])
            + (f" (and {len(leaks) - 20} more)" if len(leaks) > 20 else ""))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path, help="Combined Pages output directory")
    args = parser.parse_args()
    build = args.build_dir.resolve()
    if not build.is_dir():
        parser.error(f"Build directory does not exist: {build}")
    errors = check_build(build)
    if errors:
        print("Site build verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Site build verified: personal homepage, AIRE Lab, redirect, assets, and public output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
