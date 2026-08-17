# Source material

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


Material outside this repository that we are reusing, and what each piece is good for.
Keep this file honest: if a claim in the slides came from here rather than from
`docs.cscs.ch`, it must say so at the point of use.

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
