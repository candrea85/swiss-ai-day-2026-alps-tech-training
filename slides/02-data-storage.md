---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!--
DRAFT — owner TBD. Written as scaffolding so module 2 does not start from a blank page.
Budget: 13 minutes, so about 13 slides including the divider. Currently under that on
purpose: there is room for the owner to add the one thing they care about most.

Every claim is traceable, but several come from the storage documentation that is still
a preview at cscs-docs-preview.svc.cscs.ch/442 — see the TODO(verify) markers.
-->

<!-- _class: divider -->

<span class="tag">Module 2 · 13 min</span>

# Data and storage

Ben has a shell and an empty home directory. Where do two terabytes of training data go?

<!--
START AT T+17:00. Check the presenter timer now.
CUT IF LATE: Cut "Inodes run out before terabytes do". Say it in one line over the mount-point table.
SAY:
- Ben is in. He has a shell on Clariden and an empty home directory.
- His first real question is where to put his data.
- Getting this wrong is the most expensive mistake on this platform.
- Wrong filesystem means slow training. Or deleted data.
NEXT: There are four places, and they are not interchangeable.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/filesystems/' -->
<div class="audience all">Everyone</div>

# Six mount points, and they are not interchangeable

Putting data in the wrong one is the most common and most expensive mistake here.

| | Path | For | Cleanup |
|---|---|---|---|
| **Home** | `/users/$USER` | code, scripts, config — 50 GB | none |
| **Scratch** `iopsstor` | `/iopsstor/scratch/cscs/$USER` | training data, random I/O | **14 days** |
| **Scratch** `capstor` | `/capstor/scratch/cscs/$USER` | checkpoints, sequential I/O | **30 days** |
| **Scratch** `ritom` | `/ritom/scratch/cscs/$USER` | VAST — a third scratch | **being finalised** |
| **Project store** | `/capstor/store/cscs/swissai/<project>` | shared, medium term, backed up | none |
| **Project** `datacache` | `/iopsstor/datacache/cscs/swissai/<project>` | shared fast datasets — **on request** | none |

<div class="accent">

**Scratch** is per user and is **not** backed up. **Store** is per project and **is** backed up.

</div>

<!--
This is the slide of the module. Do not rush it.
SAY:
- Six mount points. Read the table, do not read it out loud.
- Three groups. Home, scratch, and project.
- Home is small. 50 gigabytes. Code and configuration, nothing else.
- Three scratch filesystems. The difference between the first two is the next slide.
- Ritom is newer, Clariden only, and its cleanup policy is still being finalised. Do not build a workflow on it yet.
- Then two project areas: the store, which is backed up, and datacache, which is not and which you have to ask for.
GIVE THEM THE MODEL FIRST. Two words, two properties:
- Scratch is yours. Per user. Not backed up.
- Store belongs to the project. Shared. Backed up.
- Everything else on this slide hangs off those two.
HOME SITS BETWEEN THEM, if anyone asks:
- No cleanup, and there are daily snapshots of the last seven days in $HOME/.snapshot.
- That has saved people who deleted their own code. Worth knowing it exists.
- Tape backups for Home are being implemented, so do not promise them yet.
THEN POINT AT THE CLEANUP COLUMN:
- This is the column that hurts people.
- Say the mechanism precisely, because it is not what they assume.
- It is not age. It is last access time.
- A file nobody has read for 14 days on iopsstor is deleted. 30 days on capstor.
- So a dataset you keep reading survives. A checkpoint you wrote and forgot does not.
- Not archived. Deleted.
- Ritom is the exception: its policy is still being finalised, so do not assume anything there yet.
NEXT: So which scratch, for what?
DOCS: docs.cscs.ch/storage/filesystems/ · docs.cscs.ch/platforms/mlp/
-->

<!-- Verified against cscs-docs-preview.svc.cscs.ch/442, both /storage/filesystems/ and
/platforms/mlp/, quoting them directly:
  home     "There is no cleanup policy on Home"; 50 GB and 500,000 inodes; daily
           snapshots of the last seven days in $HOME/.snapshot; tape backups "currently
           being implemented"; retained three months after your last project finishes.
  iopsstor "Files ... that have not been accessed in 14 days are automatically deleted."
  capstor  "Files ... that have not been accessed in 30 days are automatically deleted."
           150 TB, 1 million inodes, soft quota with a two-week grace period.
           "There are no backups on Scratch."
  store    "There is no cleanup policy on Store"; "the three most recent copies of every
           file backed up to tape every 24 hours"; quota from the initial resource
           request; retained three months after the project ends.
  ritom    cleanup "is being finalised". Nothing else stated.
Note the criterion is LAST ACCESS, not age or modification time.

TODO(verify): two things the preview does not settle.
 1. The iopsstor scratch quota is not stated anywhere. Find it, or leave it off.
 2. The preview labels ritom "(Clariden only)" and says "On Clariden, the cleanup policy
    ... is being finalised". Andrea says it is NOT mounted only on Clariden, so the slide
    drops that qualifier. This is a documentation error, not a gap — fix the page. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience all">Everyone</div>

