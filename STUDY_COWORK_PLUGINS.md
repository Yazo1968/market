# Study: Claude Cowork Plugins — Complete Technical Reference

A comprehensive study of the Claude Cowork plugin system, its architecture, components, and how this repository (`yazo-market`) implements them.

---

## 1. What Are Cowork Plugins?

Plugins are **self-contained, file-based packages** that extend Claude Code and Cowork with custom functionality. They bundle together:

- **Slash Commands** — user-triggered workflow shortcuts (e.g., `/pre-assess`)
- **Agents (Subagents)** — specialized AI agents Claude can invoke for specific tasks
- **Skills** — knowledge modules Claude uses automatically based on task context
- **Hooks** — event handlers that respond to Claude Code lifecycle events
- **MCP Servers** — external tool integrations via Model Context Protocol
- **LSP Servers** — language server integrations for code intelligence
- **Settings** — default configuration applied when the plugin is enabled

Plugins work across both **Cowork** (Claude Desktop) and **Claude Code** (CLI), plus anything built on the Claude Agent SDK.

**Availability:** All paid plans (Pro, Max, Team, Enterprise).

---

## 2. Plugin Architecture

### 2.1 Directory Structure

```
my-plugin/
├── .claude-plugin/           # Metadata directory (ONLY plugin.json goes here)
│   └── plugin.json           # Plugin manifest (required: name field)
├── commands/                 # Slash commands as Markdown files (legacy location)
├── skills/                   # Agent Skills — folders with SKILL.md files
│   └── my-skill/
│       ├── SKILL.md          # Skill definition with frontmatter
│       ├── references/       # Optional supporting files
│       └── scripts/          # Optional utility scripts
├── agents/                   # Subagent definitions as Markdown files
├── hooks/                    # Event handler configurations
│   └── hooks.json            # Hook definitions
├── scripts/                  # Utility scripts used by hooks/agents
├── schemas/                  # JSON validation schemas
├── settings.json             # Default plugin settings
├── .mcp.json                 # MCP server configurations
├── .lsp.json                 # LSP server configurations
├── README.md                 # Documentation
└── CHANGELOG.md              # Version history
```

**Critical rule:** Commands, agents, skills, hooks go at the **plugin root** — NOT inside `.claude-plugin/`. Only `plugin.json` belongs in `.claude-plugin/`.

### 2.2 Plugin Manifest (`plugin.json`)

The manifest is optional but recommended. If omitted, Claude auto-discovers components in default locations and derives the name from the directory.

```json
{
  "name": "plugin-name",          // Required (kebab-case, no spaces) — also the namespace
  "version": "1.2.0",             // Semantic versioning
  "description": "Brief description",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://github.com/author"
  },
  "homepage": "https://docs.example.com",
  "repository": "https://github.com/author/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "commands": ["./custom/commands/"],    // Custom command paths (supplement defaults)
  "agents": "./custom/agents/",          // Custom agent paths
  "skills": "./custom/skills/",          // Custom skill paths
  "hooks": "./config/hooks.json",        // Hook config path or inline object
  "mcpServers": "./mcp-config.json",     // MCP config path or inline object
  "lspServers": "./.lsp.json",           // LSP config path or inline object
  "outputStyles": "./styles/"            // Output style files
}
```

**Key rules:**
- Custom paths **supplement** default directories — they don't replace them
- All paths must be **relative** and start with `./`
- The `name` field becomes the **namespace prefix** for all commands: `/plugin-name:command`

### 2.3 Environment Variable

`${CLAUDE_PLUGIN_ROOT}` — Absolute path to the plugin's installation directory. Use in hooks, MCP servers, and scripts for correct path resolution regardless of where the plugin is installed.

---

## 3. Plugin Components — Deep Dive

### 3.1 Slash Commands (commands/)

Commands are **user-triggered** shortcuts invoked with `/`. They are Markdown files with YAML frontmatter.

**Location:** `commands/` directory or `skills/` directory with `SKILL.md`

