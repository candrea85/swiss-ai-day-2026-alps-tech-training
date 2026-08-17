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
CUT IF LATE: Cut "Beyond the project". Long term and object storage become one spoken line.
SAY:
- Ben is in. He has a shell on Clariden and an empty home directory.
- His first real question is where to put his data.
- Getting this wrong is the most expensive mistake on this platform.
- Wrong filesystem means slow training. Or deleted data.
NEXT: There are four places, and they are not interchangeable.
-->

---

<div class="audience all">Everyone</div>

# Four filesystems, four different jobs

Putting data in the wrong one is the most common and most expensive mistake here.

| | Path | For | Quota | Cleanup |
|---|---|---|---|---|
| **Home** | `/users/$USER` | code, scripts, config | **50 GB**, 500k inodes | none |
| **Scratch** `iopsstor` | `/iopsstor/scratch/cscs/$USER` | training data, random I/O | — | **14 days** |
| **Scratch** `capstor` | `/capstor/scratch/cscs/$USER` | checkpoints, large sequential I/O | 150 TB, 1M inodes | **30 days** |
| **Project store** | `/capstor/store/cscs/swissai/<project>` | shared, medium term | per project | none |

<div class="accent">

Scratch is **not** storage. It is a workspace that deletes itself.

</div>

<!--
This is the slide of the module. Do not rush it.
SAY:
- Four places. Read the table left to right, do not read it out.
- Home is small. 50 gigabytes. It is for code and configuration, nothing else.
- Two scratch filesystems, and the difference between them is the next slide.
- Project store is where things live for the length of the project.
POINT AT THE CLEANUP COLUMN:
- This is the column that hurts people.
- Files not accessed for 14 days on iopsstor are deleted. 30 days on capstor.
- Not archived. Deleted. There are no backups on scratch.
READ THE RED BAR:
- Scratch is not storage. It is a workspace that deletes itself.
NEXT: So which scratch, for what?
DOCS: docs.cscs.ch/storage/filesystems/ · docs.cscs.ch/platforms/mlp/
-->

<!-- TODO(verify): quotas and cleanup windows come from the storage documentation that is
still a preview at cscs-docs-preview.svc.cscs.ch/442/storage/filesystems/ and from
docs.cscs.ch/platforms/mlp/. The iopsstor quota is not stated on either — find it or
drop the column entry. Re-check every number once the preview is merged. -->

---

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

<div class="audience all">Everyone</div>

# Inodes run out before terabytes do

<!-- PLACEHOLDER — module 2 owner: this slide needs your real numbers and a real example. -->

<div class="cols-narrow">
<div>

- Home is **50 GB** but also **500,000 inodes**
- One inode is roughly one file
- A dataset of a million small files fails on **count**, not on size
- Check before you fill it, not after

</div>
<div class="shot">

**SCREENSHOT / TERMINAL CAPTURE**

The quota-checking command and its output.
See `docs.cscs.ch/storage/filesystems/` → "Checking quota".

</div>
</div>

<!--
SAY:
- A quota has two numbers, and people only remember one.
- Space, and inodes. An inode is roughly a file.
- Home gives you 50 gigabytes and 500,000 files.
- If your dataset is a million tiny images, you hit the file limit long before the size limit.
- That is also an argument for packed dataset formats, but that is module 3's problem.
NEXT: Now get the data in.
DOCS: docs.cscs.ch/storage/filesystems/
-->

<!-- TODO(verify): the exact quota-checking command is in the "Checking quota" section of
the storage docs and was not captured here. Module 2 owner: quote it verbatim, and
replace the placeholder with a real terminal capture. -->

---

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
`rclone copy --multi-thread-streams=4 --multi-thread-cutoff=256M --transfers=4`

Roughly **3 GB/s** in practice.

</div>
</div>

<!--
SAY:
- Two directions, two tools.
- From outside CSCS, use Globus. It handles restarts, which matters when the transfer takes hours.
- Between CSCS filesystems, use the xfer partition. It is a Slurm partition dedicated to this.
- The point of xfer is that you are not doing it on a login node, where you would be hurting everybody else.
- On the right, the thing people do not know: rclone is often much faster than rsync, because it works in parallel.
- Two flag sets, one for many small files, one for a few big ones. About three gigabytes per second.
NEXT: What about data that has to outlive the project?
DOCS: docs.cscs.ch/storage/transfer/
-->

<!-- TODO(verify): the transfer guidance and the rclone flags come from the preview
cscs-docs-preview.svc.cscs.ch/442/storage/transfer/. Re-check once merged. -->

---

<div class="audience">PIs and deputies</div>

# Project storage is what you asked for in the proposal

<!-- PLACEHOLDER — module 2 owner: this is the PI-facing storage slide. Expand or cut. -->

<div class="cols">
<div>

- Path: `/capstor/store/cscs/swissai/<project>`
- Quota comes from the **initial resource request**
- Small projects: **1 TB, 1M inodes** by default
- Large projects: **no default** — you state it in the proposal
- Backed up to tape; three most recent copies, every 24 hours
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
- That last point connects back to module 1: this is why we ask for a data footprint up front.
NEXT: Long term, and then where to read more.
DOCS: docs.cscs.ch/storage/filesystems/
-->

---

<div class="audience all">Everyone</div>

# Beyond the project: long term storage and object storage

<!-- PLACEHOLDER — module 2 owner: one line each, or cut this slide if short on time. -->

<div class="cols">
<div class="card">

### Long Term Storage

Preserve scientific data and make it publicly accessible through a **persistent identifier**.

For data that has to outlive the project and be cited.

</div>
<div class="card">

### Object Storage

A public cloud object storage service, based on the **Ceph Object Gateway**.

For data that has to be reachable over HTTP.

</div>
</div>

<!--
SAY:
- Two services that are not filesystems, mentioned so you know they exist.
- Long Term Storage is for data that must outlive the project and be citable. It gives you a persistent identifier.
- Object storage is Ceph behind an S3-style gateway, for data you need to reach over HTTP.
- Neither is something you set up in the last week of a project. Plan them.
NEXT: Where to read more.
DOCS: docs.cscs.ch/storage/longterm/ · docs.cscs.ch/storage/object/
-->

---

<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Storage

- **Overview** — docs.cscs.ch/storage/
- **File systems and quotas** — docs.cscs.ch/storage/filesystems/
- **Data transfer** — docs.cscs.ch/storage/transfer/
- **Long term storage** — docs.cscs.ch/storage/longterm/
- **Object storage** — docs.cscs.ch/storage/object/

### Platform specifics

- **ML Platform storage policies** — docs.cscs.ch/platforms/mlp/

</div>
<div class="card dark">

### The three rules

- **Home** is for code. 50 GB.
- **Scratch** deletes itself. 14 or 30 days.
- **Project store** is the only durable place.

### And one habit

After every job, move the results off scratch.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Three rules. Home is for code. Scratch deletes itself. Project store is the durable one.
- And the habit: after every job, move results off scratch.
NEXT: hand over to module 3. Ben knows where his data goes. Now he needs software that can read it.
-->
