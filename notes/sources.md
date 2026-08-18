# Source material

Everything the slides rest on that is **not** a live `docs.cscs.ch` page: documentation
previews, material from other repositories, and things that are true but written down
nowhere. Keep this file honest — if a claim in the slides comes from here rather than
from the public documentation, it must say so at the point of use, as a `TODO(verify)`.

## Storage documentation preview — `/442`

<https://cscs-docs-preview.svc.cscs.ch/442> — the storage and ML Platform pages as they
will be after the next merge. Module 2 is written from this, not from the live pages,
because the live ones are missing two mount points.

What is only here, and not yet on `docs.cscs.ch`:

- **`datacache`** — `/iopsstor/datacache/cscs/swissai/<project>`. A project-level working
  area on fast Iopsstor. "Like scratch, it is fast NVMe storage and is **not backed up**.
  Unlike scratch, it has **no cleanup policy**: files are never deleted automatically, and
  the project owns its data lifecycle and space hygiene within a project quota on capacity
  and inodes." Not provisioned by default: the PI opens a Service Desk ticket with the use
  case and the space and inodes required, and CSCS reviews it before creating the area.
  **Goes live on 26 August 2026, after the maintenance** — the day of the session. That
  timing is Andrea's, not the page's.
- **Ritom scratch** — "On Clariden, a further scratch path is available on Ritom (a VAST
  file system) at `/ritom/scratch/cscs/$USER`." Its cleanup policy "is being finalised",
  which is why module 2 says so on the slide rather than inventing a number.
- The scratch usage recommendations, and the instruction to move results to the project
  store after a job "for example with `rclone` on the `xfer` queue".

Re-point every module 2 link once this is merged, and re-check the numbers at that point.

### Full scan of the storage section, for whoever owns module 2

Four pages under `/storage/`, plus one guide outside it. Verified quotations:

- **`/storage/filesystems/`** — Home: "There is no cleanup policy on Home", 50 GB and
  500,000 inodes, "Daily snapshots for the last seven days ... in `$HOME/.snapshot`",
  and "Backups to tape storage are currently **being implemented** for Home directories"
  — so do not promise them. Capstor scratch: 150 TB, 1 million inodes, "a soft quota
  grace period of two weeks", files "not accessed in 30 days" deleted. Iopsstor scratch:
  files "not accessed in 14 days" deleted; **its quota is not stated anywhere**. Store:
  no cleanup, "the three most recent copies of every file backed up to tape every 24
  hours", retained three months after the project ends. The deletion criterion is **last
  access**, not age or modification.
- **`/storage/transfer/`** — Globus mount points are listed as `/iopsstor/scratch/cscs`,
  `/capstor/scratch/cscs`, **`/ritom/scratch/cscs`**, `/capstor/store/cscs` and
  `/vast/users/cscs`. Note ritom appears here with no Clariden qualifier, which supports
  Andrea's correction. Concrete figure: "copying a 1 TB directory from `/capstor/store`
  to `/iopsstor/scratch` ... takes on the order of 5 minutes on Alps (roughly 3 GB/s)".
  `xfer` jobs chain with `--dependency=afterok:$SLURM_JOB_ID`.
