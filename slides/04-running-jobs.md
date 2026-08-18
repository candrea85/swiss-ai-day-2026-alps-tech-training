---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!--
DRAFT — owner TBD. Scaffolding. Budget: 12 minutes.

Note for the module 4 owner: there is ready-made material for the HPC Console part in
the CUG 2026 deck "A Lightweight Web-UI for HPC and AI" (Pagnamenta, Ceriani, Palme,
Dorsch) — 20 slides with speaker notes and screenshots, already cleared for an external
audience. See notes/sources.md. A 5-slide version is drafted in slides/06-backup.md.
-->

<!-- _class: divider -->

<span class="tag">Module 4 · 12 min</span>

# Running and automating

Data in the right place, an environment that works. Now make it run — repeatedly, at scale.

<!--
START AT T+45:00. Check the presenter timer now.
CUT IF LATE: Cut "You are billed for the node, not for the work". Say it in one line over the GH200 slide instead.
SAY:
- Ben has his data and his container. Now he has to actually run.
- Three things in twelve minutes: Slurm, whether your job is efficient, and the web ways in.
NEXT: Slurm, and the one flag that decides who pays.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/running/slurm/' -->
<div class="audience all">Everyone</div>

# Every job is charged to a project

`--account` is not optional. It is how the GPU hours from module 1 get spent.

```bash
#!/bin/bash
#SBATCH --account=a-csstaff
#SBATCH --job-name=example-%j
#SBATCH --time=00:30:00
#SBATCH --nodes=4

srun --environment=my-pytorch python train.py
```

<div class="cols">
<div>

| Partition | Max nodes | Time limit |
|---|---|---|
| `debug` | 2 | 30:00 |
| `normal` | unlimited | 1-00:00:00 |
| `xfer` | 1 | 1-00:00:00 |

</div>
<div class="card">

### The link back to module 1

This is the line that draws down the credit. The **grace** and the **minimal** from module 1 are counted from these jobs.

</div>
</div>

<!--
SAY:
- One script. It is short on purpose.
- The account flag is how Slurm knows which project pays. It is not optional.
- This is the line that connects to module 1: every job here draws down the credit Anna was granted.
- Three partitions. Debug for quick turnaround, two nodes, thirty minutes. Normal for real work. Xfer for data, which module 2 covered.
- And the srun line carries the environment flag from module 3. That is the whole stack in one script.
NEXT: How to ask for GH200 nodes properly.
DOCS: docs.cscs.ch/running/slurm/
-->

<!-- TODO(verify): --account=a-csstaff is a placeholder. Module 4 owner: replace with a
realistic Swiss AI project account string, and confirm the partition table against
docs.cscs.ch/running/slurm/ for the ML Platform specifically — the partitions listed
there may differ per cluster. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/running/slurm/' -->
<div class="audience all">Everyone</div>

# A GH200 node is four GPUs and four sockets

Ask for it the way the hardware is built.

<div class="cols">
<div>

```bash
#SBATCH --ntasks-per-node=4
#SBATCH --gpus-per-task=1
```

One task per GPU. This is the shape almost every ML job wants.

For multiple job steps on one node:

```bash
#SBATCH --exclusive --mem=450G
```

</div>
<div class="card">

### Why this matters

Ask for the wrong shape and you get one process driving four GPUs badly, or four processes fighting over one.

Neither shows up as an error. Both show up as a bill.

</div>
</div>

<!--
SAY:
- A Grace-Hopper node is four GPUs and four CPU sockets. Ask for it that way.
- Four tasks per node, one GPU per task. That is the shape nearly every ML job wants.
- If you are running several job steps on the same node, take it exclusive.
- The reason to care is on the right: getting this wrong is not an error message. It is a slow job that still costs you the full node hours.
NEXT: Which brings us to efficiency.
DOCS: docs.cscs.ch/running/slurm/
-->

---
<div class="audience">PIs and deputies</div>

# You are billed for the node, not for the work

<!-- PLACEHOLDER — module 4 owner: this needs a real efficiency example or a tool name. -->

<div class="cols">
<div>

- A node reserved is a node **charged**, busy or idle
- 30% GPU utilisation means **70% of your credit** bought nothing
- Efficiency was a question in the proposal (module 1). It is the same question here
- Measure one run before scaling to a hundred

</div>
<div class="card">

### For the PIs

This is the other half of "check the consumption monthly".

Burning the budget on schedule and getting nothing out of it is **worse** than under-consuming.

