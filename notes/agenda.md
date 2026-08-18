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
| 0 | Welcome — what Alps and the ML Platform are, what this hour covers | 5 min | TBD | `slides/00-intro.md` | 6 | scaffold |
| 1 | **Project lifecycle and access** — request, portal, invites, resources, first login | **12 min** | **Andrea** | `slides/01-project-access.md` | 12 | **on budget** |
| 2 | Data and storage lifecycle — filesystems, quotas, moving data in, where training data lives | 13 min | TBD | `slides/02-data-storage.md` | 8 | scaffold, 5 min spare |
| 3 | Software and containers — uenv, Container Engine, Alps-extended images, best practices | 15 min | TBD | `slides/03-software-containers.md` | 8 | scaffold, 7 min spare |
| 4 | Running and automating — Slurm, job efficiency, JupyterLab, FirecREST | 12 min | TBD | `slides/04-running-jobs.md` | 7 | scaffold, 5 min spare |
| 5 | Wrap-up — support channels, User Day (28 Aug), what we did not cover | 3 min | TBD | `slides/05-wrapup.md` | 4 | scaffold |
| — | Open discussion — planned work, suggestions, requests | 30 min | all | — | — | — |
| — | Backup, shown on request only | — | — | `slides/06-backup.md` | 7 | HPC Console block done |

**46 of 60 minutes drafted.** The slack is deliberate: modules 2 to 4 are scaffolding, and
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
- **2 → 3**: the data is on the right filesystem — including the new `datacache`, which
  goes live the morning of the session. Now it needs an environment that can read it.
- **3 → 4**: the environment exists. Now it has to run at scale, repeatedly.
- **4 → 5**: the model trains. Where do you go when it breaks?

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

## Storage: one thing lands the morning of the session

`datacache` — `/iopsstor/datacache/cscs/swissai/<project>` — goes live on **26 August**,
after the maintenance. Module 2 has a slide on it, marked as new, and module 0's
maintenance slide points forward to it so the outage has an upside.

Confirm on the morning that it is actually available. If the maintenance slips, the
module 2 slide says "from today" and would be wrong on stage.

## Before the session: two documentation merges

This is the deck's biggest external dependency, and it is not in our hands.

| Preview | Covers | Slides that depend on it |
|---|---|---|
| `/463/platforms/mlp/policies/` | small vs large, expected/minimal consumption, the 15–50% grace, the `low` cap, the 90-day grace | module 1, slides 2 and 7 |
| `/442` storage and MLP pages | `datacache`, the Ritom scratch, cleanup and backup policies, the transfer figures | module 2, most of it |

Two different failure modes, and the second is the nastier one:

- `docs.cscs.ch/platforms/mlp/policies/` currently **404s**. The slide that used to print
  it now prints the parent page instead. Upgrade it once the merge lands.
- The storage URLs **already resolve** — but the live pages do not yet mention
  `datacache` or Ritom. So a slide can cite a working link whose content does not back
  what was just said. That is worse than a dead link, because it looks like we are wrong.

Check both the morning of the session. If the storage merge has not happened, say so on
the slide rather than letting somebody discover it afterwards.

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

- One screenshot, plus three optional ones — see `assets/screenshots/TODO.md`.
- Five `TODO(verify)` markers in `slides/01-project-access.md`: the portal consumption
  view, changing an existing member's role, the account identity and re-enabling, the
  MLP small/large numbers, and every number on the linear-consumption slide. Two of the
  five close on their own when the policies page is merged; the other three need somebody
  to write a paragraph on `docs.cscs.ch`. All of them are in `notes/docs-gaps.md`.
- The Swiss AI call dates on slide 2 are time-sensitive. Re-check them the week before.

Module 1 also carries the small/large project explanation, which arguably belongs in
module 0. If module 0's owner would rather cover it, module 1 drops slide 3 and gains
a minute of slack.
