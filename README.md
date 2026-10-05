# Editing Skill — give it a reference, get a rebuilt edit

A single, self-contained **editing skill** for an AI agent. Hand it **one
reference** — a video or a contact sheet — and it:

1. **Extracts that reference at maximum accuracy** — every frame, every element,
   zoomed in, verified.
2. Writes the extraction up as **`ANALYSIS.md`**.
3. Writes **two separate asset prompts** — `ASSETS-VISUAL.md` (images + logos)
   and `ASSETS-SOUND.md` (music + SFX).
4. Asks **you** for the **A-roll** (voiceover / talking avatar / podcast, per the
   contact sheet).
5. **Rebuilds the edit** to match — with the full advanced-feature toolset — then
   QAs and delivers.

```
REFERENCE -> EXTRACT (100%) -> ANALYSIS.md
                            -> ASSETS-VISUAL.md   (images + logos)
                            -> ASSETS-SOUND.md    (music + SFX)
YOU       -> A-ROLL (voiceover / avatar / podcast, per the contact sheet)
                            -> BUILD -> QA -> FINISHED EDIT
```

## The whole point: accuracy first
The skill never guesses from a few thumbnails. It pulls **all** frames, **zooms
into every element**, reads text **verbatim**, measures the **palette**, the
**cuts** and the **loudness**, and then **verifies** before moving on. A
reference read at 100% is a build that is right.

## What it asks you for
**One thing: the reference.** Everything else is derived. The A-roll comes later
— only after the extraction is done and the contact sheet says which shots need a
speaker.

## The two asset prompts are always two files
- **`ASSETS-VISUAL.md`** — images + logos (for an image generator).
- **`ASSETS-SOUND.md`** — music + sound effects (for an audio generator).

**Never merged.** No video clips, no voiceover in either.

## Folder structure
```
editing-skill/
  SKILL.md                     <- THE editing skill (read this first)
  AGENT-PROMPT.md              <- one copy-paste prompt that runs the whole flow
  README.md                    <- this file
  references/
    EXTRACTION-PROTOCOL.md     <- the 100%-accuracy extraction checklist
    ADVANCED-FEATURE-USE-CASES.md <- the full advanced-feature catalogue
    ASSET-PROMPTS.md           <- the two-prompt spec (visual + sound)
    CONTACT-SHEET-FORMAT.md    <- how a contact sheet is read and built
    EDIT-MAP.md                <- edit type -> fast path
    THINKING-SYSTEM.md         <- the planning stack behind the build
  templates/
    ANALYSIS.template.md
    ASSETS-VISUAL.template.md
    ASSETS-SOUND.template.md
    A-ROLL-REQUEST.template.md
  tools/
    extract.py  analyze.py  contact_sheet.py  qa_check.py
```

## How to use it
**With an AI agent that can read this repo:** paste `AGENT-PROMPT.md` and attach
your reference. The agent runs the whole flow.

**As a skill:** point the agent at `SKILL.md`; it is the complete skill. The
`references/`, `templates/` and `tools/` folders give it the power to execute
every stage.

## Install the tools
```
pip install imageio-ffmpeg pillow numpy
```

## The laws the skill enforces
- **Extraction Law** — extract everything, zoom, verify; never guess.
- **Two-Prompt Law** — two asset prompts, always separate; visual + sound only.
- **A-Roll Law** — the user supplies the A-roll per the contact sheet.
- **Text Law** — on-screen text maps the visual; generic subtitles are never the
  default.
- **Palette & Gradient Law** · **Camera Law** · **Sentence Law** ·
  **No-Metadata Law** · **No-Clank Law** · **Asset & Clearance Protocol**.
- **Gates** — Extraction, Asset, A-Roll, Render, QA.

## Honesty
Where something is measurable it is stated as measured; where it is inferred it
is labelled **inferred**. The skill never invents a font, a technique or a claim.
