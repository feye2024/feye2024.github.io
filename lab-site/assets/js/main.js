(function () {
  "use strict";

  var links = Array.from(document.querySelectorAll(".site-nav a[href^='#']"));
  var sections = links.map(function (link) {
    return document.getElementById(link.hash.slice(1));
  }).filter(Boolean);
  var header = document.querySelector(".site-header");
  var anchorOffset = 0;
  var currentId = null;
  var framePending = false;

  function markCurrent(id) {
    if (id === currentId) return;
    currentId = id;
    links.forEach(function (link) {
      if (link.hash === "#" + id) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function updateCurrent() {
    var nextOffset = (header ? Math.ceil(header.getBoundingClientRect().height) : 0) + 20;
    if (nextOffset !== anchorOffset) {
      anchorOffset = nextOffset;
      document.documentElement.style.setProperty("--anchor-offset", anchorOffset + "px");
    }
    if (!sections.length) return;

    var scrollTop = window.scrollY;
    var scrollRange = document.documentElement.scrollHeight - window.innerHeight;

    // A short final section may never reach the header, even at the bottom.
    // Require real scrolling so a page that fits still starts at Home.
    if (sections.length && scrollRange > 4 && scrollTop > 4 && scrollRange - scrollTop <= 2) {
      markCurrent(sections[sections.length - 1].id);
      return;
    }

    var current = sections[0];
    sections.forEach(function (section) {
      if (section.getBoundingClientRect().top <= anchorOffset + 2) current = section;
    });
    markCurrent(current.id);
  }

  function scheduleUpdate() {
    if (framePending) return;
    framePending = true;
    window.requestAnimationFrame(function () {
      framePending = false;
      updateCurrent();
    });
  }

  updateCurrent();
  // Measure the header before native anchor scrolling, including just after a resize.
  links.forEach(function (link) {
    link.addEventListener("click", updateCurrent);
  });
  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", scheduleUpdate);
  window.addEventListener("load", scheduleUpdate);
  window.addEventListener("hashchange", scheduleUpdate);

  if (header && "ResizeObserver" in window) {
    new ResizeObserver(scheduleUpdate).observe(header);
  }
}());