</div>
</div>

<!--
SAY, and this one is aimed at the PIs:
- You are billed for the node you reserved, not for the work you did on it.
- If your GPUs sit at thirty per cent, seventy per cent of that credit bought nothing.
- Remember module 1 asked you for an expected efficiency in the proposal. This is where that promise is kept or not.
- The habit that fixes it: measure one run properly before you scale it to a hundred.
POINT AT THE CARD:
- And for the PIs specifically. Spending the budget on schedule while achieving nothing is worse than under-spending, because it is invisible.
NEXT: You do not have to do all of this from a terminal.
-->

<!-- TODO(verify): docs.cscs.ch/running/slurm/ does not document a job-efficiency tool.
Module 4 owner: name the tool you actually recommend (seff, a Grafana dashboard, the HPC
Console job view) and put a real number on this slide, or cut it to a spoken line. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/jupyterlab/' -->
<div class="audience all">Everyone</div>

# JupyterLab: a notebook on a compute node

`jupyter-clariden.cscs.ch` — you pick the nodes, the time, the project and the environment.

<div class="cols-narrow">
<div>

- One URL per cluster: **`jupyter-clariden.cscs.ch`**
- The spawner form asks for node type and count, wall time, **project account**, and **uenv or container image**
- It is a Slurm job. It is charged like one
- Startup should be under a few minutes

</div>
<div class="shot">

**SCREENSHOT**

The JupyterHub spawner options form on `jupyter-clariden.cscs.ch`, with the environment
and account fields visible.

</div>
</div>

<!--
SAY:
- If you would rather not think about sbatch, this is the way in.
- One URL per cluster. Clariden is jupyter dash clariden dot cscs dot ch.
- You get a form. Node type, how many, wall time, which project pays, and which environment — the same uenv or container from module 3.
- Two things people get wrong. It is a real Slurm job, so it is charged like one. And "disk I/O error" when saving a notebook almost always means you are out of quota, not that Jupyter is broken.
NEXT: And for automation, there is an API.
DOCS: docs.cscs.ch/access/jupyterlab/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/firecrest/' -->
<div class="audience all">Everyone</div>

# FirecREST: the cluster as an HTTP API

For CI pipelines, workflow engines and anything that cannot hold an SSH key.

<div class="cols">
<div>

**ML Platform endpoint**

`api.cscs.ch/ml/firecrest/v2`

Lets you do, over HTTP:

- filesystem operations — `ls`, `mkdir`, `mv`, `chmod`
- Slurm — submit, query, cancel
- data transfers, internal and external

</div>
<div class="card">

### How it authenticates

A client ID and secret, exchanged for a short-lived **JWT access token**, valid **5 minutes**.

No user password. This is what a service account is for — see module 1.

</div>
</div>

<div class="accent">

And there is a web interface on top of it: **`console.mlp.cscs.ch`**

</div>

<!--
SAY:
- FirecREST turns the cluster into a REST API.
- One endpoint per platform. Yours is the ml one.
- Over HTTP you can list files, make directories, submit and cancel Slurm jobs, and move data.
- Authentication is a client ID and secret exchanged for a token that lives five minutes. No passwords in scripts.
- This is exactly what the service accounts from module 1 are for.
POINT AT THE RED BAR:
- And you do not have to write the HTTP yourself. There is a web console on top, console dot mlp dot cscs dot ch.
- We have backup slides on it if the discussion wants them.
NEXT: Where to read more.
DOCS: docs.cscs.ch/access/firecrest/ · eth-cscs.github.io/firecrest-v2/
-->

---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Running

- **Running jobs** — docs.cscs.ch/running/
- **Slurm** — docs.cscs.ch/running/slurm/

### Other ways in

- **JupyterLab** — docs.cscs.ch/access/jupyterlab/
- **FirecREST** — docs.cscs.ch/access/firecrest/
- **FirecREST v2** — eth-cscs.github.io/firecrest-v2/

### Worked examples

- **ML tutorials** — docs.cscs.ch/tutorials/ml/

</div>
<div class="card dark">

### Three ways in, same cluster

- `ssh` — full control
- `jupyter-clariden.cscs.ch` — a notebook
- `console.mlp.cscs.ch` — a browser

### One flag that matters

`--account` — it decides who pays.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Three doors into the same cluster. SSH, Jupyter, the console. Pick whichever fits the task.
- And one flag: account. It decides who pays.
NEXT: hand over to module 5.
-->
