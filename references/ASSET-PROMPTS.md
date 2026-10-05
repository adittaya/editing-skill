# ASSET-PROMPTS — the two prompts (visual + sound), separate, always

This is the deep spec behind **Stage 4 (THE TWO-PROMPT LAW)** in `SKILL.md`.

> ### THE LAW
> From `ANALYSIS.md`, produce **exactly two** asset prompts, as **two separate
> files**:
> 1. `ASSETS-VISUAL.md` — **images + logos** (for an image generator).
> 2. `ASSETS-SOUND.md` — **music + sound effects** (for an audio generator).
>
> Nothing else. No video clips. No voiceover. Two files, never merged.

Each file is **itself a prompt** — copy-paste ready into an AI that can generate
that medium. It is not a description *of* a prompt.

---

## 1. `ASSETS-VISUAL.md` — the visual-asset prompt

Request the **images and logos** the reference needs.

**What to include:**
| Category | What | Notes |
|---|---|---|
| Backgrounds / plates | full-frame backdrops, textures | aspect = the reference's aspect |
| Illustrations | icons, spot art, diagrams | match the reference's style |
| Transparent images | PNG/alpha cut-outs, caption PNGs | mark "transparent background" |
| Logos | wordmark + mark | in the reference's measured palette |
| Still elements | any still the reference uses | charts, cards, badges |

**How to write each item:** a one-line spec with
- **what it is**,
- **size / aspect**,
- **palette** (hex sampled in `ANALYSIS.md`),
- **style keywords** (from the style line, e.g. "cinematic, modern, clean,
  premium"),
- **transparent background?** yes/no.

**Example item:**
> `hero-bg-01` — dark-navy radial backdrop with soft blue light streaks.
> 1920×1080. Palette `#0A1428 / #1E4FD8 / #7FB2FF`. Style: cinematic, modern,
> clean, premium. Opaque.

---

## 2. `ASSETS-SOUND.md` — the sound prompt

Request the **music and sound effects** the reference needs.

**What to include:**
| Category | What | Notes |
|---|---|---|
| Music | bed tracks | mood, BPM, instrumentation, structure |
| Music | stings / risers | where they land |
| SFX | whooshes, hits, clicks | the exact cue time from the beat map |
| SFX | UI / tech sounds | clicks, toggles, data ticks |
| Ambience | room / crowd / texture | if the reference has it |

**How to write each item:**
- **what it is**,
- **where it lands** (cue time from the beat map),
- **duration**,
- **character** (warm/cold, soft/hard, rising/falling),
- for music: **mood, BPM, instrumentation, structure** (intro/build/drop/out).

**Example item:**
> `sfx-whoosh-01` — a bright rising whoosh. Lands at **00:04.2**, 0.6 s. Cold,
> fast, sweeping up.
>
> `music-bed-01` — modern corporate-electronic bed. **96 BPM**, soft synth pads
> + a light four-on-the-floor, subtle build at 0:30. Matches the reference's
> −14 LUFS bed.

---

## 3. What must NOT be in either file

- **No video clips.** (The build makes motion from the visual assets + the edit.)
- **No voiceover / A-roll.** (That comes from the user — Stage 5.)
- **No code components.** (If the reference needs an interactive UI, that is a
  build-time component, not an asset prompt.)
- **No merging.** Two files, two media, two generators.

---

## 4. Provenance & honesty

- State the palette as **measured hex** (from `ANALYSIS.md`), not invented.
- Do not name the reference's brand, product or logo text in the prompt — request
  the **form** ("a wordmark in this palette"), never the source's actual mark.
- If a cue is inferred, label it **inferred**.

---

## 5. Checklist before you send them

- [ ] Exactly two files exist: `ASSETS-VISUAL.md`, `ASSETS-SOUND.md`.
- [ ] Visual covers **images + logos**; sound covers **music + SFX**.
- [ ] Every item has palette (visual) or cue time (sound).
- [ ] No video clips, no voiceover, no code.
- [ ] Both are copy-paste ready.
