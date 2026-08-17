---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 1 · 12 min</span>

# Project lifecycle and access

Anna gets a project. Anna adds Ben. Ben logs in. Both watch the budget.

<div class="split">

**First half — PIs and deputies.** Getting a project, the team, the budget.
**Second half — everyone.** Account, MFA, keys, logging in.

</div>

<!--
START AT T+05:00. Check the presenter timer now.
CUT IF LATE: Cut "What this module deliberately skipped". Say those five lines over the hand-off.
SAY:
- This module is 12 minutes. It is the plumbing part.
- The interesting part of the hour is modules 2 to 4.
TELL THEM WHEN TO PAY ATTENTION. This is the point of this slide:
- The first half is for PIs and deputy PIs. Getting a project, adding people, watching the budget.
- The second half is for everybody who has to log in. Account, MFA, keys, the jump host.
- Each slide says in the top right corner which one it is.
- So if the first half is not your job, you have four minutes to read your email. I will not be offended.
THEN:
- Every command I show is on the handout. So do not type. Just watch.
- Meet Anna. She is a PI with a new project.
- And Ben. He is a PhD student who joins her project.
NEXT: Start at the beginning. How do you get a project at all?
-->

---

<div class="audience">PIs and deputies</div>

# Small and large are two different processes

You choose which one to apply for. The Swiss AI Initiative decides. CSCS opens the project and runs it.

<div class="cols-wide">
<div>

|  | Small | Large |
|---|---|---|
| Typical budget | up to 32,000 GPUh | 500,000 GPUh and up |
| Duration | 6 months | 12 months |
| Review | rolling | two calls a year |
| Start | first day of the next month | 1 January or 1 July |
| Storage | 1 TB, 1M inodes by default | must be in the proposal |

</div>
<div class="card">

### Before asking for a large one

- A GPU-hour number you **measured**
- The efficiency you expect to reach
- The **data footprint**, and how long it stays

A large proposal can be **cut down to a small grant** rather than rejected.

</div>
</div>

<div class="accent">

The 4th call for large projects is open right now — **3 August to 14 September 2026**. `swiss-ai.org/compute-grants`

</div>

<!--
SAY FIRST, who does what. People ask us for hours and we cannot give them:
- You decide whether to apply for a small or a large project. That choice is yours.
- You apply to the Swiss AI Initiative, not to us. They decide.
- Swiss AI tells us to open the small ones as they are approved, all year round.
- And twice a year they hand us the large ones, together.
- CSCS opens the project and runs it. We do not decide who gets what.
THEN THE TWO KINDS:
- People often apply to the wrong one.
- Small: up to 32,000 GPU hours. Six months. Reviewed all year.
- So you can ask today and start on the first day of next month.
- Large: 500,000 GPU hours and more. Twelve months.
- It starts only on 1 January or 1 July. If you miss a call, you wait six months.
- The storage row is the one people forget.
- Small gets 1 terabyte by default. Large gets no default. You must ask for it in the proposal.
- Bring three things to a large proposal: GPU hours you measured, the efficiency you expect, and your data footprint.
- Good news: a weak large proposal is usually made smaller. It is not simply rejected.
POINT AT THE RED BAR:
- The 4th large call closes on 14 September. That is about three weeks from today.
- If you want a large project in January, this is your call.
NEXT: Say Anna applied and was granted a project. Who is she now, and what is an account?
DOCS: docs.cscs.ch/platforms/mlp/ · swiss-ai.org/compute-grants
-->

<!-- TODO(verify): the small/large policy numbers come from the MLP policies page,
which is still a docs preview at cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/
and is being merged into docs.cscs.ch in the coming days. Swap the footer link and the
"Where to read more" entry to the final docs.cscs.ch URL before the session, and
re-check the numbers at that point. The call dates come from swiss-ai.org, not from
CSCS — re-check them the week before, they change per call. -->

---

<div class="audience all">Everyone</div>

# Your account lives as long as one project does