**Naming:** The filename (minus `.md`) becomes the command name, namespaced as `/plugin-name:command-name`.

**Frontmatter fields:**

| Field | Purpose | Example |
|-------|---------|---------|
| `description` | What the command does | `"Run pre-assessment on a startup"` |
| `allowed-tools` | Tools the command can use | `Read, Write, Bash(python3:*), Agent, AskUserQuestion` |
| `model` | Which model to use | `sonnet`, `inherit` |
| `argument-hint` | Hint for users about arguments | `"(path to business case doc)"` |
| `disable-model-invocation` | If true, only user-triggered (not auto-invoked) | `true` |

**Body:** The Markdown body is the full prompt/instructions Claude follows when the command is invoked. It can include:
- Step-by-step workflows
- Agent orchestration instructions
- Code blocks (Python, bash) to execute
- Confirmation points for user interaction
- Output specifications

**Example from this repo — `/pre-assess`:**
```markdown
---
description: Run pre-assessment on a startup business case document
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent, AskUserQuestion
model: sonnet
argument-hint: (no arguments required — reads from assessment/business-case-docs/)
---

## /pre-assess Command: Initial Readiness & Fit Assessment
...
```

**`$ARGUMENTS` placeholder:** Captures any text the user provides after the command name. E.g., `/greet Alex` — `$ARGUMENTS` resolves to `"Alex"`.

### 3.2 Agents (agents/)

Agents are **specialized subagents** that Claude can invoke for specific tasks. Each agent is a Markdown file with frontmatter defining its capabilities.

**Location:** `agents/` directory at plugin root

**Frontmatter fields:**

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Agent identifier | `context-extractor` |
| `description` | When Claude should invoke this agent | `"Extracts context from business docs"` |
| `model` | Model override | `inherit`, `sonnet`, `opus` |
| `color` | Display color in UI | `blue`, `green`, `red` |
| `tools` | Tools this agent can access | `[Read, Bash(python:*), Write]` |

**Body:** The Markdown body is the agent's **system prompt** — its full instructions, persona, extraction rules, output format, etc.

**Example from this repo — `context-extractor`:**
```markdown
---
name: context-extractor
description: >
  Extracts funding stage, vertical, commercial model, revenue architecture,
  geography, ask, regulatory exposure, and traction status from all business
  case documents.
model: inherit
color: blue
tools: [Read, Bash(python:*), Bash(find:*), Bash(ls:*)]
---

## System Prompt
You are the **Context Extractor** agent...
```

**How agents are invoked:**
1. **Automatically** — Claude selects the right agent based on task context
2. **By commands** — A command's instructions can explicitly orchestrate agents in sequence
3. **Manually** — Users can browse and invoke agents via `/agents`

### 3.3 Skills (skills/)

Skills are **model-invoked knowledge modules** — Claude automatically uses them based on the task context. They differ from commands: commands are user-triggered, skills are agent-triggered.

**Location:** `skills/<skill-name>/SKILL.md`

**Structure:**
```
skills/
└── domain-taxonomy/
    ├── SKILL.md          # Main skill definition
    └── references/       # Optional supporting reference files
```

**SKILL.md frontmatter:**

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Skill identifier | `domain-taxonomy` |
| `description` | When to trigger this skill (include trigger phrases) | `"Use when building frameworks or identifying domains"` |
| `version` | Skill version | `0.1.0` |

**Body:** Reference knowledge, frameworks, taxonomies, rubrics, or procedures that Claude can consult while working.

**Example from this repo — `domain-taxonomy`:**
```markdown
---
name: domain-taxonomy
description: >
  This skill should be used when any agent needs to understand the 10-domain
  analytical framework, identify which domains and modules apply, determine
  module criticality, or construct/validate a dynamic assessment framework.
---

# Domain and Module Taxonomy
| Domain | ID | Focus |
| Market and Opportunity | 1 | Market validity, size, dynamics |
...
```

**Key difference: Commands vs Skills:**

