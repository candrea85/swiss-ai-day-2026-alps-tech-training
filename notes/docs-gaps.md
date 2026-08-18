# Documentation gaps found while writing this session

Every gap below was hit while writing this session and checking each claim against
`docs.cscs.ch`. In each case the behaviour is known and correct, but nothing on the
public documentation states it, so a slide asserting it cannot be reviewed by anyone
except the person who already knew.

The body of this file is written to be pasted into an issue on the documentation
repository. Keep adding to it as the remaining modules are finished — the list will grow.

Source of the corrections: Andrea Ceriani, ML Platform service manager.
Cross-referenced in `notes/sources.md`.

---

## The portal — `docs.cscs.ch/accounts/waldur/`

The page currently has four sections: the tool, log in, select the organisation, invite
users. It stops at the invitation. Everything a PI does *after* that is undocumented.

- [ ] **Who can see consumption, and at what granularity.** Nothing on the page
      describes the usage view at all. The behaviour is:
      - every **project member** — not only the PI — sees the **project total**;
      - **per-user** usage is visible inside the detail of each individual resource;
      - there is **no per-user total** across the whole project.
      Worth stating explicitly, because the common assumption is that usage is a
      PI-only view.

- [ ] **Changing the role of an existing member.** The page documents assigning a role
      *at invitation time* only. It should say whether an existing member's role can be
      changed afterwards, by whom (project administrator, project manager, or both) and
      from where (the Team tab). This is a routine request and there is currently no
      page to point people at.

- [ ] **The Team tab.** Mentioned only in passing as part of the path to Invitations.
      It is the answer to "who is on my project and what can they do", which is the
      question PIs ask most often, and it deserves its own short section.

## Accounts — `docs.cscs.ch/accounts/`

The page states that "accounts are bound to projects, and accounts will be closed with
the project unless the account is also part of another open project". That is the middle
of the lifecycle. Both ends are missing.

- [ ] **The email address is the account identity.** One address, one account, however
      many projects. Not stated anywhere.

- [ ] **A later invitation re-enables the same account.** When the last project of an
      account closes, the account is closed — but a subsequent invitation switches the
      *same* account back on rather than creating a new one. This is the difference
      between a user believing their account was deleted and understanding that it is
      dormant, and it is worth one sentence.

## ML Platform policies — what the grace period actually suspends

- [ ] The policies page says a project "remains accessible for a grace period of 90 days
      for data retrieval". It does not say what stops at the end date and what does not.
      The behaviour is: the **end date stops the compute**, the project itself **stays
      active** for those 90 days, and only then does it close. Users read "the project
      ends" and assume everything goes at once, including their data. One sentence on
      that page would prevent a recurring panic.

## Storage — pending merge, plus one genuinely open question

- [ ] `datacache` and the Ritom scratch exist only on the `/442` preview. Nothing to fix
      here — a tracking entry, to be closed when the pages land and the module 2 links
      are re-pointed.
- [ ] **Ritom is documented as Clariden-only, and it is not.** The preview's table says
      `/ritom/scratch/cscs/$USER` "(Clariden only)" and the prose says "On Clariden, the
      cleanup policy ... is being finalised". Per Andrea it is mounted more widely than
      that. This is wrong information rather than missing information, so it matters
      more: someone will plan around a filesystem they think they do not have.

- [ ] **Ritom's cleanup policy "is being finalised".** This one is not just a merge:
      until there is a number, nobody can plan a workflow on that filesystem, and the
      slide has to say "being finalised" out loud. Worth closing before people start
      using it and discover the policy afterwards.

## ML Platform policies — pending merge

- [ ] The policies page is still only a preview at
      `cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/`. Module 1 depends on it
      for the small/large project comparison and for the whole linear-consumption slide
      (expected and minimal consumption, the 15% to 50% grace, the `low` partition cap,
      the 90-day retrieval window). Nothing to fix here — this is a tracking entry, to be
      closed when the page lands on `docs.cscs.ch` and the links in
      `slides/01-project-access.md` are switched over.

---

## Why this matters beyond the docs

The session is built on the rule that every technical claim must be traceable to
`docs.cscs.ch`. Where that fails, the deck either says nothing — which leaves the
audience without an answer they came for — or asserts something a reviewer cannot check.
The deck currently carries **16** `TODO(verify)` markers across seven files. Most of
them exist only because of the gaps above, and most would close on their own the day the
pending pages are merged. The ones that would not are the portal behaviours and the
project lifecycle — those need somebody to write a paragraph.
