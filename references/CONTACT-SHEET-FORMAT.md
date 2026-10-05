# CONTACT-SHEET-FORMAT — how the reference is laid out and read

The contact sheet is how a reference gets summarised into one readable grid. It
is both an **input** (the user may hand you one) and an **output** (Stage 3 builds
V1/V2/V3 from the reference). This file defines the format so every sheet — in or
out — is read and made the same way.

---

## 1. Header (always present)

```
CONTACT SHEET V<N> - <NAME>  (<FRAME COUNT> FRAMES • <ASPECT>)
STYLE: <WORD> • <WORD> • <WORD> • <WORD>
```

Example (a real reference):
```
CONTACT SHEET V2 - UPGRADED  (68 FRAMES • 16:9)
STYLE: CINEMATIC • MODERN • CLEAN • PREMIUM
```

- **V<N>** — the sheet variant (see §4).
- **FRAME COUNT** — how many panels; a panel is one sampled moment.
- **ASPECT** — 16:9 / 9:16 / 1:1 / 4:5 / 2.39:1.
- **STYLE line** — 3-4 style words; these become the visual asset-prompt keywords.

## 2. Panels

- A **grid**, read left-to-right, top-to-bottom, **in time order**.
- Each panel carries a **timecode label** (`00s`, `01s`, …) — the seconds (or
  frames) it was sampled at.
- **How many:** enough to show every distinct state — a new sheet when text
  changes, a new visual, or a new beat. Typically **1 panel per 0.5-1 s**, or one
  per beat. A 68-frame sheet for a ~35 s piece ≈ 2 panels/s.
- **Reading a panel:** zoom it; read its **text verbatim**, its **element(s)**,
  its **colour**, and its **motion**.

## 3. What a sheet must let a reader reconstruct

From the sheet alone, a reader should be able to answer:
1. **What changes and when** — the text/element timeline.
2. **What stays** — the recurring title, the persistent brand frame.
3. **The palette** — dominant / accent / background.
4. **The style** — from the style line + the look.
5. **The pacing** — how fast panels change.

If a sheet cannot answer those five, it is incomplete — add panels.

## 4. The three variants (V1 / V2 / V3)

When you *build* sheets from a reference (Stage 3) and again before a render
(Render Gate), produce three variants:

| Variant | Layout | Best for |
|---|---|---|
| **V1 — Grid** | tight grid, many panels | overview; spotting the text timeline |
| **V2 — Upgraded** | grid + labels + style header | reading text + style; the "upgraded" look |
| **V3 — Filmstrip / QC** | large panels, few per row | fine detail; colour and composition QC |

Show all three, then ask: *"Did you like any of these, or shall I generate more
variants so you can choose?"* Render only after sign-off.

## 5. Building one

Tool: `tools/contact_sheet.py --frames <dir> --out sheet.png --variant v2 --aspect 16:9`.

The tool labels each panel with its time, writes the header, and lays the grid.
Run it for V1, V2 and V3.

---

## 6. Reading a *supplied* sheet (the common case)

When the **user** hands you a sheet:

1. Read the **header** (name, frame count, aspect, style line).
2. Read **every panel in order**, zooming each.
3. Extract the **recurring text** vs the **changing text**.
4. Extract the **data/numbers** verbatim (e.g. `82%`, `+72%`, `240K Users ↑ 12%`).
5. Extract the **palette** and **type**.
6. Note the **bottom menus / badges / buttons** (e.g. `Data Insights Strategy
   Growth`, a `LIVE` badge).
7. Fold all of it into `ANALYSIS.md`.

> A supplied sheet is a **legitimate reference** — you do not need the source
> video to rebuild from it. Read it as carefully as a video.