| Aspect | Commands (`commands/`) | Skills (`skills/`) |
|--------|----------------------|-------------------|
| Trigger | User types `/command` | Claude auto-selects based on context |
| Purpose | Run a workflow | Provide reference knowledge |
| Naming | `/plugin:command` | Internal reference |
| Contains | Step-by-step instructions | Domain knowledge, frameworks, rubrics |

### 3.4 Hooks (hooks/)

Hooks are **event handlers** that run automatically in response to Claude Code lifecycle events.

**Location:** `hooks/hooks.json` or inline in `plugin.json`

**Available events:**

| Event | When it fires |
|-------|---------------|
| `PreToolUse` | Before Claude uses any tool |
| `PostToolUse` | After successful tool use |
| `PostToolUseFailure` | After tool execution fails |
| `PermissionRequest` | When a permission dialog is shown |
| `UserPromptSubmit` | When user submits a prompt |
| `Notification` | When Claude sends notifications |
| `Stop` | When Claude attempts to stop |
| `SubagentStart` | When a subagent starts |
| `SubagentStop` | When a subagent stops |
| `SessionStart` | At session beginning |
| `SessionEnd` | At session end |
| `TeammateIdle` | When an agent team teammate goes idle |
| `TaskCompleted` | When a task is marked completed |
| `PreCompact` | Before conversation compaction |

**Hook types:**
1. **`command`** — Execute a shell command or script
2. **`prompt`** — Evaluate a prompt with an LLM
3. **`agent`** — Run an agentic verifier with tools

**Example:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

### 3.5 MCP Servers (.mcp.json)

Connect Claude to external tools and services via the Model Context Protocol.

```json
{
  "mcpServers": {
    "database-connector": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    }
  }
}
```

### 3.6 LSP Servers (.lsp.json)

Provide real-time code intelligence (diagnostics, go-to-definition, references).

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

### 3.7 Settings (settings.json)

Apply default configuration when the plugin is enabled. Currently only the `agent` key is supported — it activates a plugin's agent as the main thread.

```json
{
  "agent": "security-reviewer"
}
```

---

## 4. Plugin Marketplace System

### 4.1 Marketplace Structure

A marketplace is a **catalog** that distributes plugins. It lives in a Git repository with this structure:

```
my-marketplace/
├── .claude-plugin/
│   └── marketplace.json    # Marketplace catalog
└── plugins/
    ├── plugin-a/           # Plugin directories
    │   ├── .claude-plugin/
    │   │   └── plugin.json
    │   ├── commands/
    │   ├── agents/
    │   └── skills/
    └── plugin-b/
        └── ...
```

### 4.2 Marketplace Schema (`marketplace.json`)

```json
{
  "name": "marketplace-name",       // Required — kebab-case identifier
  "owner": {                        // Required
    "name": "Maintainer Name",
    "email": "email@example.com"    // Optional
  },
  "metadata": {                     // Optional
    "description": "Brief description",
    "version": "1.0.0",
    "pluginRoot": "./plugins"       // Base directory for relative source paths
  },
  "plugins": [                      // Required — array of plugin entries
    {
      "name": "plugin-name",        // Required — kebab-case
      "source": "./plugins/plugin", // Required — where to fetch the plugin
      "description": "...",
      "version": "1.0.0",
      "author": { "name": "..." },
      "keywords": ["tag1", "tag2"],
      "category": "productivity",
      "strict": true                // Default: true (plugin.json is authority)
    }
  ]
}
```

### 4.3 Plugin Sources

| Source | Format | Example |
|--------|--------|---------|
| Relative path | String starting with `./` | `"./plugins/my-plugin"` |
| GitHub | Object with `source: "github"` | `{ "source": "github", "repo": "owner/repo", "ref": "v2.0" }` |
| Git URL | Object with `source: "url"` | `{ "source": "url", "url": "https://gitlab.com/team/plugin.git" }` |
| Git subdirectory | Object with `source: "git-subdir"` | `{ "source": "git-subdir", "url": "...", "path": "tools/plugin" }` |
| npm | Object with `source: "npm"` | `{ "source": "npm", "package": "@acme/plugin", "version": "^2.0.0" }` |
| pip | Object with `source: "pip"` | `{ "source": "pip", "package": "my-plugin" }` |

