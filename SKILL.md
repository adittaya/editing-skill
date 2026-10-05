---
name: editing-skill
description: A reference-first editing skill. Give it ONE reference (a video file or a contact sheet), and it extracts that reference at maximum accuracy - every frame, every element, zoomed in - then writes TWO separate asset prompts (one for visual assets, one for sound) and asks you for the A-roll. Use when someone wants to replicate or rebuild the look, motion, text and pacing of an existing edit with their own footage, voiceover, avatar or podcast. Triggers on "replicate this edit", "rebuild this video", "extract this reference", "make it look like this", "edit like this reference", "copy this style".
---

# Editing Skill — Reference In, Finished Edit Out

This is the whole skill. Read it top to bottom. It is the only skill file you
need; the folders beside it give you the power to execute every stage.

**What it does in one sentence:** you hand it a **reference** — a video, or a
contact sheet — and it **extracts that reference at maximum accuracy**, turns the
extraction into an **analysis** plus **two asset prompts**, asks you for the
**A-roll**, and then **rebuilds the edit** with your own material.

```
REFERENCE  ->  EXTRACT (100% accuracy)  ->  ANALYSIS.md
                                        ->  ASSETS-VISUAL.md  (images + logos)
                                        ->  ASSETS-SOUND.md   (music + SFX)
YOU        ->  A-ROLL (voiceover / avatar / podcast, per the contact sheet)
                                        ->  BUILD  ->  QA  ->  FINISHED EDIT
```

---

## 0. THE ONE THING YOU ASK FOR

You ask the user for **one thing only**: the **reference**.