An account can belong to several projects. It closes only when the last one closes.

<div class="cols">
<div>

### Three roles in the portal

- **Project administrator** — the PI. Anna.
- **Project manager** — the deputy PI.
- **Project member** — everyone else. Ben.

Administrators and managers **invite people** and **assign roles**.

</div>
<div class="card">

### One account, many projects

- Your **email address** identifies you — one address, one account
- Open while **at least one** project is open
- When the last one closes: **90 days** to retrieve your data
- A later invitation **re-enables** the same account

</div>
</div>

<div class="accent">

If you are a PI and you have never opened `portal.cscs.ch`, this module is the one to stay awake for.

</div>

<!--
SAY:
- The portal uses three words. People often guess them wrong.
- Project administrator is the PI. That is Anna.
- Project manager is the deputy PI.
- Project member is everyone else. That is Ben.
- Only the first two can invite people and set roles.
NOW THE IMPORTANT PART. Say it slowly:
- Your account is identified by your email address. One address, one account.
- Your account belongs to projects, and it can belong to several at the same time.
- It stays open while at least one of those projects is open.
- When the last project closes, the account is closed too.
- After that you have 90 days to copy your data out.
- Good news: if someone invites you to a project later, the same account is switched back on.
- People forget this every year. Say it slowly.
NEXT: Anna has a project and a role. Let us open the portal.
DOCS: docs.cscs.ch/accounts/
-->

<!-- TODO(verify): docs.cscs.ch/accounts/ backs only the middle of this card — "accounts
are bound to projects, and accounts will be closed with the project unless the account
is also part of another open project". The two ends do not appear there: that the email
address is the unique identity, and that a later invitation re-enables the same account
rather than creating a new one. Both come from Andrea as ML Platform service manager.
Confirm, then get them written into the docs page. -->

---

<div class="audience">PIs and deputies</div>

# The portal is where the project lives

`portal.cscs.ch` — organisation, then project, then Team, then Invitations.

<div class="cols-narrow">
<div>

- Log in with your CSCS account and MFA
- Pick your **organisation**
- Pick the **project**
- **Team** lists everyone and their role
- **Invitations** is where you add people

<div class="accent quiet">

Same login as every other CSCS web application.

</div>

</div>
<div class="shot">

**SCREENSHOT**

`portal.cscs.ch` — project page with the Team tab open, roles column visible.
Anonymise real names.

</div>
</div>

<!--
SAY:
- This is a tour, not a tutorial. One sentence per step.
- Log in. Pick your organisation. Pick your project.
- Two tabs matter: Team and Invitations.
- Team answers the question "who is on my project and what can they do".
- That is the question PIs email us about most.
POINT AT: the roles column in the screenshot.
NEXT: Anna is looking at Team. Ben is not there yet. Let us add him.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

---

<div class="audience">PIs and deputies</div>

# Adding Ben takes one email address

One email address, or a CSV for a whole cohort. Either way the invitation carries the role.

<div class="cols">
<div>

### One person

Green **Invite Users** button, enter the email address, assign the role.

### A whole group

Upload a CSV with three columns:

```
Email,Role,Project
CragAlvarado@example.com,Project member,prj02
```

</div>
<div class="card dark">

### What Ben receives

- An email invitation
- **Already has a CSCS account** → accepts via the login page
- **New to CSCS** → follows the account creation procedure

</div>
</div>

<!--
SAY:
- Two ways to do this. Both are fast.
- One person: green Invite Users button, email address, role.
- A group: upload a CSV file. Three columns. Exactly this header.
- Useful when ten students arrive in September.
- On the right is what Ben receives.
- If he already has a CSCS account, he logs in and accepts.
- If he is new, the invitation sends him to account creation. That is the next slide.
EXPECT THIS QUESTION: "Can I change a role later?"
- If the network works, open the Team tab and show it.
- Do not promise anything you have not clicked yourself.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

