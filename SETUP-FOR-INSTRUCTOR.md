# Setting this up (instructor notes — delete before publishing the template)

## Once, before term

### 1. Fix the two values that depend on Chatterbox

In `llm.py`:

- `BASE_URL` — verify against the IT wiki
- `MODEL` — get the exact string with
  `curl -H "Authorization: Bearer $KEY" https://chatterbox.ee.cooper.edu/api/v1/models`

### 2. Delete this file

It is instructor notes. Students should not get it.

```bash
cd ~/Documents/cooperClasses/SophProjects/course-template
rm SETUP-FOR-INSTRUCTOR.md
```

### 3. Make it a git repository

**The repository is this `course-template` directory, not the folder above it.**
`git init` runs *inside* `course-template`, so its root is `llm.py`,
`snapshot.py`, `check.py`, `labs/` and so on. Your syllabus, lab manual and
design notes live one level up in `SophProjects/` and are not part of it — no
student ever sees them.

```bash
cd ~/Documents/cooperClasses/SophProjects/course-template
git init -b main
git add -A
git commit -m "Course template"
```

Confirm you are committing what you think you are:

```bash
git ls-files
```

You should see about seventeen files, all of them from the list in `README.md`,
and **no `.docx`, no syllabus, no `SETUP-FOR-INSTRUCTOR.md`.**

Sanity check before it goes anywhere public:

```bash
git ls-files | grep -c '^\.env$'   # must print 0 — .env must never be tracked
python check.py --secrets            # must pass
```

### 4. Create the repo on GitHub and push

**With the `gh` CLI** (`brew install gh`, then `gh auth login`):

```bash
gh repo create COOPER-ORG/agentic-coding-template --public --source=. --push
```

**Without `gh`:** on github.com choose **New repository**, set the owner to your
course organisation, name it `agentic-coding-template`, and **do not tick "Add a
README", ".gitignore" or "license"** — an initialised repo will reject your first
push. Then:

```bash
git remote add origin https://github.com/COOPER-ORG/agentic-coding-template.git
git push -u origin main
```

### 5. Mark it as a template

On the repo page: **Settings → General → tick "Template repository"**. That is what
puts the green **Use this template** button on the page for students.

(`gh repo edit COOPER-ORG/agentic-coding-template --template` does the same thing
if your `gh` is recent enough.)

### 6. Check the Action ran

Push triggers `.github/workflows/check.yml`. Open the **Actions** tab — the secret
scan should be green. If the tab is empty, Actions is disabled for the
organisation; turn it on under **Settings → Actions → General**.

---

### ⚠️ Make the *template* public, and students' repos private

This is the one that will bite you. **A private template can only be used by people
who already have read access to it** — so a private template means adding all 16
students to the organisation before they can click "Use this template."

The template holds no secrets: skeleton files, `llm.py` with no key in it, and
`.env.example` with a placeholder. So:

- **template repo: public** — anyone can use it, no org membership needed
- **students' own repos: private** — their work stays theirs

If your department requires the template be private too, you will need to add every
student to the org as a member first. Budget time for that; it is not instant.

---

## Week 1, in class (15 min of the 45-minute setup block)

Each group: **Use this template** → name it `agentic-<surname>-<surname>` → make it
**private** → add the instructor as a collaborator with Read access.

Collect the 8 URLs on the Google form. That is the whole roster.

## Grading

```bash
gh repo list <org> --json name -q '.[].name' | while read r; do
  gh repo clone <org>/$r -- -q 2>/dev/null || (cd $r && git pull -q)
  (cd $r && echo "== $r" && python3 check.py $LAB)
done
```

`check.py` returns exit code 1 if anything fails, so it scripts cleanly.

## What the CI does

`.github/workflows/check.yml` runs on every push:

- **the secret scan fails the build** — this is the one that matters
- the lab checklist reports but never fails, since nobody has finished Lab 9 in Week 2

If a key does get committed, deleting it is not enough — the key is in the git
history and must be **revoked and reissued** in Chatterbox.

## Why snapshot.py exists

Provenance is the mechanism the quizzes rest on, so it must not depend on a
third-party tool's behaviour. aider auto-commits; OpenCode doesn't; aider had no
tagged release between Aug 2025 and Aug 2026. Tying the assessment to any of
that was a single point of failure.

`snapshot.py` also produces a *better* log: agent-generated commit messages
describe the diff, while the quiz asks students to reconstruct their intent.
Making them write "asked for X, got Y, kept Z" is the exercise, not overhead.

Consequence: **the coding agent is now a free choice.** Recommend OpenCode
(IT already does), permit anything, and stop worrying about which tool is
healthy in any given semester.

## Known limits

`check.py` checks that files exist and occasionally that they contain something
plausible. It cannot tell whether the work is good. That is what the quizzes and
the adversarial run are for — do not let a green check substitute for reading
the submission.