- **`/guides/storage/`** — the page module 2 most needs and the one easiest to miss,
  because it sits outside the storage section. Lustre striping
  (`lfs setstripe --stripe-count 32 --stripe-size 4M`, 4 MB block size "gives good
  throughput"), VAST/ROMIO tuning for Ritom, and "Lustre is not well suited to handling
  many small files" — demonstrated with a PyTorch virtual environment of **22,806
  inodes**, with the recommendation to squash it into a squashfs image. That example is
  now on the module 2 inodes slide and hands off to module 3.
- **`/storage/longterm/`** — not on a slide, the long-term-storage slide was cut. Kept
  here because the numbers are concrete and a PI may ask: `lts.cscs.ch`, 10-year
  retention, persistent identifiers, "2 TB of LTS storage quota (for 10 years) free of
  charge per project" for User Lab, then "CHF 600.- for each terabyte (for 10 years)".
  The PI grants LTS permissions to team members through the portal.
- **`/storage/object/`** — also not on a slide. Ceph Object Gateway, S3-compatible, at
  `https://rgw.cscs.ch`. Works with the AWS CLI, s3cmd and Cyberduck; quota via the
  `/_quota` endpoint.

## Not documented anywhere yet — Andrea, as ML Platform service manager

These are load-bearing claims in module 1 that no public page currently backs. They are
correct, but they are marked `TODO(verify)` in the slide source because a reviewer
cannot check them.

**See `notes/docs-gaps.md`** — the same list written up as a ready-to-paste issue for
the documentation repository. Add to it as modules 2 to 5 are written.

- **Who sees consumption in the portal.** Not a PI-only view. *Every* project member
  sees the project-level total. Per-user usage is visible inside the detail of each
  individual resource. There is **no** per-user total across the whole project.
- **The per-role permission matrix** is not written down. The portal documents the three
  role names and that administrators and managers can invite users and assign roles;
  everything beyond that is folklore.
- **Account identity and re-enabling.** The docs say an account is bound to projects and
  closes with the project "unless the account is also part of another open project".
  They do not say that the **email address is the unique identity** (one address, one
  account), nor that a **later invitation re-enables the same account** instead of
  creating a new one. Both are true and both are worth documenting — they are the
  difference between "my account was deleted" and "my account is dormant".
- **"We are actively improving these views"** on the consumption slide is a
  forward-looking statement, not a documented fact: better usage visualisation for
  compute, for storage, and for the new inference resources. It is Andrea's to make
  from the stage as service manager. Re-read it in the week before 26 August 2026 —
  roadmaps move, and a promise made to this particular room will be remembered.
- **Changing an existing member's role** is not documented at all —
  `docs.cscs.ch/accounts/waldur/` has exactly four sections (the tool, log in, select
  the organisation, invite users) and stops at the invitation. The expectation is that
  a PI and a deputy PI can both change a role from the Team tab, but nobody has written
  it down, so module 1 deliberately claims nothing either way. Click it, then fix the
  docs page.

## ML Platform project policies — still a docs preview

<https://cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/>

**This is the authority for the small/large slide in module 1** and for a good part of
module 2. It is being merged into `docs.cscs.ch` in the coming days, so every reference
to it is currently marked `TODO(verify)` in the slide source. Swap the links and
re-check the numbers once it lands.

What it says, for the record:

- **Small**: typical budget up to 32,000 GPUh, 6 months, rolling start ("as soon as
  they are accepted", default the first day of the following month, delayable by up to
  3 months on request), storage default 1 TB and 1,000,000 inodes.
- **Large**: typical budget from ~500,000 GPUh, 12 months, starts at the scheduled time
  of the call, normally 1 July or 1 January, storage must be stated in the proposal
  with no default applied.
- A large proposal can be **reduced to a small grant** rather than rejected.
- Credit is fixed for the whole duration, with monthly expected consumption targets.
  Exhausted projects can fall back to the low-priority partition.
- **90-day grace period** for data retrieval after the project ends — module 2 material.
- Section headings: project types · core project data · compute budget · storage budget ·
  other resources · start · duration · users and job priority · appendix on computing
  compute consumption.

## Swiss AI Initiative compute grants

<https://www.swiss-ai.org/compute-grants> — the application side, not CSCS.

- Large projects (>500k GPU hours): **4th call open 3 August to 14 September 2026**,
  twice a year. Contact `large-grants@swiss-ai.org`.
- Small projects (≤32k GPU hours): rolling reviews. Contact `small-grants@swiss-ai.org`.
- Roughly 10–20 million GPU hours to be distributed in 2026. Open to researchers in
  Europe and beyond.

The call dates are time-sensitive and live on swiss-ai.org, not on docs.cscs.ch —
**re-check them the week before the session**. Detailed submission instructions sit in
linked Google Drive documents that were not read.


## ML Platform drop-in repository

`~/Development/GitHub/ml-platform-drop-in` — Andrea's bi-weekly drop-in sessions.
Public at `github.com/candrea85/ml-platform-drop-in`.

**Reused here:**

- **Branding.** Palette (`#D61F26` red, `#1A1A1A` dark, `#F7F7F8` light), Inter,
  the header/footer band, and the card / accent-bar / URL-box vocabulary were ported
  into `slides/theme/cscs.css`.
- **Logos.** `assets/logos/cscs.png` and `assets/logos/eth.png` were extracted from the
  base64 blobs in `2026-04-08-ssh-service/presentation/slides.html`.
  `TODO(brand)`: confirm these are the current approved assets.

**Good for module 1, not yet used:**

- Service accounts turned out to be documented after all, on
  `docs.cscs.ch/accounts/account-create/`: scoped to a single project, grant access to
  all its resources, and the **project PI** requests one from a Platform Manager via a
  Service Desk ticket. Module 1 cites the docs for this, not the drop-in material.
  That same page describes exactly two account types — regular user and service
  account — and has no notion of "non-Swiss-AI account types", which is why that line
  was dropped from the out-of-scope slide.
- `2026-04-08-ssh-service/README.md` is the deep reference on the new SSH service:
  user-account vs service-account flows, the `hpc-ssh` / `api-ssh-service` endpoints,
  `1min` vs `1d` durations, IP-restricted and force-command keys, and how a PI gets a
  service account (support ticket, then the PI or deputy creates it in the portal).
  Too much detail for a 12-minute module — this is Q&A and backup-slide material.
- It also records that legacy `sshservice.cscs.ch` / `sshservice-cli` were retired in
  **May 2026**, which is why module 1 mentions them only in the "skipped" slide.

## CUG 2026 — "A Lightweight Web-UI for HPC and AI"

`~/Downloads/various/CUG26/CUG-26-a-lightweight-web-ui-for-hpc-and-ai.pptx`
(Pagnamenta, Ceriani, Palme, Dorsch — 29 April 2026, 20 slides with speaker notes.)

**This is module 4 material, not module 1.** It covers the HPC Console
(open-source as `firecrest-ui`) built on FirecREST: cluster-health dashboard, job
listing and filtering, job submission from the browser, log inspection with shareable
per-job URLs, Grafana integration, and the filesystem browser with large-file upload.
Whoever owns module 4 should mine it — the screenshots and the workflow framing are
already done and already approved for an external audience.

## CUG 2026 — "Transitioning User and Identity Management for Alps"

`~/Desktop/All/CUG2026/CUG-26-transitioning-user-and-identity-management-for-alps-30-04-2026.pptx`
(Ceriani et al. — 30 April 2026, 16 slides with speaker notes.)

**Background, not slide content.** Too internal for this audience, but it gives the
one sentence that explains the whole portal story if somebody asks in the discussion:

> Waldur (`portal.cscs.ch`) is where project and resource **workflows start**; the
> Identity Management Platform (IMP) **owns identity state and lifecycle**. The legacy
> User Management Portal (UMP) did both for over ten years and was migrated gradually,
> without a cut-over.

Also useful as scale context: roughly 14k managed users, 3–4k active, ~4k projects,
growth driven largely by AI workloads.