# NVMe for reading data, HDD for writing checkpoints

The two scratch filesystems are built from different hardware. Match the workload.

<div class="cols">
<div class="card">

### `iopsstor` — NVMe

Use it for:

- Training and validation datasets read **frequently and non-sequentially**
- Workloads doing **many small, random** I/O operations

Cleaned after **14 days**.

</div>
<div class="card">

### `capstor` — HDD

Use it for:

- **Model checkpoints**
- Outputs involving **large, contiguous** I/O

Cleaned after **30 days**.

</div>
</div>

<div class="accent">

After the job: move anything you care about to project storage. Nothing on scratch survives.

</div>

<!--
SAY:
- Both are called scratch. They are different hardware and they behave differently.
- iopsstor is NVMe. It is good at IOPS. Put your dataset there, the thing you read from constantly in random order.
- capstor is spinning disks, optimised for large sequential reads and writes. Put your checkpoints there.
- Get this backwards and your training is slower for no reason at all.
READ THE RED BAR:
- And when the job finishes, move what you care about to project storage. Say it every time.
NEXT: How much have you actually used?
DOCS: docs.cscs.ch/platforms/mlp/ (Scratch Usage Recommendations)
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/guides/storage/' -->
<div class="audience all">Everyone</div>

# Inodes run out before terabytes do

A quota has two numbers, and people only remember one.

<div class="cols">
<div>

- Home is **50 GB** — and **500,000 inodes**
- One inode is roughly one file
- **One PyTorch virtual environment is about 22,800 inodes**
- So about twenty of those and Home is full, on a metric nobody was watching

</div>
<div class="card">

### The fix, and it is the same one as module 3

> "Lustre is not well suited to handling many small files."

Squash the environment into a **single squashfs image**. One file instead of twenty-two thousand.

That is exactly what a **uenv** already is.

</div>
</div>

<div class="accent">

Millions of small training files hurt the metadata servers, not just your quota.

</div>

<!--
SAY:
- A quota has two numbers and people only remember the gigabytes.
- Space, and inodes. An inode is roughly a file.
- Home gives you 50 gigabytes and five hundred thousand files.
- Now the number that surprises everyone: one PyTorch virtual environment is about
  twenty-two thousand eight hundred inodes.
- So roughly twenty environments and your home directory is full — not on size, on file count.
- The documentation is blunt about why: Lustre is not well suited to handling many small files.
- The fix is on the right, and it is the same trick module 3 will show you.
- Squash the whole environment into one squashfs image. One file, not twenty-two thousand.
- That is literally what a uenv is. Module 3 picks this up.
NEXT: Now get the data in.
DOCS: docs.cscs.ch/guides/storage/ · docs.cscs.ch/storage/filesystems/
-->

<!-- TODO(verify): the quota-checking command is in the "Checking quota" section of the
storage docs and was never captured here. Module 2 owner: quote it verbatim and put it
on this slide or say it out loud. The 22,800-inode figure and the Lustre quotation come
from cscs-docs-preview.svc.cscs.ch/442/guides/storage/. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/transfer/' -->
<div class="audience all">Everyone</div>

# Moving data in: Globus from outside, `xfer` from inside

Never move terabytes from a login node.

<div class="cols">
<div>

### From outside CSCS

The recommended route is the **CSCS Globus Online endpoint**. Authenticate with your CSCS credentials.

### Between CSCS filesystems

Submit to the **`xfer`** Slurm partition. Do not do it interactively.

```bash
#!/bin/bash -l
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --partition=xfer

command="rsync -av"
srun -n $SLURM_NTASKS $command $1 $2
```

</div>
<div class="card">

### `rclone` beats `rsync` at scale

For a directory with many files, or a few very large checkpoints, `rclone` copies in parallel.

**Many files**
`rclone copy --transfers=16 --checkers=32 --progress`

**Large files**
`rclone copy --multi-thread-streams=4 --multi-thread-cutoff=256M --transfers=4 --progress`

**1 TB in about 5 minutes** — roughly 3 GB/s.

</div>
</div>

<!--
SAY:
- Two directions, two tools.
- From outside CSCS, use Globus. It handles restarts, which matters when the transfer takes hours.
- Between CSCS filesystems, use the xfer partition. It is a Slurm partition dedicated to this.
- The point of xfer is that you are not doing it on a login node, where you would be hurting everybody else.
- On the right, the thing people do not know: rclone is often much faster than rsync, because it works in parallel.
- Two flag sets, one for many small files, one for a few big ones.
- Give them the concrete number: a one terabyte directory from store to scratch takes about five minutes. Roughly three gigabytes a second.
- Start with those values and raise the parallelism gradually, watching the effect on the metadata servers.
- If you need to chain transfers, xfer jobs take --dependency=afterok like any other Slurm job.
NEXT: What about data that has to outlive the project?
DOCS: docs.cscs.ch/storage/transfer/
-->

