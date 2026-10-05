# ASSETS-SOUND — "Blue Glass" portfolio reel

> A **complete, ready-to-paste example** of `ASSETS-SOUND.md`. Copy this shape for
> any build: replace the values with the ones measured in `ANALYSIS.md` (the beat
> map gives every cue time; the audio map gives the loudness and BPM). This file
> is **itself a prompt** — hand it straight to the audio generator.

You are an AI agent with **audio generation**. Produce every audio asset below
and return **ONE zip file** (`sound-assets.zip`) containing all outputs, organised
exactly as the deliverable tree shows. Use every value given exactly as written.
Do not ask questions. Do not generate voiceover — the user supplies the A-roll
separately.

---

## Deliverable — return ONE zip, containing MULTIPLE zips inside

```
sound-assets.zip                     ← the ONE zip you return
├── MANIFEST.md                      ← the only loose file
├── music.zip                        ← section 1 outputs
└── sfx.zip                          ← section 2 outputs
```

No loose audio files — `MANIFEST.md` is the only loose file. The manifest lists
every track, its length, and the beat it serves.

---

## 1. Music — generate (1) → `music/`

1. **Reel bed** — 31 s, 95 BPM, deliver WAV + MP3 → `music/reel_bed.*`
   Generate a calm, premium electronic bed. Soft sustained synth pad under a light
   piano motif and a very subtle pulse. Steady and unhurried, with a gentle lift
   at 20 s that settles by 27 s. No vocals, no drums, no big drops. Master to
   **−14 LUFS integrated** (matching the reference).

## 2. Sound effects — generate (5) → `sfx/`

Short WAV files, clean, no reverb unless stated. Each is timed to a beat from the
analysis.

1. `tick_text_land.wav` — **lands at 0:02.4**, 0.1 s. A single soft UI tick:
   clean, quiet, high-frequency.
2. `whoosh_card_expand.wav` — **lands at 0:08.0**, 0.4 s. A smooth airy whoosh,
   soft and low-energy, no pitch sweep up.
3. `pop_badge.wav` — **lands at 0:16.5**, 0.15 s. A clean bright UI pop, rounded,
   short.
4. `swipe_message.wav` — **lands at 0:21.2**, 0.2 s. A soft tactile swipe/blip,
   quiet, as a message bubble arrives.
5. `impact_finale.wav` — **lands at 0:30.0**, 1.2 s. A low soft cinematic impact
   with a gentle tail — warm, not aggressive.

---

## Acceptance checks before you return the zip

- Sections 1 and 2 are both present.
- Every value given was used exactly (BPM, lengths, loudness, cue times).
- Every SFX file is named as listed and lands on its stated beat.
- The music is delivered as WAV **and** MP3.
- The zip contains **multiple zips** — no loose audio files except `MANIFEST.md`.
- `MANIFEST.md` lists every track, its length, and the beat it serves.
- The zip contains **no** voiceover.
