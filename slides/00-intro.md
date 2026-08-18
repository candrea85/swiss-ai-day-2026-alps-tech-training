---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!--
DRAFT — owner TBD. Written by Andrea's session as scaffolding so module 0 does not start
from a blank page. Everything here is traceable to docs.cscs.ch, but the module owner
should rewrite the voice and cut whatever they do not want to say. Budget: 5 minutes.
-->

<!-- _class: divider -->

<span class="tag">Module 0 · 5 min</span>

# Alps, the ML Platform, and the next hour

Where your project runs, and what we are about to walk through.

<!--
START AT T+00:00. Check the presenter timer now.
CUT IF LATE: Cut the Alps/vClusters slide. Say it in one sentence over the two-cluster slide.
SAY:
- Welcome. This is the Alps technical training.
- One hour of presentation, then thirty minutes of open discussion.
- We are five people from CSCS. Each of us takes one part.
- We are not going to teach you everything. There is not time.
- We are going to build you a map, so you know where to look next.
NEXT: First, what is the machine you are all using?
-->

---
<div class="audience all">Everyone</div>

# Today is a maintenance day

Expect limitations. Nothing in this hour depends on the machine being up.

<div class="cols">
<div>

- Systems may be **unavailable or degraded** today
- If you try to log in during the session, it may not work
- That is expected. It is **not** your SSH key

</div>
<div class="card">

### So we planned around it

Everything you will see is a **screenshot or a recording**. There are no live demos.

Ask your question anyway — we will answer it, and show you for real afterwards.

</div>
</div>

<div class="accent">

Try the commands tomorrow, not now. They are all on the handout.

</div>

<!--
Housekeeping, twenty seconds, then move on.
SAY:
- One practical thing before we start.
- Today is a maintenance day. Systems may be down or degraded.
- So if you try to log in during this hour and it does not work, that is expected. It is not your key and it is not you.
- We planned for it. Everything you will see is a screenshot or a recording. No live demos.
- That was going to be true anyway. Conference wifi and MFA on stage are a bad combination.
- Ask your questions as they come. We will answer, and we can show you for real afterwards or at the User Day on Friday.
- One upside worth mentioning: this maintenance is what delivers the new datacache storage area. Module 2 will show you what it is for.
NEXT: So, what is the machine you are all using?
-->

<!-- TODO(verify): confirm the exact maintenance window and which services are affected
before the session — the clusters, the portal, JupyterLab and the docs may not all be
down at the same time, or at all. If only some are affected, name them here rather than
saying "systems". If the maintenance moves, this slide comes out. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/alps/' -->
<div class="audience all">Everyone</div>

# Alps is one machine with many faces

You do not get "an Alps account". You get a project on a **platform**.

<div class="cols">
<div>

### The infrastructure

**Alps** is a general-purpose compute and data research infrastructure, open to researchers in Switzerland and beyond.

It is **multi-tenant**: it creates versatile clusters, **vClusters**, tailored to different communities.

</div>
<div class="card">

### Three platforms

- **Machine Learning Platform** — you are here
- HPC Platform
- Climate and Weather Platform

Each has its own clusters, its own software stack and its own policies.

</div>
</div>

<div class="accent">

Everything in this hour is the **ML Platform**. Other platforms do some of it differently.

</div>

<!--
SAY:
- Alps is the research infrastructure. One physical machine, many logical clusters.
- Those logical clusters are called vClusters. They are tailored per community.
- On top of them CSCS runs three platforms. You are on the Machine Learning Platform.
- This matters for one reason: when you search the documentation, the answer often depends on the platform.
- Everything we say today is the ML Platform. If you read a page about the HPC Platform, some of it will not apply to you.
NEXT: So what is on the ML Platform?
DOCS: docs.cscs.ch/alps/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience all">Everyone</div>

# Two clusters, and they are not interchangeable

The ML Platform provides compute, storage and expertise to the machine learning communities on Alps.

<div class="cols">
<div class="card">

### Clariden

**Grace-Hopper GH200.** The main system.

This is where **production runs** go.

</div>
<div class="card">

### Bristen

**A100 nodes.** Smaller.

Data processing, development and x86 workloads. **Test and development**, best effort.

</div>
</div>

<div class="accent">

"It is **not** a cluster where to do the bulk of your computation." — the Bristen documentation, about Bristen.

</div>

<!--
SAY:
- The ML Platform gives you compute, storage and expertise.
- Two clusters, and people mix them up.
- Clariden is Grace-Hopper, GH200. It is the main system. Production runs go here.
- Bristen is A100, smaller. Data processing, development, x86 work.
- Bristen is best effort. Read the red bar out loud, it is the docs talking about themselves.
NEXT: Here is what we are going to cover in the next hour.
DOCS: docs.cscs.ch/platforms/mlp/ · /clusters/clariden/ · /clusters/bristen/
-->

---
<div class="audience all">Everyone</div>

# One project, from nothing to a trained model

We follow **Anna**, a PI, and **Ben**, a PhD student who joins her project.

<div class="cols">
<div>

| | | |
|---|---|---|
| **1** | Project and access | 12 min |
| **2** | Data and storage | 13 min |
| **3** | Software and containers | 15 min |
| **4** | Running and automating | 12 min |
| **5** | Wrap-up | 3 min |
| | **Open discussion** | **30 min** |

</div>
<div class="card">

### How to follow this

Each slide says in the top right corner who it is for — **PIs and deputies**, or **Everyone**.

Every module ends with **where to read more**.

There is a **handout**. Every command is on it.

</div>
</div>

<!--
SAY:
- The hour is one story. One project, from "we need compute" to "the model is trained and being served".
- Two people carry it. Anna is a PI who has just been granted a project. Ben is a PhD student who joins her.
- Five modules. Here are the times, so you know when your part is coming.
- Then thirty minutes of open discussion, which is honestly the part we want most.
- Two practical things. Every slide says in the corner who it is for. And there is a handout with every command, so do not type.
NEXT: Module 1. How do you get a project at all?
-->

---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Start here

- **Alps** — docs.cscs.ch/alps/
- **Machine Learning Platform** — docs.cscs.ch/platforms/mlp/
- **Clariden** — docs.cscs.ch/clusters/clariden/
- **Bristen** — docs.cscs.ch/clusters/bristen/

</div>
<div class="card dark">

### If you remember one thing

`docs.cscs.ch` is the answer to almost every question in this hour.

The deck is a **signpost**. The documentation is the destination.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Four links. They are all on docs.cscs.ch.
- This deck is a signpost, not a manual.
NEXT: hand over to module 1.
-->