<!-- TODO(verify): the transfer guidance and the rclone flags come from the preview
cscs-docs-preview.svc.cscs.ch/442/storage/transfer/. Re-check once merged. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/filesystems/' -->
<div class="audience">PIs and deputies</div>

# Project storage is what you asked for in the proposal

`/capstor/store/cscs/swissai/<project>` — the only durable place, and the only backed-up one.

<div class="cols">
<div>

- Quota comes from the **initial resource request**
- Small projects: **1 TB, 1M inodes** by default
- Large projects: **no default** — you state it in the proposal
- **Backed up** to tape: three most recent copies, every 24 hours
- No cleanup policy

</div>
<div class="card">

### At the end

Contents are retained for **three months** after the project finishes.

Home is retained for three months after your **last** project finishes.

</div>
</div>

<div class="accent">

This is why the proposal asks for a data footprint. Storage is not elastic.

</div>

<!--
SAY:
- Project storage is the only place that is neither small nor temporary.
- The quota is not negotiable after the fact. It is what you asked for in the proposal.
- Small projects get a terabyte by default. Large projects get no default at all, you state it.
- It is backed up to tape, three copies, every 24 hours. Scratch is not.
- And at the end, three months, then it goes.
- That connects back to module 1: this is why we ask for a data footprint up front.
NEXT: And from today there is a second project area, which is new.
DOCS: docs.cscs.ch/storage/filesystems/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience all">Everyone</div>

<span class="tag">New — from 26 August</span>

# `datacache` is fast, shared, and does not disappear

Available from today, after the maintenance. It fills the gap between scratch and project store.

<div class="cols-wide">
<div>

| | Fast? | Survives? | Shared by the project? |
|---|---|---|---|
| Scratch `iopsstor` | **yes** | no — 14 days | no, per user |
| Project store | medium | **yes** | **yes** |
| **`datacache`** | **yes** | **yes** | **yes** |

`/iopsstor/datacache/cscs/swissai/<project>`

</div>
<div class="card">

### How to get one

It is **not** provisioned by default.

Your **PI** opens a Service Desk ticket with the use case, and the space and inodes needed. CSCS reviews it before creating the area.

</div>
</div>

<div class="accent">

Project-level like the store, but **not backed up**, like scratch. And nothing is ever deleted for you.

</div>

<!--
This is new. Nobody in the room has used it. Spend a moment.
SAY, start from the problem it solves:
- Until today you had two bad options for a dataset the whole team reads.
- Put it on scratch: fast, but it is per user, and it is deleted after 14 days.
- Put it on project store: shared and durable, but it is medium-performance, so random reads are slow.
- So teams kept a copy each, on scratch, and re-staged it every two weeks.
- datacache is the third option. Fast NVMe, shared across the project, and never cleaned automatically.
- One copy of the dataset. The whole project reads it. It is still there next month.
POINT AT THE RED BAR:
- Place it against the model from two slides ago. Scratch is yours and not backed up. Store is the project's and is backed up.
- datacache is the odd one: it belongs to the project, like the store, but it is not backed up, like scratch.
- And unlike both, nothing is ever deleted for you.
- Within your quota on capacity and inodes, the project owns its own space hygiene. That is a real responsibility.
HOW TO GET IT:
- It is not created by default. Your PI opens a Service Desk ticket saying what it is for and how much space and how many inodes.
- We review it before creating the area.
NEXT: Where to read more.
DOCS: docs.cscs.ch/platforms/mlp/
-->

<!-- TODO(verify): datacache is documented only on the preview at
cscs-docs-preview.svc.cscs.ch/442/platforms/mlp/ and goes live on 26 August after the
maintenance. Confirm on the morning of the session that it is actually available — if
the maintenance slips, this slide says "from today" and would be wrong on stage.
Re-point the DOCS line once the page is merged. -->

---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Storage

- **Overview** — docs.cscs.ch/storage/
- **File systems and quotas** — docs.cscs.ch/storage/filesystems/
- **Data transfer** — docs.cscs.ch/storage/transfer/
- **Storage guide** — docs.cscs.ch/guides/storage/
- **Long term storage** — docs.cscs.ch/storage/longterm/
- **Object storage** — docs.cscs.ch/storage/object/

### Platform specifics

- **ML Platform storage, incl. `datacache`** — docs.cscs.ch/platforms/mlp/

</div>
<div class="card dark">

### The three rules

- **Home** is for code. 50 GB, 500k inodes.
- **Scratch** is yours. Not backed up. Cleaned after 14 or 30 days.
- **Project** areas are shared. Store is backed up, `datacache` is not.

### And one habit

After every job, move the results off scratch.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Three rules. Home is for code. Scratch is yours and gets cleaned. The project areas are shared and do not.
- Of the two project areas, only the store is backed up.
- And the habit: after every job, move results off scratch.
NEXT: hand over to module 3. Ben knows where his data goes. Now he needs software that can read it.
-->
