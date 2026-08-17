# Screenshots and recordings to capture

Claude cannot produce these. Each entry says exactly which view to capture. Save the
file under `assets/screenshots/` with the filename given, then replace the
`<div class="shot">` placeholder in the slide with a normal Markdown image.

Capture at 2x on a 16:9 window so the image still reads on a projector.

## Set up a demo project first

Everything below is easier, and better, if there is a **dedicated demo project** in the
portal rather than a real one:

- No anonymisation. Nothing to blur, nothing to leak, no chance of a real colleague's
  address appearing on a projector in Bern.
- Name the members after the personas — **Anna** as project administrator, **Ben** as
  project member. The screenshots then show the same two names the story uses, on every
  slide. That coherence is worth more than it sounds when the audience is following a
  narrative.
- It stays available afterwards, for the drop-in sessions and for the next edition.

One thing a demo project **cannot** give you: a consumption history. See capture 2.

## Module 1 — `slides/01-project-access.md`

| # | Filename | Source | View to capture |
|---|---|---|---|
| 1 | `portal-team-tab.png` | demo project | The **Team** tab with the roles column visible and legible: Anna as project administrator, Ben as project member. Slide: "The portal is where the project lives". |
| 2 | `portal-consumption.png` | **a real project** | The single most important capture. See below. |
| 3 | `portal-invite-dialog.png` | demo project | The **Invite Users** dialog with the role dropdown open, so the three role names are readable. Optional — use it if slide "Adding Ben takes one email address" feels too abstract on the day. |
| 4 | `user-account-sign-key.png` | own account | `user-account.cscs.ch` → SSH Keys → **Sign Key**, the paste-and-download step. Optional. |

### Capture 2 — one annotated image, six things on it

Confirmed by Andrea: **granted vs used, the per-user breakdown, expected, minimal, grace
and the project end date are all in the same view.** So this is one screenshot, not two,
and the module needs no extra slide.

Use **a real project partway through its period**, not the demo project: an empty chart
argues the opposite of what the slide says. Blur names and the project ID.

Annotate it with callouts. Use **exactly the words from the diagram** on the next slide —
`expected`, `minimal`, `grace`, `project ends`. If the diagram says "minimal" and the
portal label reads differently, the audience has to translate between the two and the
pairing stops paying off. Where the wording genuinely differs, put both: `minimal (portal
label)`.

The slide is "Check the consumption monthly, not in the last week", and it sits directly
before the slide that explains what those numbers mean. Order on purpose: where to look,
then the rule.

## On showing it live

The style guide says avoid live demos, and that still holds **for the 12-minute slot**:

- MFA on stage costs 30 to 60 seconds of dead air, minimum, and that is when it works.
- The invite flow sends a real email, so it needs a throwaway address prepared anyway.
- The module is already at 12 minutes against a 12-minute budget. A live demo adds two
  to three minutes and there is nothing left to take them from.

The good compromise, if the still images feel flat:

- **Record** the two flows from the demo project as short GIFs or asciinema clips —
  the invite, and navigating to the accounting view. Marp embeds them like any image,
  they always work, and they can be paused.
- Keep the portal **open in a second browser tab** as a fallback for the 30-minute
  discussion at the end. That is where a live click costs nothing if the wifi dies, and
  where somebody will almost certainly ask "can you show me where that is?".

## Modules 2–5

Not yet started. Owners: add your entries here when you draft your module. If the demo
project exists, reuse it rather than screenshotting production.