It can be:
- a **video file** (any length), or
- a **contact sheet** (an image or PDF of frames — like "CONTACT SHEET V2 —
  68 FRAMES • 16:9"), or
- a **link** to the reference.

Do **not** ask for the A-roll yet. Do **not** ask for assets yet. Do **not** ask
for a brief. **Extract first.** Everything else is derived from the reference.

> If the user has already told you the reference, skip to **Stage 1**.

---

## 1. STAGE 1 — INTAKE

Confirm what you received and how you will read it:

| Input | How you read it |
|---|---|
| Video file | Pull **every frame** (or the highest rate the tool allows), plus the audio track. |
| Contact sheet (image/PDF) | Read **every panel**; zoom each panel to its own element level. |
| Link | Fetch it; if it is a video, treat as video; if a page, treat as a contact sheet. |

State the plan in one line, then go. Example: *"Got a 42 s 16:9 video. I'll pull
all frames, zoom each into quadrants, OCR every text element, and measure the
palette, cuts and loudness."*

---

## 2. STAGE 2 — EXTRACT (THE EXTRACTION LAW)

**This is the heart of the skill. Accuracy is the product.**

> ### THE EXTRACTION LAW
> Extract **everything**, at **maximum resolution**, and **zoom in** until no
> element is unread. Do not sample and guess. Do not summarise. Take as long as
> it takes. A wrong extraction poisons every later stage.

### 2.1 What "extract everything" means

For a **video**, extract in this order:
1. **All frames** — every frame, or the highest FPS the tool allows (default 2 FPS
   for a first pass, then **dense 10-30 FPS around every cut** and every text
   change). Never analyse from memory of a few thumbnails.
2. **Audio** — loudness curve, music cues, SFX hits, and a full transcript with
   word timings.
3. **Cuts** — every scene change, on the frame.
4. **Text** — OCR **verbatim**, every on-screen word, with its in/out time.
5. **Elements** — logos, UI, charts, characters, icons, backgrounds.
6. **Colour** — sampled hex per element, per shot.
7. **Motion** — what moves, how, and why (per the camera/motion law).

For a **contact sheet**, extract in this order:
1. **Every panel**, in order, at its own zoom.
2. **Verbatim text** in every panel (OCR).
3. **The recurring text pattern** (which line repeats, which changes).
4. **The data/number elements** (e.g. "82%", "+72%", "240K Users ↑ 12%").
5. **The style header** (e.g. "CINEMATIC • MODERN • CLEAN • PREMIUM").
6. **The palette and type**, sampled per panel.

### 2.2 ZOOM until it is readable

Every frame gets a **zoom pass**: split it into a grid (2×2, then 3×3 on dense
frames), and read each tile on its own. Small text, faint logos and fine UI are
only legible when zoomed. **If you cannot read it at the frame level, zoom.**

### 2.3 Verify, then verify again

- **Pass 1** — extract.
- **Pass 2** — re-open a random sample of frames/tiles and check the extraction
  against them. Fix every miss.
- **Pass 3** — check the *time* axis: does every text element have a plausible
  in/out? Does every cut line up with an audio cue?

Write the running notes as you go — they become `ANALYSIS.md` in Stage 3.

### 2.4 Tools for this stage
- `tools/extract.py` — all frames + zoom tiles + optional dense rate.
- `tools/analyze.py` — palette, cuts, loudness, transcript scaffold.
- `tools/contact_sheet.py` — build V1/V2/V3 contact sheets from any frames.
- See `references/EXTRACTION-PROTOCOL.md` for the full checklist.

---

## 3. STAGE 3 — ANALYSIS.md (the extraction, written down)

Turn the extraction into **one file**: `ANALYSIS.md` (template:
`templates/ANALYSIS.template.md`). It must contain, at minimum:

1. **Reference summary** — duration, aspect, fps, style header, one-line read.
2. **Beat map** — a row per shot/text event: `time | shot | on-screen text
   (verbatim) | element(s) | colour | motion | audio cue`.
3. **Text map** — every on-screen string, verbatim, with in/out times.
4. **Palette** — measured hex, with the role of each colour.
5. **Type system** — families (or nearest classification), weights, sizes,
   placement, animation.
6. **Motion grammar** — the moves, transitions and their triggers.
7. **Element inventory** — every logo, icon, chart, character, prop.
8. **Audio map** — music cues, SFX, loudness, and the transcript.
9. **Contact sheet** — the V1/V2/V3 sheets built from the reference.
10. **Open questions** — anything genuinely unreadable, flagged honestly.

> **THE HONESTY LAW.** Where something is measurable (colour, timing, text,
> loudness), state it as measured. Where it is inferred (a font family, a hidden
> technique), say **"inferred"**. Never present a guess as a measurement.

---

## 4. STAGE 4 — THE TWO ASSET PROMPTS (THE TWO-PROMPT LAW)

> ### THE TWO-PROMPT LAW
> From `ANALYSIS.md`, write **exactly two** asset prompts, as **two separate
> files**. One is for **visual assets**. One is for **sound**. Nothing else.

### 4.0 THE DEPTH LAW — each file IS a prompt, at full depth
Write each file so it can be handed **straight to a generator** with no
rewriting. It **opens with the role + the task**, gives a **deliverable tree**
(one zip containing multiple zips inside), numbers every asset with its own
**executable brief** carrying **exact values** (hex, px, durations, BPM, cue
times, filenames), and **ends with acceptance checks**.

> A thin list of names is **wrong**. Match the depth of the worked examples:
> `examples/EXAMPLE-ASSETS-VISUAL.md` and `examples/EXAMPLE-ASSETS-SOUND.md`.
> If your file is much shorter than those, it is under-specified.

### 4.1 `ASSETS-VISUAL.md` — the visual-asset prompt
A ready-to-paste prompt for an AI with **image generation**. Three sections:
- **images** — backgrounds, textures, plates, illustrations, charts,
- **transparent images** — PNG/alpha cut-outs, icons, caption PNGs,
- **logos** — wordmark + mark (supplied or a brief; never a real brand's mark).

Deliverable: **`visual-assets.zip`** holding `MANIFEST.md`, `images.zip`,
`transparent.zip`, `logos.zip`.

### 4.2 `ASSETS-SOUND.md` — the sound prompt
A ready-to-paste prompt for an AI with **audio generation**. Two sections:
- **music** — mood, genre, BPM, length, instrumentation, energy arc,
- **sound effects** — whooshes, hits, UI clicks, risers; each timed to a beat.

Deliverable: **`sound-assets.zip`** holding `MANIFEST.md`, `music.zip`, `sfx.zip`.

### 4.3 The rule about the two files
- **Two files. Separate. Always.** Never merge them into one prompt.
- **Visual = images + transparent + logos. Sound = music + SFX.** Do not put code
  or video clips in either — **no video clips, no voiceover** (the A-roll comes
  from the user; see Stage 5).
- Each file is **itself a prompt** — copy-paste ready, at full depth.

Templates: `templates/ASSETS-VISUAL.template.md`, `templates/ASSETS-SOUND.template.md`.
**Worked examples (match these):** `examples/EXAMPLE-ASSETS-VISUAL.md`,
`examples/EXAMPLE-ASSETS-SOUND.md`. Full spec: `references/ASSET-PROMPTS.md`.

---

## 5. STAGE 5 — THE A-ROLL (you supply it)

Now — and only now — you ask the user for the **A-roll**. The A-roll is **what
carries the meaning**: a **voiceover**, a **talking avatar**, a **podcast**
segment, or a **talking-head** — whichever the user has.

> ### THE A-ROLL LAW
> The user supplies the A-roll **according to the contact sheet**. The contact
> sheet says which shots need a speaker and for how long; the user records or
> provides the voice/avatar to match.

Write the ask as `A-ROLL-REQUEST.md` (template:
`templates/A-ROLL-REQUEST.template.md`): per shot, state whether a speaker is
needed, the duration, and the line (from the transcript/analysis). If the
reference has no speaker, say so and note that the A-roll may be voiceover-only
or absent.

**If the A-roll arrives as a talking-head**, run **STEP 0.5 — A-ROLL PREP**
first: the **first job is the background** — keep it, or matte the character off
(or onto green) before any concept work.

---

## 6. STAGE 6 — BUILD

With the reference analysed, the two asset prompts delivered, and the A-roll in
hand, build the edit to match the analysis:

1. **CONCEPT** — restate the beat map as a build plan, using `ANALYSIS.md` as the
   blueprint (see `references/EDIT-MAP.md` for the fast path per edit type).
2. **Feature map** — walk the full feature catalogue
   (`references/ADVANCED-FEATURE-USE-CASES.md`) and mark which advanced features
   the reference uses and where. You have the power to use all of them.
3. **Assemble** — cut to the beat map; place the generated visual assets and the
   sound assets; lay the A-roll; add the text exactly as mapped.
4. **Contact-sheet variants** — build **V1/V2/V3** and show them before the full
   render (**RENDER GATE**).

### The laws you build by
- **Palette & Gradient Law** — use the analysis's measured palette; gradients are
  deliberate, never decorative mud.
- **Text Law** — on-screen text **maps the visual**; generic subtitles are never
  the default; a plain SRT is an optional sidecar only.
- **Sentence Law** — every spoken sentence gets its own visual event on its
  stressed word (±100 ms).
- **Camera Law** — one wrapper, one move at a time, a reason per zoom, never cut
  while zoomed, motion blur only while fast.
- **No-Metadata Law** — never leave tool watermarks, export tags or stray UI in
  the frame.
- **No-Clank Law** — nothing that reads as an accident; every sound, cut and move
  is motivated.
- **Asset & Clearance Protocol** — if you need a logo, a likeness or licensed
  material, **ask**; asking is expected, never a failure.

---

## 7. STAGE 7 — QA

Run the master checklist before delivery:
- `tools/qa_check.py` + the checklist in `references/` (see QA section below).
- **AUDIT → AI RE-THINK → REVALIDATE.**
- Write `EDIT-QA.md` recording what was checked and what was fixed.

**QA checklist (minimum):**
- Every on-screen text matches the reference's text map (verbatim, timed).
- Every cut lands on the beat map.
- Palette matches the measured hex.
- Audio: loudness target met; every cue present.
- No watermarks, no stray UI, no clank.
- A-roll cleanly integrated (matte/key verified on a sample of frames).

---

## 8. THE ADVANCED-FEATURE POWER

You have the full catalogue of advanced editing features — camera & framing
(zoom in/out, character/face zoom, rack focus, dolly, whip pan, dolly zoom,
parallax), motion, speed & time, transitions, text, colour, compositing/VFX,
audio, AI, stills and workflow. Before building, **walk the catalogue** and mark
what the reference uses. See `references/ADVANCED-FEATURE-USE-CASES.md`.

---

## 9. FILE CONTRACT — what this skill produces

| File | When | What |
|---|---|---|
| `ANALYSIS.md` | Stage 3 | The full extraction of the reference. |
| `ASSETS-VISUAL.md` | Stage 4 | The visual-asset prompt (images + logos). |
| `ASSETS-SOUND.md` | Stage 4 | The sound prompt (music + SFX). |
| `A-ROLL-REQUEST.md` | Stage 5 | The per-shot ask for the user's A-roll. |
| contact sheets (V1/V2/V3) | Stage 3/6 | Visual proof of the extraction and the build. |
| `EDIT-QA.md` | Stage 7 | The QA record. |

**Never merge the two asset prompts. Never ask for the A-roll before the
extraction. Never render before the contact-sheet sign-off.**

---

## 10. GATES

1. **EXTRACTION GATE** — before Stage 3 is "done", the extraction has had its
   verify pass (2.3). Do not move on with unread elements.
2. **ASSET GATE** — the two prompts exist as two separate files (Stage 4).
3. **A-ROLL GATE** — the user has supplied the A-roll per the contact sheet
   (Stage 5).
4. **RENDER GATE** — contact-sheet variants V1/V2/V3 shown and signed off
   (Stage 6).
5. **QA GATE** — the checklist passes and `EDIT-QA.md` is written (Stage 7).

---

## Quick start

1. **User:** drops a reference (video or contact sheet).
2. **You:** extract everything (Stage 2), zoom in, verify.
3. **You:** write `ANALYSIS.md`, `ASSETS-VISUAL.md`, `ASSETS-SOUND.md`.
4. **You:** ask for the A-roll (`A-ROLL-REQUEST.md`).
5. **User:** supplies voiceover / avatar / podcast per the contact sheet.
6. **You:** build to the beat map, show V1/V2/V3, render, QA, deliver.
