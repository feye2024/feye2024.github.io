#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

for ruby_bin in /opt/homebrew/opt/ruby@3.3/bin /usr/local/opt/ruby@3.3/bin; do
  if [[ -x "$ruby_bin/ruby" ]]; then
    export PATH="$ruby_bin:$PATH"
    break
  fi
done
export BUNDLE_PATH="${BUNDLE_PATH:-$HOME/.local/share/my-academic-site/gems}"
if ! bundle check >/dev/null 2>&1; then
  echo "Run bundle install with the Ruby and BUNDLE_PATH configured above."
  exit 1
fi

echo "AIRE Lab preview: http://127.0.0.1:4001 (Ctrl+C to stop)"
exec bundle exec jekyll serve --config _config.yml,_config.local.yml --host 127.0.0.1 --port 4001 --livereload --livereload-port 35730 "$@"
