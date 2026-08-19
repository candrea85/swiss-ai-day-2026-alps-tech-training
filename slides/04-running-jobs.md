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
- Four things in twelve minutes: Slurm, whether your job is efficient, the two ways in through a browser, and the inference API.
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

# The HPC Console: the cluster in a browser

`console.mlp.cscs.ch` — nothing to install, and it needs no agent on the cluster.

<div class="cols">
<div>

- **Dashboard** — cluster health. It will stop you submitting to a degraded cluster
- **Jobs** — list, filter, submit, and inspect logs
- Every job has a **shareable URL**: send a colleague the failing job, not a screenshot
- **Files** — browse, preview, upload

</div>
<div class="card">

### The same API underneath

It runs on **FirecREST**, so anything the console does, your own script can do:

`api.cscs.ch/ml/firecrest/v2`

Client ID and secret, exchanged for a 5-minute token. No passwords in CI — this is what a **service account** is for.

</div>
</div>

<div class="accent">

Same login as everything else. Longer version in the backup slides, if you want it.

</div>

<!--
SAY:
- Third way in, and the one fewest of you will have seen.
- A browser pointed at the cluster. Nothing to install, and no agent running as you on the cluster.
- The dashboard shows cluster health, and it will refuse to submit to a degraded cluster. That alone saves a failed overnight run.
- Jobs: list, filter, submit, read the logs.
- The feature I would highlight is the shareable per-job URL. It replaces the screenshot-in-Slack workflow that most debugging conversations start with.
POINT AT THE CARD:
- It runs on FirecREST, and that is the useful part: anything the console can do, your script can do, because it is the same API.
- Client ID and secret for five-minute tokens. No passwords in a pipeline. That is what the service accounts from module 1 are for.
- We have five more slides on this in backup if the discussion wants them.
NEXT: One last thing, and it does not involve a cluster at all.
DOCS: docs.cscs.ch/access/firecrest/ · eth-cscs.github.io/firecrest-v2/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/services/inference/api/' -->
<div class="audience all">Everyone</div>

# You can use a model without training one

`https://api.inference.cscs.ch/v1` — **OpenAI and Anthropic compatible**. Change a base URL and your existing code works.

<div class="cols-wide">
<div>

- Open-weight models, served and managed for you — **Apertus 70B** and **8B**, among others
- **The PI or deputy PI** creates the inference resource in `portal.cscs.ch`
- Then **any project member** can create API keys
- **Set a token budget on every key** — plus a reset period and the allowed models. Today it is the only limit there is

</div>
<div class="card">

### It is not free, it is yours

> "The credit for the inference resource is taken from your project's credit."

The same credit as module 1. Inference spends it, like any job.

</div>
</div>

<div class="accent">

The docs also show how to point **Claude Code** and **OpenCode** at it.

</div>

<!--
This one is for a Swiss AI room specifically. Do not rush it.
SAY:
- Last thing, and it does not involve a cluster, a container or Slurm at all.
- There is a managed inference API. Open-weight models, served for you, behind a public endpoint.
- It is OpenAI and Anthropic compatible, so whatever you already wrote works if you change the base URL.
- And it serves Apertus, which is your own model.
- Many of you want to use a model rather than train one. This is that, and until today we were not telling you about it.
HOW YOU GET IT, and note the split:
- The PI or the deputy PI creates an inference resource in the portal. The same portal as module 1.
- After that, any member of the project can create their own API keys.
- And this is the part to dwell on if you are a PI.
- Each key can carry its own token budget, a period after which that budget resets, and a list of allowed models.
- An API key is a spending instrument, because the credit comes out of the project.
- The key is shown once when it is created. Put it in a password manager.
THE HONEST VERSION. Decide in the room how far you go:
- Today there is NO project-level cap on how much of the credit inference can consume.
- So if no key has a budget, a single key can spend the entire project credit.
- Aim it at the PIs as an instruction — "put a budget on every key" — rather than as an
  announcement that the guardrail is missing. Same fact, but one lands as an action.
- If a PI asks you directly whether there is a cap, answer directly. Do not imply there
  is one.
BE HONEST ABOUT THE COST. Read the quotation out loud:
- The credit comes out of the project credit. It is not a free extra.
- So it lands on the same budget as the linear consumption slide in module 1.
POINT AT THE RED BAR:
- And the documentation shows how to wire it into Claude Code and OpenCode, if that is how you work.
NEXT: Where to read more.
DOCS: docs.cscs.ch/services/inference/api/
-->

<!-- TODO(verify): model names and pricing move. Re-check the model list and the
"Available models and pricing" section the week before the session, and confirm the
Apertus tag swiss-ai/Apertus-70B-Instruct-2509 is still current if you quote it. -->

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
- **HPC Console and FirecREST** — docs.cscs.ch/access/firecrest/
- **FirecREST v2** — eth-cscs.github.io/firecrest-v2/

### Inference

- **LLM Inference API** — docs.cscs.ch/services/inference/api/

### Worked examples

- **ML tutorials** — docs.cscs.ch/tutorials/ml/

</div>
<div class="card dark">

### Four ways in

- `ssh` — full control
- `jupyter-clariden.cscs.ch` — a notebook
- `console.mlp.cscs.ch` — a browser
- `api.inference.cscs.ch` — no cluster at all

### One thing they share

They all spend the **same project credit**.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Four ways in. SSH, Jupyter, the console, and the inference API. Pick whichever fits the task.
- And the thing they have in common: they all spend the same project credit.
NEXT: hand over to module 5.
-->