### 4.4 Strict Mode

| `strict` value | Behavior |
|----------------|----------|
| `true` (default) | `plugin.json` is the authority. Marketplace entry can supplement with additional components. |
| `false` | Marketplace entry is the entire definition. Plugin must NOT have its own component definitions. |

### 4.5 Installation Scopes

| Scope | Settings file | Use case |
|-------|--------------|----------|
| `user` | `~/.claude/settings.json` | Personal plugins across all projects (default) |
| `project` | `.claude/settings.json` | Team plugins shared via version control |
| `local` | `.claude/settings.local.json` | Project-specific, gitignored |
| `managed` | Managed settings | Organization-enforced (read-only) |

---

## 5. CLI Commands

```bash
# Install a plugin
claude plugin install <plugin>[@marketplace] [--scope user|project|local]

# Uninstall
claude plugin uninstall <plugin>[@marketplace] [--scope ...]

# Enable/disable without uninstalling
claude plugin enable <plugin> [--scope ...]
claude plugin disable <plugin> [--scope ...]

# Update to latest version
claude plugin update <plugin> [--scope ...]

# Validate plugin/marketplace structure
claude plugin validate .

# Test locally during development
claude --plugin-dir ./my-plugin

# Load multiple plugins
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two

# Reload plugins without restart
/reload-plugins
```

**Marketplace management (inside Claude/Cowork):**
```
/plugin marketplace add owner/repo
/plugin marketplace add ./local-marketplace
/plugin marketplace add https://gitlab.com/team/plugins.git
/plugin marketplace update
/plugin install plugin-name@marketplace-name
```

---

## 6. How This Repository Implements The Plugin System

### 6.1 Repository: `yazo-market`

This repository is a **plugin marketplace** containing one plugin: `startup-assessment`.

**Marketplace config** (`.claude-plugin/marketplace.json`):
```json
{
  "name": "yazo-market",
  "owner": { "name": "Yasser", "email": "job.international.company@gmail.com" },
  "plugins": [{
    "name": "startup-assessment",
    "source": "./plugins/startup-assessment",
    "version": "1.2.0"
  }]
}
```

### 6.2 The `startup-assessment` Plugin

An AI-powered startup investment due-diligence tool implementing a 4-phase workflow:

```
/initiate  →  /pre-assess  →  /assess  →  /sensitivity  →  /recommend
```

**Component inventory:**

| Component Type | Count | Purpose |
|---------------|-------|---------|
| Commands | 5 | `/initiate`, `/pre-assess`, `/assess`, `/sensitivity`, `/recommend` |
| Agents | 15 | Specialized roles (context-extractor, scorer, gap-analyst, etc.) |
| Skills | 9 | Knowledge modules (domain-taxonomy, scoring-rubric, etc.) |
| Schemas | 14 | JSON validation for all data structures |
| Python Scripts | 5 | Score calculation, gap classification, go/no-go determination |

### 6.3 Workflow Architecture

The plugin demonstrates **agent orchestration** — commands coordinate multiple agents in sequence:

```
/pre-assess workflow:
  Step 0: Pre-flight checks (discover workspace, read documents)
  Step 1: context-extractor agent → context-profile.json
  Step 1b: AskUserQuestion for assessor profile → criteria-resolver agent
  ── CP1: User confirms context & assessor profile ──
  Step 2: framework-builder agent → framework.json
  ── CP2: User confirms assessment framework ──
  Step 3: research-agent → research-log.json
  Step 4: module-mapper agent → module-content-map.json
  Step 5: scorer agent → readiness-register.json + fit-to-purpose-register.json
  Step 6: gap-analyst agent → gap-register.json + dependency-map.json
  Step 7: go_nogo_determinator.py → preliminary-go-nogo-determination.json
  ── CP3: User reviews scored findings ──
  Step 8: qaqc-agent → qaqc-report.json
  Step 9: pre-assess-output-agent → HTML, PDF, MD reports
```

