# ASSETS-SOUND — <project>

> This file **is a prompt.** Hand it straight to an audio generator. Fill every
> `<...>` from `ANALYSIS.md` (the beat map gives every cue time; the audio map
> gives loudness and BPM). See `examples/EXAMPLE-ASSETS-SOUND.md` for a complete
> worked example — **match that depth**: exact BPM, exact lengths, exact cue
> times, one executable brief per track.

You are an AI agent with **audio generation**. Produce every audio asset below and
return **ONE zip file** (`sound-assets.zip`) containing all outputs, organised
exactly as the deliverable tree shows. Use every value given exactly as written.
Do not ask questions. Do not generate voiceover — the user supplies the A-roll
separately.

---

## Deliverable — return ONE zip, containing MULTIPLE zips inside

```
sound-assets.zip
├── MANIFEST.md            ← the only loose file
├── music.zip              ← section 1 outputs
└── sfx.zip                ← section 2 outputs
```

`MANIFEST.md` lists every track, its length, and the beat it serves.

---

## 1. Music — generate (<N>) → `music/`

One **executable brief** per track: mood · genre · BPM · length · instrumentation
· energy arc.

1. **<name>** — <length>, <BPM> BPM, deliver WAV + MP3 → `music/<file>.*`
   <brief: mood, instrumentation, structure, the lift/settle points>. No vocals.
   Master to **<LUFS> integrated** (matching the reference).

## 2. Sound effects — generate (<N>) → `sfx/`

One brief per cue, each timed to a beat from the analysis. Short WAV files, clean,
no reverb unless stated.

1. `<file>.wav` — **lands at <time>**, <length>. <brief: type + character>.
2. `<file>.wav` — **lands at <time>**, <length>. <brief>.

---

## Acceptance checks before you return the zip

- Sections 1 and 2 are both present.
- Every value given was used exactly (BPM, lengths, loudness, cue times).
- Every SFX file is named as listed and lands on its stated beat.
- The music is delivered as WAV **and** MP3.
- The zip contains **multiple zips** — no loose audio files except `MANIFEST.md`.
- `MANIFEST.md` lists every track, its length, and the beat it serves.
- The zip contains **no** voiceover.
