---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!--
BACKUP SLIDES. These sit after the wrap-up and are NOT part of the 60-minute budget.
They are shown only if the open discussion asks for them.

The HPC Console block below is the ~5 minute section Andrea asked for. It is drafted here
rather than inside module 4 so that the placement decision stays open: it can be moved
into slides/04-running-jobs.md, promoted to a section of its own, or left here as
backup. Moving it costs nothing — cut the block and paste it.

Source: the CUG 2026 paper and deck "A Lightweight Web-UI for HPC and AI" (Pagnamenta,
Ceriani, Palme, Dorsch, 29 April 2026), plus docs.cscs.ch/access/firecrest/.
See notes/sources.md.
-->

<!-- _class: divider -->

<span class="tag">Backup · shown on request</span>

# Backup slides

Kubernetes · post-training · multi-node scaling · GPU efficiency · the HPC Console

<!--
Only put this up if somebody asks. Then jump straight to the block they asked for.
-->

---
<!-- _class: divider -->

<span class="tag">Backup · ~5 min</span>

# The HPC Console

A browser interface to the cluster, built on FirecREST. Open source as `firecrest-ui`.

<!--
SAY:
- Five minutes on the HPC Console, since you asked.
- Short version: it is a web interface to the cluster. It does not replace SSH. It complements it.
NEXT: Why it exists.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/firecrest/' -->
<div class="audience all">Everyone</div>

# Not everything needs a terminal

HPC systems are powerful, but not always easily accessible.

<div class="cols">
<div>

- Most access is through **command-line tools** like SSH
- They give flexibility and full control, and they are essential for automation
- They are **not equally usable by everyone**
- Entry-level users face a steep learning curve, even for simple tasks
- Checking system status, finding a job, reading a log: none of it needs full shell expertise

</div>
<div class="card">

### The goal

**Not** to replace SSH.

To provide a complementary tool that simplifies the common operations, and to let AI and ML users get at HPC resources without a week of Slurm first.

</div>
</div>

<!--
SAY:
- The honest framing first, because this room contains people who love their terminal.
- The goal is not to replace SSH. SSH stays, and for automation it is still the right answer.
- But a lot of daily operations do not need a shell. Is the cluster healthy. What is my job doing. Why did it fail.
- Those are the things people currently do with three tools and six commands.
NEXT: What it is built on.
DOCS: docs.cscs.ch/access/firecrest/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/firecrest/' -->
<div class="audience all">Everyone</div>

# Built on FirecREST, so it needs nothing on the cluster

`console.mlp.cscs.ch`

<div class="cols">
<div>

### Design principles

- **API-first**, on top of FirecREST
- **Single sign-on** — the same login as everything else
- **No privileged agents** on the HPC systems
- Authentication and session handling stay in the **backend**, never in the browser
- Works across different clusters and schedulers

</div>
<div class="card">

### Why that matters to you

Nothing to install. Nothing running as you on the cluster.

It is the same FirecREST API from module 4 — anything the console does, your own script can do too.

</div>
</div>

<!--
SAY:
- It is built on the FirecREST API we saw in module 4. That has two consequences worth stating.
- One, there is no privileged agent running on the cluster. The console has no special powers.
- Two, and this is the useful part: anything the console can do, your own script can do, because it is the same API.
- Single sign-on, so it is the same login as the portal and Jupyter.
NEXT: What you can actually do with it.
DOCS: docs.cscs.ch/access/firecrest/
-->

---
<div class="audience all">Everyone</div>

# Four things it does well

<div class="cols">
<div>

### Dashboard

Real-time **cluster health**. Spot a degraded service *before* you submit — the system can prevent execution on unhealthy clusters.

### Scheduler

List and filter your jobs, or all jobs on the account. Submit and configure new ones.

</div>
<div>

### Monitoring

Inspect job scripts, logs and status. Each job has a **shareable URL** — send a colleague the failing job, not a screenshot.

### Filesystem

Browse, manage and preview files. Large uploads.

</div>
</div>

<div class="accent">

The shareable per-job URL is the feature people keep. External dashboards such as Grafana can be integrated.

</div>

<!--
SAY:
- Four workflows.
- The dashboard shows cluster health in real time, and it will stop you submitting to a degraded cluster. That alone saves a failed overnight run.
- The scheduler view lists your jobs, or everything on the account, with filters.
- Monitoring: job script, logs, status. And the thing I would highlight — every job has its own URL you can send to someone.
- That replaces the screenshot-in-Slack workflow, which is how most debugging conversations start today.
- And a filesystem browser with preview and large upload.
NEXT: Where to find it.
-->

<!-- PLACEHOLDER: the CUG deck has approved screenshots of all four views. Whoever
presents this should pull two of them in — the dashboard and the job detail with the
shareable URL — rather than showing this as a bullet list. -->

---
<!-- _class: ref -->

# The HPC Console — where to read more

<div class="cols">
<div>

### Use it

- **ML Platform console** — console.mlp.cscs.ch
- HPC Platform — console.hpcp.cscs.ch
- C&W Platform — console.cwp.cscs.ch

### Underneath

- **FirecREST** — docs.cscs.ch/access/firecrest/
- **FirecREST v2** — eth-cscs.github.io/firecrest-v2/

</div>
<div class="card dark">

### The one-line version

It is a browser you can point at the cluster, it needs nothing installed, and it is the same API your scripts can call.

Open source as **`firecrest-ui`**.

</div>
</div>

<!--
SAY:
- One URL per platform. Yours is console dot mlp.
- It is open source as firecrest-ui, so if your institution wants its own, that is possible.
NEXT: back to the discussion.
-->

---
<!-- _class: divider -->

<span class="tag">Backup</span>

# Still to write

Kubernetes · post-training and RLHF · advanced multi-node scaling · GPU efficiency in depth

<!--
PLACEHOLDER. These four were listed in CLAUDE.md as backup topics but have no slides yet.
If the discussion asks for one and there is nothing to show, say so plainly and offer to
follow up by email or at the User Day on Friday. Do not improvise a technical answer at
the whiteboard in front of this audience.
-->
