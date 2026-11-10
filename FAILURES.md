# Failure log

One entry per lab, per group. Append yours at the bottom; never edit anyone else's.

**An entry must name a specific input and a specific wrong output.** "It didn't work"
is not an entry. Bugs in your own Python are not entries either — this file is only
for what the *model* did.

By Week 11 this is a catalogue of a hundred real failure modes of the model we are
all building on. You will use it when you write your eval cases in Lab 9.

---

## Lab 0 — Example (delete nothing, just append below)

```
Input:    asked for one tool call, prompt in format.md v2
Expected: a single JSON object
Got:      two JSON objects, the second malformed, wrapped in prose
Did:      parser now takes the first valid object and logs the rest
```

---

## Lab 1

```
Input:    asked for recent information
Expected: correct information
Got:      confidently wrong information
Did:      enabled web search to increase accuracy
```

## Lab 2

```
Input:    asked for script output in chat window
Expected: working script with user input
Got:      single function
Did:      had it write the file instead to make sure the output format was the cause.
```

## Lab 3
```
Input:    "implement lgrep in python according to spec-v1.md. do not look at the tests. they will be used later to evaluate this draft"
Expected: working script
Got:      broken -n argument
Did:      asked it to fix, reiterating the instruction.
```

## Lab 7
```
Input (antigravity): > using the mcp, classify the files
Expected: tool calls, files to be classified
Got: agent reading unrelated files
Did: corrected the agent
LOG:
○ Thought for 5.1s (Initial hypothesis: utilize the available tools within the MCP server environment to classify files. Found a `classifier` MCP with tools for file c...)
● Ran (ls -la /Users/noahsmith/.gemini/antigravity-cli/mcp/classifier) failed (ctrl+o to expand)

Command
  ⎿  User declined the tool call

> do not run any other commands

● Explored 4 files (instructions.md, get_unclassified_file.json, get_categories.json, +1) (ctrl+o to expand)

────────────────────────────────────────────────────────────
> do not read files. only use the mcp.
```