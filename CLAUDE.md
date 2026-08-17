# CLAUDE.md — Alps Technical Training @ Swiss AI Initiative Annual Meeting 2026

## 0. Language policy (important)

- **Every artifact in this repository must be in English**: slides, speaker notes, handouts,
  code comments, commit messages, file names, issue text. No exceptions.
- Use British/international English, spell out acronyms on first use.
- Contributors may prompt in whatever language they prefer; that never changes the rule
  above. Personal preferences of this kind belong in an untracked `CLAUDE.local.md`.

## 1. What this repo is

Material for the **Alps technical training** session that CSCS delivers at the
**Swiss AI Initiative Annual Meeting**, Wednesday **26 August 2026**, Bern.

- Slot: **90 minutes**, scheduled around 13:30 (may shift slightly).
- Structure: **~60 min presentation + ~30 min open discussion / Q&A**.
- The session is delivered by several CSCS people; each owns one module (see §5).
- It sits two days before the **CSCS User Day (Friday 28 August 2026)** — deliberately
  reuse and cross-reference User Day material instead of duplicating it, and end by
  pointing the audience there.

### Audience

Researchers of the Swiss AI Initiative who **already use or are about to use Alps**,
plus their **PIs and deputy PIs**. Assume:

- Comfortable with Python, PyTorch, the shell and Git.
- Mostly **not** HPC experts: Slurm, SSH certificates, parallel filesystems, containers
  on HPC and quota mechanics are the parts they get wrong.
- Some are PIs who must administer a project (invite people, watch the budget) and have
  never opened the portal.
- Many already have an account — so onboarding content must be **fast and skippable**,
  not a tutorial.

### Goal of the session

Walk the audience through **the life of a project on Alps**, end to end, so that each
person leaves knowing *where the authoritative documentation is* for the next step they
personally have to take. We are not teaching everything — we are building a map.

## 2. Non-negotiable content rules

1. **Never invent CSCS facts.** Every technical claim (path, quota, command, flag,
   hostname, role name, URL) must be traceable to <https://docs.cscs.ch> or to material
   the user provides. If you cannot verify something, write
   `<!-- TODO(verify): ... -->` in the source and flag it in your reply. Do not guess.
2. **Link to the docs, always.** Every content slide carries at least one
   `docs.cscs.ch` deep link in the footer or speaker notes. The deck is a signpost, not
   a replacement for the documentation.
3. Prefer `docs.cscs.ch` over the legacy `user.cscs.ch` and over Confluence KB pages.
   If only a legacy page exists, mark it as legacy.
4. **Commands must be copy-pasteable and real.** No pseudo-commands, no invented flags.
5. Screenshots of `portal.cscs.ch` and `user-account.cscs.ch` go in `assets/screenshots/`.
   Claude cannot produce them — when a screenshot is needed, insert a placeholder slide
   and list it in `assets/screenshots/TODO.md` with the exact view to capture.
6. Keep everything **vendor- and cluster-accurate for the ML Platform**: the audience's
   systems are **Clariden** (GH200) and **Bristen** (A100), not Daint/Eiger.

## 3. Deliverables

| Path | What |
|---|---|
| `slides/00-intro.md` … `slides/05-wrapup.md` | One Marp Markdown file per module |
| `slides/theme/cscs.css` | Shared Marp theme (CSCS colours, footer with docs link) |
| `handout/quickstart.md` | One-page cheat sheet, exported to PDF, given to attendees |
| `assets/` | Images, diagrams, screenshots |
| `build/` | Generated output — **git-ignored, never edit by hand** |
| `notes/agenda.md` | Live agenda with per-module time budget and owner |

## 4. Toolchain — Marp (decided)