<!-- TODO(verify): whether, and by whom, an existing member's role can be changed after
the invitation is NOT documented — docs.cscs.ch/accounts/waldur/ covers only the
invitation flow. Andrea's expectation is that a PI and a deputy PI can both do it from
the Team tab. Click it in the portal, then either put one line on this slide or get it
into the docs page. Until then the slide claims nothing either way. -->

---

<div class="audience all">Everyone</div>

# Check the consumption monthly, not in the last week

The portal shows what the project was granted and what it has burned.

<div class="cols-narrow">
<div>

- **Everyone on the project** sees the project total — not just the PI
- Per-user usage sits inside the detail of each resource
- There is **no per-user total** across the project

<div class="accent">

<span class="tag">In progress</span>
We are actively improving these views — compute, storage, and the new inference resources.

</div>

</div>
<div class="shot">

**SCREENSHOT**

`portal.cscs.ch` — the project resources view. Granted vs used, the per-user breakdown,
**and** expected, minimal, grace and the end date. Annotated with the same words as the
next slide.

</div>
</div>

<!--
SAY FIRST, to correct a wrong assumption:
- This view is not only for the PI.
- Every project member can see the total for the project.
- Open one resource and you see the usage per user inside it.
- What you cannot see is one total per user for the whole project.
- If you want that number, you add it up yourself.
POINT AT THE RED BAR. Say it as a promise, not as an excuse:
- We know these views are not good enough yet.
- We are working on them now.
- This covers compute, storage, and the new inference resources.
- If someone has a request, ask them to raise it in the discussion at the end.
NEXT: Why every month? The next slide explains.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

<!-- TODO(verify): the consumption view is not documented on
docs.cscs.ch/accounts/waldur/. The visibility rules above come from Andrea as ML
Platform service manager, not from the docs — see notes/sources.md. Confirm the exact
tab name when capturing the screenshot, and consider getting this written into the
docs page. -->

---

<div class="audience">PIs and deputies</div>

# Spend it linearly, or you lose it

Every project gets a credit in GPU hours, spent as your jobs run. Each month has an expected amount, and a minimal you must not fall below.

<!-- The <div> wrapper is load-bearing: CommonMark only treats a whitelisted set of tag
     names as HTML blocks, and <svg> is not one of them, so an unwrapped diagram is
     parsed as inline HTML and its text nodes are flattened into a paragraph. Keep the
     whole block free of blank lines, which would close the HTML block early. -->
