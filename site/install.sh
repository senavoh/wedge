#!/usr/bin/env sh
# Wedge installer: copies the skills into every agent skills folder it finds.
# Usage: curl -fsSL https://getwedge.dev/install.sh | sh
#    or: ./install.sh [target-dir ...]
set -eu

REPO="https://github.com/senavoh/wedge"
SRC=""
TMP=""

cleanup() { if [ -n "$TMP" ]; then rm -rf "$TMP"; fi; }
trap cleanup EXIT

if [ -d "$(dirname "$0")/skills/wedge" ]; then
  SRC="$(cd "$(dirname "$0")" && pwd)/skills"
else
  command -v git >/dev/null 2>&1 || { echo "wedge: git is required"; exit 1; }
  TMP="$(mktemp -d)"
  git clone --depth 1 --quiet "$REPO" "$TMP/wedge"
  SRC="$TMP/wedge/skills"
fi

if [ "$#" -gt 0 ]; then
  TARGETS="$*"
else
  # Personal skills folders for agents that read SKILL.md files.
  TARGETS=""
  for d in "$HOME/.claude" "$HOME/.codex" "$HOME/.gemini" "$HOME/.cursor" "$HOME/.config/opencode" "$HOME/.agents"; do
    [ -d "$d" ] && TARGETS="$TARGETS $d/skills"
  done
  [ -z "$TARGETS" ] && TARGETS="$HOME/.agents/skills"
fi

for t in $TARGETS; do
  mkdir -p "$t"
  for s in "$SRC"/*/; do
    name="$(basename "$s")"
    rm -rf "${t:?}/$name"
    cp -R "$s" "$t/$name"
  done
  echo "wedge: installed $(ls -d "$SRC"/*/ | wc -l | tr -d ' ') skills into $t"
done

echo "wedge: done. Ask your agent: \"Use wedge to find me a business I can start.\""
