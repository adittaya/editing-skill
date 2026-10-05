# tools/ — the runnable helpers

Four small, dependency-light tools. No network. They write only where you tell
them to.

| Tool | What it does | Stage |
|---|---|---|
| `extract.py` | Pull **every frame** (or a dense pass), write a time-stamped manifest, and cut each frame into **zoom tiles**. | 2 |
| `analyze.py` | Measure **loudness**, **cuts** (scene changes) and **palette** (dominant hex). | 2 |
| `contact_sheet.py` | Build the **V1 / V2 / V3** contact sheets from a video. | 3, 6 |
| `qa_check.py` | Audit a project against the QA list; write `EDIT-QA.md`. | 7 |

## Setup
```
pip install imageio-ffmpeg pillow numpy
```
`ffmpeg` is picked up from your PATH, or from `imageio-ffmpeg` if it is not
installed system-wide. No system ffmpeg needed.

## Extract (Stage 2)
```
python tools/extract.py probe   REF.mp4
python tools/extract.py frames  REF.mp4 --out frames --fps 2 --dense-fps 10
python tools/extract.py tiles   frames  --grid 3 --out frames/tiles
```
- `probe` prints duration, resolution, fps.
- `frames` writes `frames/f_000001.jpg …` plus `manifest.csv` (frame → time).
- `--dense-fps 10` also runs a dense pass into `frames/dense/`.
- `tiles` splits every frame into a grid so small text is readable — **zoom
  before you conclude.**

## Analyze (Stage 2)
```
python tools/analyze.py loudness REF.mp4
python tools/analyze.py cuts     REF.mp4 --thresh 0.30
python tools/analyze.py palette  frames  --n 6
```

## Contact sheets (Stages 3 & 6)
```
python tools/contact_sheet.py REF.mp4 --out sheets --variant all --fps 1
```
Writes `V1` (grid), `V2` (upgraded), `V3` (filmstrip/QC). Show them, then ask
before rendering.

## QA (Stage 7)
```
python tools/qa_check.py PROJECT_DIR --video build.mp4 --out EDIT-QA.md
```
