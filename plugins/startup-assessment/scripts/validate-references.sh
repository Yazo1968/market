#!/usr/bin/env bash
# Cross-reference validation for startup-assessment plugin.
# Checks that all file references between commands, agents, and skills resolve.

PLUGIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0

report_error() {
  echo "  ERROR: $1"
  ERRORS=$((ERRORS + 1))
}

report_ok() {
  echo "  OK: $1"
}

echo "=== Validating startup-assessment cross-references ==="
echo

# 1. Commands → Agents: "Agent: **name**" and "**name-agent**" patterns
echo "--- Commands -> Agents ---"
for agent in $(grep -roh '\*\*[a-z0-9-]*\*\*' "$PLUGIN_DIR/commands/" 2>/dev/null \
  | tr -d '*' | sort -u \
  | while read -r name; do [ -f "$PLUGIN_DIR/agents/$name.md" ] || true; echo "$name"; done); do
  # Only check names that look like agent names (exist in agents/)
  true
done
# Simpler approach: extract all bold names and check against agents dir
AGENT_FILES=$(ls "$PLUGIN_DIR/agents/" 2>/dev/null | sed 's/\.md$//')
for agent in $AGENT_FILES; do
  # Check that each agent file is referenced by at least one command
  if grep -rq "\*\*$agent\*\*" "$PLUGIN_DIR/commands/" 2>/dev/null; then
    report_ok "agents/$agent.md is referenced by commands"
  else
    report_error "agents/$agent.md exists but is never referenced by any command"
  fi
done

# 2. Commands → Skill reference files
echo
echo "--- Commands -> Skill reference files ---"
for ref in $(grep -roh 'skills/[a-z0-9-]*/references/[a-z0-9-]*\.md' "$PLUGIN_DIR/commands/" 2>/dev/null | sort -u); do
  if [ -f "$PLUGIN_DIR/$ref" ]; then
    report_ok "$ref"
  else
    report_error "$ref not found (referenced by a command)"
  fi
done

# 3. Agents → Skills: check skill references (various formats)
echo
echo "--- Agents -> Skills ---"
# Pattern 1: "skills/skill-name/SKILL.md" or "skill-name/SKILL.md" in body text
# Pattern 2: "Load skills: skill1, skill2, skill3"
# Extract all skill directory names referenced in agent files
for skill in $(grep -roh '[a-z0-9-]*/SKILL\.md' "$PLUGIN_DIR/agents/" 2>/dev/null \
  | sed 's|/SKILL\.md||' | sort -u); do
  if [ -f "$PLUGIN_DIR/skills/$skill/SKILL.md" ]; then
    report_ok "skills/$skill/SKILL.md (referenced by agent)"
  else
    report_error "skills/$skill/SKILL.md not found (referenced by an agent)"
  fi
done

# 4. SKILL.md → Reference files (local and cross-skill)
echo
echo "--- SKILL.md -> Reference files ---"
for skillfile in $(find "$PLUGIN_DIR/skills" -name "SKILL.md" 2>/dev/null); do
  skilldir="$(dirname "$skillfile")"
  skillname="$(basename "$skilldir")"
  # Cross-skill references: skills/<other-skill>/references/<file>.md
  for ref in $(grep -oh 'skills/[a-z0-9-]*/references/[a-z0-9-]*\.md' "$skillfile" 2>/dev/null | sort -u); do
    if [ -f "$PLUGIN_DIR/$ref" ]; then
      report_ok "$skillname -> $ref (cross-skill)"
    else
      report_error "$ref not found (cross-skill ref in $skillname/SKILL.md)"
    fi
  done
  # Local references: references/<file>.md (exclude cross-skill paths)
  all_refs=$(grep -oh 'references/[a-z0-9-]*\.md' "$skillfile" 2>/dev/null | sort -u)
  cross_refs=$(grep -oh 'skills/[a-z0-9-]*/references/[a-z0-9-]*\.md' "$skillfile" 2>/dev/null \
    | sed 's|skills/[a-z0-9-]*/||' | sort -u)
  for ref in $all_refs; do
    # Skip if this ref was part of a cross-skill path
    echo "$cross_refs" | grep -qx "$ref" && continue
    if [ -f "$skilldir/$ref" ]; then
      report_ok "$skillname/$ref"
    else
      report_error "$skillname/$ref not found (referenced in $skillname/SKILL.md)"
    fi
  done
done

# 5. Orphan check: reference files not mentioned in their parent SKILL.md
echo
echo "--- Orphan reference files ---"
for reffile in $(find "$PLUGIN_DIR/skills" -path "*/references/*.md" 2>/dev/null); do
  refname="$(basename "$reffile")"
  skilldir="$(dirname "$(dirname "$reffile")")"
  skillname="$(basename "$skilldir")"
  skillmd="$skilldir/SKILL.md"
  if [ -f "$skillmd" ]; then
    if ! grep -q "$refname" "$skillmd"; then
      report_error "$skillname/references/$refname is not referenced in SKILL.md"
    fi
  else
    report_error "$skillname/references/$refname has no parent SKILL.md"
  fi
done

echo
if [ "$ERRORS" -eq 0 ]; then
  echo "All cross-references valid."
  exit 0
else
  echo "$ERRORS error(s) found."
  exit 1
fi
