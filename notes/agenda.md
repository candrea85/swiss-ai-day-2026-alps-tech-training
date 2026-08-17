# Agenda — Alps technical training

**Swiss AI Initiative Annual Meeting 2026 · Wednesday 26 August 2026, Bern**
Slot: 90 minutes, around 13:30 (may shift slightly).
Structure: ~60 min presentation + ~30 min open discussion.

**60 minutes is a hard ceiling.** If a module grows, another one shrinks — say so
explicitly rather than overrunning.

## Running story

One Swiss AI project, from "we need compute" to "the model is trained and being
served", carried by two personas:

- **Anna** — the PI. Requests the project, runs the team, watches the budget.
- **Ben** — a PhD student who joins her project partway through.

Every module should be able to say where we are in that story.

## Modules

| # | Module | Budget | Owner | Slides | Drafted | Status |
|---|---|---|---|---|---|---|
| 0 | Welcome — what Alps and the ML Platform are, what this hour covers | 5 min | TBD | `slides/00-intro.md` | 5 | scaffold |
| 1 | **Project lifecycle and access** — request, portal, invites, resources, first login | **12 min** | **Andrea** | `slides/01-project-access.md` | 12 | **on budget** |
| 2 | Data and storage lifecycle — filesystems, quotas, moving data in, where training data lives | 13 min | TBD | `slides/02-data-storage.md` | 8 | scaffold, 5 min spare |
| 3 | Software and containers — uenv, Container Engine, Alps-extended images, best practices | 15 min | TBD | `slides/03-software-containers.md` | 8 | scaffold, 7 min spare |
| 4 | Running and automating — Slurm, job efficiency, JupyterLab, FirecREST, inference and serving | 12 min | TBD | `slides/04-running-jobs.md` | 8 | scaffold, 4 min spare |
| 5 | Wrap-up — support channels, User Day (28 Aug), what we did not cover | 3 min | TBD | `slides/05-wrapup.md` | 4 | scaffold |
| — | Open discussion — planned work, suggestions, requests | 30 min | all | — | — | — |
| — | Backup, shown on request only | — | — | `slides/06-backup.md` | 7 | HPC Console block done |

**45 of 60 minutes drafted.** The slack is deliberate: modules 2 to 4 are scaffolding, and
their owners should spend it on the one worked example they know best, not on more
bullets. `make check` reports the split and excludes backup slides from the budget.

### What "scaffold" means

Modules 0 and 2 to 5 were drafted from `docs.cscs.ch` so that no owner starts from a
blank page. Every factual claim is sourced and every unsourced one carries a
`TODO(verify)`. They are **not finished modules**: the voice is generic, several slides
are marked `PLACEHOLDER`, and each one is missing the thing only its owner can supply —
a real command, a real screenshot, a real number from a real run. Owners should rewrite
freely rather than treat this as a draft to defend.

## Hand-offs between modules

- **1 → 2**: Ben has a shell on Clariden and an empty home directory. His first
  question is where to put two terabytes of training data.
- **2 → 3**: the data is on the right filesystem. Now it needs an environment that
  can read it.
- **3 → 4**: the environment exists. Now it has to run at scale, repeatedly.
- **4 → 5**: the model trains and serves. Where do you go when it breaks?

## Backup slides (after the wrap-up)

In `slides/06-backup.md`. Mentioned on the wrap-up slide, shown only if the discussion
asks for them:

- **HPC Console** — drafted, 5 slides, about 5 minutes. Ready.
- Kubernetes — not written
- Post-training and RLHF workflows — not written
- Advanced multi-node scaling — not written
- GPU-efficiency deep dive — not written

### Open decision: where the HPC Console block lives

It is drafted as backup so the placement decision stays open. Three options, and moving
between them costs nothing — cut the block and paste it:

1. **Backup** (where it is now). Zero budget impact. Shown only on request.
2. **Inside module 4**, whose owner would give up about 5 of their 12 minutes. Zero
   impact on the 60-minute total.
3. **A section of its own**, taking 5 minutes from the 30-minute discussion: 65 + 25.
   This changes the shape of the session and needs the agreement of all the presenters,
   not just one module owner.

Andrea's view is that the content is worth showing to this audience — many are
comfortable with PyTorch and not with Slurm, and a browser lowers that barrier — but
that option 3 is not one person's call to make.

## Closing

End by pointing the audience at the **CSCS User Day, Friday 28 August 2026** — two
days later. Reuse and cross-reference User Day material rather than duplicating it.

## Module 1 detail

Twelve slides — a divider plus **eleven** content slides — so about 12 minutes against
a 12-minute budget. On time, but one slide over the "max 10 content slides" ceiling in
CLAUDE.md §6. The extra slide is "Spend it linearly, or you lose it": the expected /
minimal consumption rule with its 15–50% grace, the low partition, and the 90-day
retrieval window, drawn as a single timeline. It earns its place because it is the only
slide in the module that changes what a PI does on Monday morning. If the module has to
shrink, the cut order is: the "deliberately skipped" slide first (it can become a
sentence over the hand-off), then merge the portal tour into the invitations slide.

**The module is split by audience, and says so.** The divider announces it, and every
content slide carries a marker top-right: *PIs and deputies* for getting a project, the
portal, invitations and the budget; *Everyone* for the account lifecycle, MFA, keys and
the jump host. The order already groups them — administration first, then access — so
nobody has to track two threads at once. Worth copying in modules 2 to 5: the same
audience split runs through the whole session.

Speaker notes on every slide. Outstanding before the session:

- Two screenshots — see `assets/screenshots/TODO.md`.
- Three `TODO(verify)` markers in `slides/01-project-access.md`: the portal consumption
  view, the MLP small/large numbers, and every number on the linear-consumption slide.
  The last two are the same root cause — the policies page is still a docs preview.
- The Swiss AI call dates on slide 3 are time-sensitive. Re-check them the week before.

Module 1 also carries the small/large project explanation, which arguably belongs in
module 0. If module 0's owner would rather cover it, module 1 drops slide 3 and gains
a minute of slack.
