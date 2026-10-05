#!/usr/bin/env python3
"""
analyze.py - measure a reference (Stage 2, passes B/C/F).

Measures, from a video:
  * loudness      (integrated mean/max via ffmpeg volumedetect)
  * cuts          (scene-change list via ffmpeg select='gt(scene,..)')
  * palette       (dominant hex from extracted frames)

Usage:
    python analyze.py loudness VIDEO
    python analyze.py cuts     VIDEO [--thresh 0.30]
    python analyze.py palette  FRAMES_DIR [--n 6]

Deps: ffmpeg (system, or `pip install imageio-ffmpeg`), Pillow, numpy.
No network. Read-only.
"""
import argparse, os, re, shutil, subprocess, sys

def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found. Install with: pip install imageio-ffmpeg")

def loudness(video):
    exe = ffmpeg_exe()
    p = subprocess.run([exe, "-i", video, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    out = p.stderr
    mean = re.search(r"mean_volume:\s*(-?\d+(?:\.\d+)?) dB", out)
    mx = re.search(r"max_volume:\s*(-?\d+(?:\.\d+)?) dB", out)
    print(f"mean_volume: {mean.group(1) if mean else '?'} dB")
    print(f"max_volume : {mx.group(1) if mx else '?'} dB")
    print("(integrated LUFS: run ffmpeg -af loudnorm=I=-14:print_format=summary for the exact figure)")

def cuts(video, thresh):
    exe = ffmpeg_exe()
    vf = f"select='gt(scene,{thresh})',showinfo"
    p = subprocess.run([exe, "-i", video, "-vf", vf, "-f", "null", "-"],
                       capture_output=True, text=True)
    times = [float(m) for m in re.findall(r"pts_time:([\d.]+)", p.stderr)]
    print(f"cuts @ scene>{thresh}: {len(times)}")
    for t in times:
        print(f"  {t:8.2f}s")

def palette(frames_dir, n):
    from PIL import Image
    import numpy as np
    frames = sorted(f for f in os.listdir(frames_dir)
                    if f.endswith((".jpg", ".png")) and not f.startswith("tile"))
    if not frames:
        sys.exit(f"no frames in {frames_dir}")
    step = max(1, len(frames)//40)
    from collections import Counter
    cnt = Counter()
    for name in frames[::step]:
        im = Image.open(os.path.join(frames_dir, name)).convert("RGB").resize((160, 90))
        a = (np.array(im)//24*24).reshape(-1, 3)
        for px in a:
            cnt[(int(px[0]), int(px[1]), int(px[2]))] += 1
    print(f"dominant palette ({len(frames)} frames sampled):")
    for (r, g, b), c in cnt.most_common(n):
        print(f"  #{r:02X}{g:02X}{b:02X}   {100*c/sum(cnt.values()):5.1f}%")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["loudness", "cuts", "palette"])
    ap.add_argument("target")
    ap.add_argument("--thresh", type=float, default=0.30)
    ap.add_argument("--n", type=int, default=6)
    a = ap.parse_args()
    if a.cmd == "loudness": loudness(a.target)
    elif a.cmd == "cuts":   cuts(a.target, a.thresh)
    elif a.cmd == "palette":palette(a.target, a.n)

if __name__ == "__main__":
    main()