### 6.4 Design Patterns Used

1. **Confirmation Points (CP1-CP5):** Human-in-the-loop checkpoints where the user reviews and can correct outputs before proceeding. Uses `AskUserQuestion` tool with single-select options.

2. **Agent-per-task:** Each processing step has a dedicated agent with constrained tools and focused system prompt (e.g., context-extractor only reads and extracts; scorer only scores).

3. **Skills as shared knowledge:** Skills like `domain-taxonomy` and `scoring-rubric` provide reference data that multiple agents can consult — avoiding duplication of framework knowledge.

4. **Schema-driven validation:** 14 JSON schemas define the data contracts between agents, ensuring consistent data flow through the pipeline.

5. **Cowork workspace integration:** Commands discover the Cowork filesystem mount (`/sessions/*/mnt/*/`) dynamically, enabling file I/O within the user's workspace.

6. **Progressive output:** Each phase writes structured data (`.json`) and human-readable reports (`.md`, `.html`, `.pdf`) — the structured data feeds the next phase, while reports serve the assessor.

---

## 7. Key Differences: Standalone vs Plugin

| Aspect | Standalone (`.claude/`) | Plugin |
|--------|------------------------|--------|
| Skill names | `/hello` | `/plugin-name:hello` |
| Scope | Single project | Shareable across projects |
| Distribution | Manual copy | Marketplace install |
| Hooks location | `settings.json` | `hooks/hooks.json` |
| Best for | Personal workflows, quick experiments | Team sharing, community distribution |

---

## 8. Building a Plugin — Quick Reference

1. **Create directory structure:**
   ```bash
   mkdir -p my-plugin/.claude-plugin
   mkdir -p my-plugin/commands
   mkdir -p my-plugin/agents
   mkdir -p my-plugin/skills/my-skill
   ```

2. **Create manifest** (`my-plugin/.claude-plugin/plugin.json`):
   ```json
   { "name": "my-plugin", "description": "...", "version": "1.0.0" }
   ```

3. **Add a command** (`my-plugin/commands/do-thing.md`):
   ```markdown
   ---
   description: Does the thing
   allowed-tools: Read, Write
   ---
   Instructions for what Claude should do when /do-thing is invoked...
   ```

4. **Add a skill** (`my-plugin/skills/my-knowledge/SKILL.md`):
   ```markdown
   ---
   name: my-knowledge
   description: Reference knowledge Claude uses automatically when relevant
   ---
   # Knowledge Content
   ...
   ```

5. **Add an agent** (`my-plugin/agents/specialist.md`):
   ```markdown
   ---
   name: specialist
   description: Handles specialized task X
   model: inherit
   tools: [Read, Write]
   ---
   System prompt for the specialist agent...
   ```

6. **Test locally:**
   ```bash
   claude --plugin-dir ./my-plugin
   ```

7. **Create marketplace** for distribution:
   ```bash
   mkdir -p my-marketplace/.claude-plugin
   # Create marketplace.json listing your plugin
   ```

---

## 9. Debugging & Troubleshooting

| Issue | Solution |
|-------|----------|
| Plugin not loading | Validate JSON: `claude plugin validate .` |
| Commands not appearing | Ensure `commands/` at root, not inside `.claude-plugin/` |
| Hooks not firing | Make scripts executable: `chmod +x script.sh` |
| MCP server fails | Use `${CLAUDE_PLUGIN_ROOT}` for all paths |
| Path errors after install | All paths must be relative, starting with `./` |
| Version not updating | Bump version in `plugin.json` — caching uses version for cache keys |

**Debug mode:** `claude --debug` or `/debug` — shows plugin loading details, errors, and component registration.

---

## 10. Sources

- [Customize Cowork with plugins](https://claude.com/blog/cowork-plugins)
- [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins)
- [Create plugins — Claude Code Docs](https://code.claude.com/docs/en/plugins)
- [Plugins reference — Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
- [Plugin marketplaces — Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Use plugins in Cowork — Help Center](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
