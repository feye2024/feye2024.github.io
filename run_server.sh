#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# Use the preview runtime without changing the system Ruby or shell settings.
for ruby_bin in /opt/homebrew/opt/ruby@3.3/bin /usr/local/opt/ruby@3.3/bin; do
  if [[ -x "$ruby_bin/ruby" ]]; then
    export PATH="$ruby_bin:$PATH"
    break
  fi
done

# Keep installed dependencies outside the OneDrive-synced website folder.
export BUNDLE_PATH="${BUNDLE_PATH:-$HOME/.local/share/my-academic-site/gems}"

if ! bundle check >/dev/null 2>&1; then
  echo "Preview dependencies are missing. Run:"
  echo "  PATH=\"$PATH\" BUNDLE_PATH=\"$BUNDLE_PATH\" bundle install"
  exit 1
fi

echo "Local preview: http://127.0.0.1:4000 (Ctrl+C to stop)"
exec bundle exec jekyll serve --config _config.yml,docs/local-preview.yml --host 127.0.0.1 --livereload "$@"