<div class="diagram">
<svg viewBox="0 0 1160 320" width="100%" role="img"
     aria-label="Top: three example months of usage as bars against two thresholds, an expected line and a minimal line below it separated by the grace. Above expected is fine, in between rolls over, below the minimal the gap is lost. Bottom: the project timeline, 6 or 12 months, then a 90-day data-retrieval period, then access is gone.">
  <g font-family="Inter, sans-serif">
    <!-- ── row 1: the monthly rule ───────────────────────────────────────── -->
    <text x="90" y="20" font-size="13" font-weight="600" fill="#888888" letter-spacing="0.6">IN ANY GIVEN MONTH</text>
    <!-- your usage -->
    <rect x="140" y="52"  width="100" height="128" fill="#9A9AA0"/>
    <rect x="320" y="90"  width="100" height="90"  fill="#9A9AA0"/>
    <rect x="500" y="148" width="100" height="32"  fill="#9A9AA0"/>
    <!-- the credit burned by falling short -->
    <rect x="500" y="112" width="100" height="36" fill="#F3E0E1" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="550" y="136" font-size="13" font-weight="600" fill="#D61F26" text-anchor="middle">lost</text>
    <!-- thresholds -->
    <line x1="100" y1="70"  x2="800" y2="70"  stroke="#D61F26" stroke-width="2"   stroke-dasharray="7 5"/>
    <line x1="100" y1="112" x2="800" y2="112" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="3 4"/>
    <line x1="100" y1="180" x2="820" y2="180" stroke="#E5E5E5" stroke-width="2"/>
    <text x="810" y="75"  font-size="15" font-weight="600" fill="#D61F26">expected</text>
    <text x="810" y="117" font-size="15" font-weight="600" fill="#D61F26">minimal</text>
    <!-- the grace between the two -->
    <line x1="990" y1="70" x2="990" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="70" x2="996" y2="70"  stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="112" x2="996" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <text x="1006" y="86"  font-size="13" font-weight="600" fill="#D61F26">grace</text>
    <text x="1006" y="104" font-size="12" fill="#555555">15–50%, by budget size</text>
    <!-- what each case means -->
    <g text-anchor="middle" fill="#1A1A1A">
      <text x="190" y="202" font-size="14" font-weight="600">you go faster</text>
      <text x="190" y="220" font-size="12" fill="#555555">fine — lower priority while ahead</text>
      <text x="370" y="202" font-size="14" font-weight="600">you go slower</text>
      <text x="370" y="220" font-size="12" fill="#555555">the rest rolls over</text>
      <text x="550" y="202" font-size="14" font-weight="600">you fall below</text>
      <text x="550" y="220" font-size="12" fill="#555555">that credit is gone</text>
    </g>
    <!-- ── row 2: the project timeline ───────────────────────────────────── -->
    <line x1="90" y1="240" x2="1140" y2="240" stroke="#F0F0F0" stroke-width="1"/>
    <text x="90" y="262" font-size="13" font-weight="600" fill="#888888" letter-spacing="0.6">OVER THE WHOLE PROJECT</text>
    <line x1="380" y1="288" x2="870" y2="288" stroke="#9A9AA0" stroke-width="5"/>
    <line x1="870" y1="288" x2="1060" y2="288" stroke="#D61F26" stroke-width="5"/>
    <line x1="870" y1="274" x2="870" y2="302" stroke="#1A1A1A" stroke-width="2"/>
    <line x1="1060" y1="278" x2="1060" y2="298" stroke="#1A1A1A" stroke-width="2"/>
    <text x="625" y="310" font-size="13" fill="#555555" text-anchor="middle">6 or 12 months</text>
    <text x="870" y="264" font-size="14" font-weight="600" text-anchor="middle">project ends</text>
    <text x="965" y="310" font-size="13" font-weight="600" fill="#D61F26" text-anchor="middle">90 days — retrieve your data</text>
    <text x="1074" y="293" font-size="13" fill="#555555">gone</text>
  </g>
</svg>
</div>

<div class="accent">

