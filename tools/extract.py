#!/usr/bin/env python3
"""
extract.py - the EXTRACTION tool for the editing skill (Stage 2).

Pulls EVERY frame of a reference (or a dense pass), writes a time-stamped
manifest, and can cut each frame into zoom tiles so small text / fine UI is
readable. Accuracy is the goal: never analyse from a few thumbnails.

Usage:
    python extract.py probe   VIDEO
    python extract.py frames  VIDEO --out DIR [--fps 2] [--dense-fps 0]
    python extract.py tiles   FRAMES_DIR [--grid 2] [--out DIR]

Deps: ffmpeg (system, or `pip install imageio-ffmpeg`), Pillow.
No network. Writes only under --out.
"""
import argparse, csv, os, re, shutil, subprocess, sys

def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found. Install with: pip install imageio-ffmpeg")

def probe(video):
    exe = ffmpeg_exe()
    p = subprocess.run([exe, "-i", video], capture_output=True, text=True)
    err = p.stderr
    info = {"file": os.path.basename(video), "duration_s": None,
            "width": None, "height": None, "fps": None}
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", err)
    if m:
        h, mi, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
        info["duration_s"] = round(h*3600 + mi*60 + s, 2)
    m = re.search(r"Video:.*?,\s*(\d{2,5})x(\d{2,5})", err)
    if m:
        info["width"], info["height"] = int(m.group(1)), int(m.group(2))
    m = re.search(r"(\d+(?:\.\d+)?)\s*fps", err)
    if m:
        info["fps"] = float(m.group(1))
    return info

def extract_frames(video, out, fps, prefix="f"):
    exe = ffmpeg_exe()
    os.makedirs(out, exist_ok=True)
    pat = os.path.join(out, f"{prefix}_%06d.jpg")
    cmd = [exe, "-y", "-i", video, "-vf", f"fps={fps}", "-q:v", "2", pat]
    subprocess.run(cmd, capture_output=True, text=True)
    frames = sorted(f for f in os.listdir(out) if f.startswith(prefix) and f.endswith(".jpg"))
    rows = []
    for i, name in enumerate(frames, 1):
        t = round((i - 1) / fps, 3)
        rows.append({"file": name, "t_sec": t, "t_hms": hms(t)})
    with open(os.path.join(out, "manifest.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "t_sec", "t_hms"])
        w.writeheader(); w.writerows(rows)
    return frames, rows

def hms(t):
    m, s = divmod(t, 60)
    return f"{int(m):02d}:{s:05.2f}"

def make_tiles(frames_dir, grid, out):
    from PIL import Image
    os.makedirs(out, exist_ok=True)
    frames = sorted(f for f in os.listdir(frames_dir)
                    if f.endswith(".jpg") and not f.startswith("tile"))
    n = 0
    for name in frames:
        im = Image.open(os.path.join(frames_dir, name))
        W, H = im.size
        tw, th = W // grid, H // grid
        base = os.path.splitext(name)[0]
        for r in range(grid):
            for c in range(grid):
                box = (c*tw, r*th, (c+1)*tw if c < grid-1 else W,
                       (r+1)*th if r < grid-1 else H)
                im.crop(box).save(os.path.join(out, f"{base}_r{r}c{c}.jpg"), quality=92)
                n += 1
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["probe", "frames", "tiles"])
    ap.add_argument("target")
    ap.add_argument("--out", default=None)
    ap.add_argument("--fps", type=float, default=2.0)
    ap.add_argument("--dense-fps", type=float, default=0.0,
                    help="also run a full dense pass at this fps (e.g. 10)")
    ap.add_argument("--grid", type=int, default=2, help="tile grid (2 = 2x2, 3 = 3x3)")
    a = ap.parse_args()

    if a.cmd == "probe":
        import json
        print(json.dumps(probe(a.target), indent=2)); return

    if a.cmd == "frames":
        out = a.out or "frames"
        frames, rows = extract_frames(a.target, out, a.fps, prefix="f")
        print(f"[extract] {len(frames)} frames @ {a.fps} fps -> {out}")
        print(f"[extract] manifest -> {os.path.join(out,'manifest.csv')}")
        if a.dense_fps and a.dense_fps > a.fps:
            dout = os.path.join(out, "dense")
            df, _ = extract_frames(a.target, dout, a.dense_fps, prefix="d")
            print(f"[extract] {len(df)} dense frames @ {a.dense_fps} fps -> {dout}")
        return

    if a.cmd == "tiles":
        out = a.out or os.path.join(a.target, "tiles")
        n = make_tiles(a.target, a.grid, out)
        print(f"[extract] {n} tiles ({a.grid}x{a.grid}) -> {out}")

if __name__ == "__main__":
    main()