Slides are **Markdown compiled with [Marp](https://marp.app)**. Rationale: the source is
plain text (diffable, reviewable, editable by Claude), and one source produces all three
outputs we need, **including speaker notes**:

- `marp slides/deck.md -o build/deck.pptx` → PowerPoint, **with Marpit presenter notes
  carried into PowerPoint's speaker-notes pane** → real Presenter View on the venue laptop.
- `marp slides/deck.md -o build/deck.html` → self-contained HTML; press `p` for the
  built-in presenter view (notes + timer + next slide).
- `marp slides/deck.md --pdf --pdf-notes -o build/deck.pdf` → PDF to circulate afterwards,
  with the notes attached as PDF annotations.

Caveats to respect:

- Do **not** use `--pptx-editable`: that experimental mode drops presenter notes.
- Speaker notes are written as **HTML comments** in the Markdown:
  `<!-- Say this out loud. Mention the 50 GB home quota. -->`
- Always build all three targets before declaring a task done.

Build entry point: a `Makefile` at the repo root with `make pptx`, `make html`, `make pdf`,
`make all`, `make clean`. Create it if it does not exist.

## 5. Agenda and module ownership (60 min)

The spine is a **single running story**: one Swiss AI project, from "we need compute" to
"the model is trained and being served". Use two recurring personas — **Anna, the PI**,
and **Ben, a PhD student who joins her project** — so every module can say *where we are
in the story*.

| # | Module | Budget | Owner |
|---|---|---|---|
| 0 | Welcome, what Alps/MLP is, what this hour covers | 5 min | TBD |
| 1 | **Project lifecycle & access** — request, portal, invites, resources, first login | **12 min** | **Andrea** |
| 2 | Data & storage lifecycle — filesystems, quotas, moving data in, where training data lives | 13 min | TBD |
| 3 | Software & containers — uenv, Container Engine, Alps-extended images, best practices | 15 min | TBD |
| 4 | Running & automating — Slurm, job efficiency, JupyterLab, FirecREST, inference/serving | 12 min | TBD |
| 5 | Wrap-up — support channels, User Day (28 Aug), what we did not cover | 3 min | TBD |
| — | Open discussion: planned work, suggestions, requests | 30 min | all |

Rules for the agenda:

- **60 min is a hard ceiling.** If a module grows, something else shrinks — say so
  explicitly rather than silently overrunning.
- Topics that do **not** fit the main line go to **backup slides** after the wrap-up:
  Kubernetes, post-training/RLHF workflows, advanced multi-node scaling, GPU-efficiency
  deep dive. Mention they exist, show them only if asked in the discussion.
- Each module ends with a **"Where to read more"** slide of docs links.

## 6. Module 1 in detail (Andrea's part — the one to develop first)

**Time budget: 12 minutes, max 10 content slides.** This is plumbing, not the intellectually
interesting part of the session — the value of the hour is in modules 2–4. Module 1 must be
**fast, screenshot-driven and confident**, and push detail into backup slides and the handout.
Do not let it grow.

Storyline: *Anna gets a project → Anna adds Ben → Ben logs in → both watch the budget.*

1. **What a "project" is at CSCS** and who is who — Project Administrator (PI),
   Project Manager (deputy PI), Project Member. What each role can and cannot do.
2. **Getting a project**: the request path, what to prepare *before* asking for a large
   allocation — realistic GPU-hour estimate, expected GPU efficiency, and the **data
   footprint** (how much, where it comes from, how long it must stay). Message: large
   projects should arrive *ready to run*, not ready to start learning.
3. **portal.cscs.ch tour**: organisation → project → Team → Invitations;
   single invite vs bulk CSV; assigning roles.
4. **Resources in the portal**: what the project has been granted, and how to read
   consumption. Message for PIs: check this monthly, not in the last week.
5. **First login for the new member**: create the account, set up **MFA**, generate a
   local ED25519 key, get it **signed by CSCS** (`cscs-key` CLI, or the
   `user-account.cscs.ch` dashboard), note that signed keys are **valid one day** and
   there is a **limit of 5 keys per day**.
6. **Connecting**: everything goes through the **`ela.cscs.ch` jump host**; show a working
   `~/.ssh/config` block with `ProxyJump`, and `ssh -A`. Mention SSH tunnelling to a
   service on a compute node via Ela as a one-liner (details → docs).
7. **Hand-off slide**: "you now have an account, a project and a shell — the rest of the
   hour is what you actually do with them."

Deliberately **out of scope** for module 1 (say so on a slide, one line each):
password/MFA troubleshooting, legacy key management, non-Swiss-AI account types,
Kubernetes/HPC-console specifics beyond a pointer.

Produce alongside the slides: **`handout/quickstart.md`**, a single printable page with
the exact commands for key signing, the `~/.ssh/config` snippet, the portal URL and the
support contact — so Andrea can move quickly on stage and say "it is all on the handout".

## 7. Slide style guide

- **One idea per slide.** Max ~6 bullet lines; ~10 words per line. If it needs more,
  it is two slides or it is speaker notes.
- **Speaker notes are mandatory** on every content slide: what to say, the transition to
  the next slide, and the doc link. Write them as **short bullets in simple English** —
  they are glanced at on stage, not read aloud, and most of us are not presenting in our
  first language. Short sentences, plain words, no idioms. Use these markers so a
  presenter can find their place instantly:

  ```
  SAY:
  - One short line per idea.
  POINT AT / READ OUT LOUD / EXPECT THIS QUESTION:   (physical cues, only when needed)
  NEXT: the one-line hand-off to the following slide.
  DOCS: docs.cscs.ch/...
  ```

  Every note block ends with `NEXT:` and `DOCS:`. See `slides/01-project-access.md`
  for the reference implementation.
- Slide titles are statements, not labels: "Signed keys expire after one day", not "SSH keys".
- Prefer a diagram or an annotated screenshot over a bullet list for anything spatial
  (storage layout, login path, portal navigation).
- **Live demos: avoid.** Conference wifi and MFA will betray you. Use screenshots or a
  pre-recorded asciinema/GIF, and keep the real demo as a fallback for the Q&A.
- Every module's final slide is "Where to read more" with 3–5 `docs.cscs.ch` links.
- Footer on every slide: session name + `docs.cscs.ch`.
- Do not use CSCS/ETH logos or brand colours you have not been given — put a
  `TODO(brand)` marker instead.
- **Never say or show "Waldur"** to this audience. They know the tool as
  **`portal.cscs.ch`**, which is the CSCS-customised deployment. This applies to slide
  text, speaker notes, the handout and any link label. Where a docs link is needed,
  prefer the parent page <https://docs.cscs.ch/accounts/> over the `/accounts/waldur/`
  URL, whose path carries the name. The word is fine in `notes/` and in `TODO(verify)`
  comments, which never reach the room.

## 8. Canonical references (verified, use these)

Accounts, projects, access:

- Accounts and Projects — <https://docs.cscs.ch/accounts/>
- The portal, `portal.cscs.ch` — <https://docs.cscs.ch/accounts/waldur/>
  (link the parent page <https://docs.cscs.ch/accounts/> in anything the audience sees;
  the URL above names the upstream product, which we do not say — see §7)
- Creating a new account — <https://docs.cscs.ch/accounts/account-create/>
- Multi-factor authentication — <https://docs.cscs.ch/access/mfa/>
- SSH access, key signing, Ela jump host — <https://docs.cscs.ch/access/ssh/>

Platform and clusters (this audience):

- Machine Learning Platform — <https://docs.cscs.ch/platforms/mlp/>
- Clariden (GH200) — <https://docs.cscs.ch/clusters/clariden/>
- Bristen (A100) — <https://docs.cscs.ch/clusters/bristen/>
- Alps research infrastructure — <https://docs.cscs.ch/alps/>

Data, software, running:

- Storage and data management — <https://docs.cscs.ch/storage/>
- File systems — <https://docs.cscs.ch/storage/filesystems/>
- uenv — <https://docs.cscs.ch/software/uenv/>
- Container Engine — <https://docs.cscs.ch/software/container-engine/>
- ML software stack — <https://docs.cscs.ch/software/ml/> · PyTorch — <https://docs.cscs.ch/software/ml/pytorch/>
- ML tutorials (inference, fine-tuning, training) — <https://docs.cscs.ch/tutorials/ml/>
- Running jobs / Slurm — <https://docs.cscs.ch/running/> · <https://docs.cscs.ch/running/slurm/>
- JupyterLab — <https://docs.cscs.ch/access/jupyterlab/>
- FirecREST — <https://docs.cscs.ch/access/firecrest/> · v2 docs — <https://eth-cscs.github.io/firecrest-v2/>

Legacy (use only if nothing on docs.cscs.ch covers it, and label as legacy):
`user.cscs.ch`, `confluence.cscs.ch/display/KB/…`.

## 9. How to work in this repo

- Before writing slides on a topic, **fetch the relevant docs.cscs.ch page** and work
  from it. Do not write from memory.
- Work **module by module**. Do not generate the whole 60-minute deck in one pass.
- After editing any `slides/*.md`, run `make all` and report the resulting **slide count
  and estimated speaking time** (≈1 min per content slide, plus demos).
- If a module exceeds its time budget, say so and propose what to cut — do not silently
  overflow.
- Keep `notes/agenda.md` in sync whenever a budget or owner changes.
- Commit messages in English, imperative mood, one module per commit where possible.

## 10. Definition of done (per module)

- [ ] Fits its time budget at ~1 min/slide
- [ ] Every factual claim linked to a `docs.cscs.ch` page
- [ ] Speaker notes on every content slide
- [ ] "Where to read more" closing slide
- [ ] No `TODO(verify)` left unresolved (or all listed explicitly in the reply)
- [ ] `make all` produces PPTX, HTML and PDF without errors
- [ ] Screenshot placeholders listed in `assets/screenshots/TODO.md`