Out of credit before the end? The `low` partition, capped at two months of your budget.
All the rules: **docs.cscs.ch/platforms/mlp/policies/**

</div>

<!--
This is the most useful slide for PIs. Do not rush it.
SAY, to frame it first:
- Every project is granted a compute credit, in GPU hours.
- The model is usage based. You spend the credit as your jobs run.
- And you are expected to spend it more or less evenly, month by month.
THEN THE TWO NUMBERS:
- Every month has two numbers.
- Expected: how much you should use this month.
- Minimal: the expected amount minus a grace. The grace is 15 to 50 per cent, depending on how big your budget is.
NOW WALK THROUGH THE THREE BARS, left to right:
- Left bar: you used more than expected. This is fine. You only run at lower priority while you are ahead.
- Middle bar: you used less, but you stayed above the minimal. The rest moves to the next months.
- Right bar: you fell below the minimal. The red box is credit you lost. It does not come back.
THEN THE TIMELINE AT THE BOTTOM:
- The project runs 6 or 12 months.
- Then it ends. Then you have 90 days to copy your data out. Then access stops.
POINT AT THE RED BAR:
- If you run out of credit early, you are not stuck.
- You can still use the low partition. About two months of your budget.
POINT AT THE LINK IN THE RED BAR:
- Every number on this slide is on that one page. Take a photo of it.
NEXT: That is Anna finished. The rest of the module is Ben.
DOCS: docs.cscs.ch/platforms/mlp/policies/
-->

<!-- TODO(verify): every number on this slide — the 15-50% grace, the two-month cap on
the low partition, the 90-day retrieval window — comes from the MLP policies page,
which is still a docs preview at cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/.
Re-check them once it is merged into docs.cscs.ch.
The slide now PRINTS the URL docs.cscs.ch/platforms/mlp/policies/, which does not resolve
yet. Load it in a browser before the session. If it is still not live on 26 August, fall
back to docs.cscs.ch/platforms/mlp/ here and on the "Where to read more" slide — a URL
that 404s on a projector costs more credibility than a less precise one. -->

---

<div class="audience all">Everyone</div>

# No MFA means no SSH. There is no way around it

New accounts are usually opened within 48 hours — plan for it, do not do this the night before.

<div class="cols">
<div>

### Creating the account

- Scanned ID or passport
- **Institutional** email address
- Correct personal details
- Usually open within **48 hours**

</div>
<div class="card">

### Enrolling MFA

Log in to any CSCS web application, enter the code sent by email, scan the QR code, type the six-digit code.

Google Authenticator and FreeOTP are tested; any TOTP app works.

</div>
</div>

<div class="accent">

"It is not possible to log in to CSCS systems using SSH without registering a device and creating certified SSH keys."

</div>

<!--
Now it is Ben's turn.
SAY:
- To create an account he needs three things.
- A scan of his ID or passport. An institutional email address. Correct personal details.
- It usually takes up to 48 hours. So do not do this the night before a deadline.
- Then MFA. It is not optional.
- Log in to any CSCS web page. Type the code you get by email. Scan the QR code. Type the six digits.
- Any TOTP app works. We tested Google Authenticator and FreeOTP.
READ THE RED BAR OUT LOUD. It is the exact sentence from the docs:
- This prevents our most common ticket.
- Someone tries SSH, gets "permission denied", and never set up MFA.
NEXT: Ben has an account. Now he needs a key.
DOCS: docs.cscs.ch/accounts/account-create/ · docs.cscs.ch/access/mfa/
-->

---

<div class="audience all">Everyone</div>

# Signed keys expire after one day

Generate the key pair once. Sign it every day. Five signatures per day, maximum.

```bash
brew install eth-cscs/tap/cscs-key       # macOS, Linux — or download the release binary
ssh-keygen -t ed25519 -f ~/.ssh/cscs-key # once, ever
cscs-key sign                            # every day: signs ~/.ssh/cscs-key
ssh-add -t 1d ~/.ssh/cscs-key            # load it into the agent
```

<div class="cols">
<div>

- Keys are valid for **1 day** by default
- You can create up to **5 keys per day**
- `cscs-key list` and `cscs-key revoke` if something leaks

</div>
<div class="card">

### No CLI? Use the dashboard

`user-account.cscs.ch` → SSH Keys → Sign Key. Paste the public key, download the certificate.

</div>
</div>

<!--
People take a photo of this slide. Pause here.
SAY, one line per command:
- Install cscs-key. One time.
- Create the key pair. One time. Only once, ever.
- Sign it. This is the daily step.
- Load it into the agent.
THEN THE RULES:
- A signed key lasts one day.
- You can sign five keys per day. That is enough for normal work.
- If a key leaks, use cscs-key list and cscs-key revoke.
- Cannot install the CLI on your machine? Use the web page. Same result.
- All of this is on the handout. Nobody needs to type now.
NEXT: Ben has a signed key. Where does he send it?
DOCS: docs.cscs.ch/access/ssh/
-->

---

<div class="audience all">Everyone</div>

# Everything goes through ela.cscs.ch

Ela is the jump host. You never connect to Clariden or Bristen directly.

<div class="cols">
<div>

```
Host ela
    HostName ela.cscs.ch
    User cscsusername
    IdentityFile ~/.ssh/cscs-key

Host clariden
    HostName clariden.alps.cscs.ch
    User cscsusername
    ProxyJump ela
    IdentityFile ~/.ssh/cscs-key
    IdentitiesOnly yes
```

</div>
<div class="stack">
<div class="card">

### Then it is just

`ssh clariden` — add `-A` to forward your agent.

</div>
<div class="card">

### Bristen needs its own block

Copy the `clariden` block, change the alias and `HostName`. Ela is shared.

</div>
<div class="card code-sm">

### Tunnel to a compute node

```bash
ssh -N \
  -J ${MYUSER}@ela.cscs.ch,${MYUSER}@${CLUSTER}.alps.cscs.ch \
  -L ${PORT}:localhost:${PORT} ${MYUSER}@${NODE}
```

</div>
</div>
</div>

<!--
SAY:
- Write this in your SSH config one time. Then you never think about the jump host again.
- Two entries. Ela. And the cluster behind it, with ProxyJump.
- Replace cscsusername with your real username.
- After that you just type: ssh clariden.
BE VERY CLEAR HERE. People get this wrong:
- Bristen is not a hostname you swap in.
- It is a second Host block of its own. The Ela entry stays shared.
- Clariden is for production runs. Bristen is for test and development, best effort.
LAST BOX:
- This is the question we get at every drop-in. How do I reach a dashboard or a notebook on a compute node?
- That is the tunnel. It is on the handout and in the docs.
- Do not explain it here. There is no time.
NEXT: Ben is in. Two things I am not covering.
DOCS: docs.cscs.ch/access/ssh/ · /clusters/clariden/ · /clusters/bristen/
-->

---

# What this module deliberately skipped

<div class="cols">
<div>

- **Password and MFA troubleshooting** — service desk, they are fast
- **Legacy key management** — `sshservice.cscs.ch` was retired in May 2026

</div>
<div>

- **Service accounts** — for pipelines. Scoped to one project, grant access to all its resources. The **PI** requests one by Service Desk ticket
- **Kubernetes and the HPC Console** — a pointer only, see the wrap-up
- **Everything you do once you are in** — modules 2 to 4

</div>
</div>

<div class="accent">

You now have an account, a project and a shell. The rest of the hour is what you do with them.

</div>

<!--
One line each. Ten seconds in total. Do not start a discussion here.
SAY:
- Password and MFA problems: write to the service desk. They are fast.
- The old SSH service was switched off in May 2026. Some people still have it in their notes. Say the date out loud.
- Service accounts exist. They are for pipelines. One service account belongs to one project.
- The PI asks for one with a Service Desk ticket. It is not a self-service button.
- Kubernetes and the HPC Console: only a pointer today. See the wrap up.
READ THE RED BAR:
- You now have an account, a project and a shell.
NEXT, hand over to module 2:
- Ben has a shell on Clariden and an empty home directory.
- His first question is where to put two terabytes of training data.
-->

---

<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Getting a project

- **MLP project policies** — docs.cscs.ch/platforms/mlp/policies/
- **Applying** — swiss-ai.org/compute-grants
- **Accounts, projects and the portal** — docs.cscs.ch/accounts/

### Getting in

- **Creating an account** — docs.cscs.ch/accounts/account-create/
- **MFA** — docs.cscs.ch/access/mfa/
- **SSH, key signing, Ela** — docs.cscs.ch/access/ssh/

</div>
<div class="card dark">

### Keep these three

- `portal.cscs.ch` — the project
- `user-account.cscs.ch` — the account and the keys
- `docs.cscs.ch` — everything else

### Stuck?

- **service-desk@cscs.ch**
- The handout has every command from this module

</div>
</div>

<!--
Do not read this slide out loud.
SAY only this:
- Three addresses to remember.
- portal.cscs.ch for your project.
- user-account.cscs.ch for your account and your keys.
- docs.cscs.ch for everything else.
- And the service desk when none of those help.
- Everything on this slide is also on the handout.
NEXT: hand over to module 2 immediately. We are on the clock.
-->
