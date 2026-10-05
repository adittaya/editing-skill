#!/usr/bin/env python3
"""
contact_sheet.py — render the mandatory RENDER GATE contact sheets in three
variants (V1 Classic Grid, V2 Storyboard Filmstrip, V3 Pro QC Sheet) from a
video, so the user can pick one before the full render.

Usage:
    python contact_sheet.py VIDEO [--out DIR] [--variant all|v1|v2|v3] [--fps 1]

Deps: ffmpeg (system, or `pip install imageio-ffmpeg`), Pillow.
Prints the paths it wrote. No network. No side effects beyond --out.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile
from collections import Counter

# ---------------------------------------------------------------- ffmpeg
def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found. Install it, or `pip install imageio-ffmpeg`.")

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def probe(exe, video):
    """Parse `ffmpeg -i` stderr (imageio-ffmpeg ships ffmpeg, not ffprobe)."""
    err = run([exe, "-i", video]).stderr
    w = h = None; fps = 0; dur = 0.0
    m = re.search(r"(\d{2,5})x(\d{2,5})", err)
    if m:
        w, h = int(m.group(1)), int(m.group(2))
    m = re.search(r"([0-9.]+)\s*fps", err)
    if m:
        fps = round(float(m.group(1)), 2)
    m = re.search(r"Duration:\s*(\d+):(\d+):([0-9.]+)", err)
    if m:
        dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return {"w": w, "h": h, "fps": fps, "duration": dur}

def scene_cuts(exe, video):
    """Return cut times (seconds) via ffmpeg scene detection."""
    p = run([exe, "-i", video, "-filter:v",
             "select='gt(scene,0.3)',showinfo", "-f", "null", "-"])
    return sorted({round(float(m), 2)
                   for m in re.findall(r"pts_time:([0-9.]+)", p.stderr)})

def extract_frames(exe, video, fps, outdir):
    os.makedirs(outdir, exist_ok=True)
    run([exe, "-y", "-v", "error", "-i", video, "-vf", f"fps={fps}",
         os.path.join(outdir, "f%05d.jpg")])
    return sorted(os.path.join(outdir, f) for f in os.listdir(outdir)
                  if f.endswith(".jpg"))

# ---------------------------------------------------------------- helpers
def dominant(path, n=5):
    from PIL import Image
    im = Image.open(path).convert("RGB").resize((80, 80))
    q = im.quantize(colors=n).convert("RGB")
    counts = Counter(q.getdata())
    return ["#%02x%02x%02x" % c for c, _ in counts.most_common(n)]

def thumb(path, width):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    h = max(1, int(im.height * width / im.width))
    return im.resize((width, h))

# ---------------------------------------------------------------- variants
INK, MUTE, LINE, ACCENT, BG = (29,29,31), (110,110,115), (222,222,224), (0,113,227), (255,255,255)

def label(draw, xy, text, fill=INK, size=13):
    from PIL import ImageFont
    try:
        f = ImageFont.truetype("DejaVuSans.ttf", size)
    except Exception:
        f = ImageFont.load_default()
    draw.text(xy, text, fill=fill, font=f)

def v1_grid(frames, fps, info, out):
    from PIL import Image, ImageDraw
    cols, tw, pad = 6, 300, 16
    th = thumb(frames[0], tw).height
    rows = (len(frames) + cols - 1) // cols
    W = cols * tw + (cols + 1) * pad
    H = 70 + rows * (th + 26) + pad
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    label(d, (pad, 18), "CONTACT SHEET  V1 - CLASSIC GRID", INK, 20)
    label(d, (pad, 44), f"{os.path.basename(info['name'])}  |  {len(frames)} frames @ {fps} fps", MUTE, 12)
    for i, fr in enumerate(frames):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + pad), 70 + r * (th + 26)
        im.paste(thumb(fr, tw), (x, y))
        d.rectangle([x, y, x + tw, y + th], outline=LINE)
        label(d, (x, y + th + 4), f"{i/fps:5.1f}s", MUTE, 12)
    im.save(out); return out

def v2_filmstrip(frames, fps, cuts, info, out):
    from PIL import Image, ImageDraw
    cols, tw, pad = 4, 420, 18
    th = thumb(frames[0], tw).height
    rows = (len(frames) + cols - 1) // cols
    W = cols * tw + (cols + 1) * pad
    H = 96 + rows * (th + 46) + pad
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    label(d, (pad, 16), "CONTACT SHEET  V2 - STORYBOARD FILMSTRIP", INK, 20)
    label(d, (pad, 42), f"{os.path.basename(info['name'])}  |  {len(frames)} frames  |  {len(cuts)} scene cuts", MUTE, 12)
    # time ruler
    rx0, rx1, ry = pad, W - pad, 78
    d.line([rx0, ry, rx1, ry], fill=LINE)
    dur = max(info["duration"], len(frames) / fps, 1)
    for t in range(0, int(dur) + 1):
        x = rx0 + (rx1 - rx0) * t / dur
        d.line([x, ry - 4, x, ry + 4], fill=LINE)
        if t % max(1, int(dur // 12) or 1) == 0:
            label(d, (x - 10, ry - 20), f"{t}s", MUTE, 11)
    for ct in cuts:
        x = rx0 + (rx1 - rx0) * ct / dur
        d.line([x, ry - 8, x, ry + 8], fill=ACCENT)
    for i, fr in enumerate(frames):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + pad), 96 + r * (th + 46)
        im.paste(thumb(fr, tw), (x, y))
        d.rectangle([x, y, x + tw, y + th], outline=LINE)
        label(d, (x, y + th + 5), f"{i/fps:5.1f}s", INK, 12)
        label(d, (x + 46, y + th + 5), "| scene cut" if any(abs(ct - i/fps) < 0.5 for ct in cuts) else "", ACCENT, 12)
    im.save(out); return out

def v3_qc(frames, fps, cuts, info, out):
    from PIL import Image, ImageDraw
    cols, tw, pad = 5, 320, 18
    th = thumb(frames[0], tw).height
    rows = (len(frames) + cols - 1) // cols
    pal = dominant(frames[len(frames)//2])
    W = cols * tw + (cols + 1) * pad
    H = 168 + rows * (th + 30) + pad
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    label(d, (pad, 14), "CONTACT SHEET  V3 - PRO QC SHEET", INK, 20)
    dur = max(info["duration"], len(frames) / fps, 1)
    asl = round(dur / max(1, len(cuts)), 2)
    summary = (f"{os.path.basename(info['name'])}  |  {info['w']}x{info['h']}  {info['fps']}fps  |  "
               f"dur {dur:.1f}s  |  shots {len(cuts)}  |  ASL {asl}s  |  {len(frames)} frames")
    label(d, (pad, 42), summary, MUTE, 12)
    # palette strip
    sw, sx = 60, pad
    for c in pal:
        d.rectangle([sx, 66, sx + sw, 90], fill=tuple(int(c[i:i+2], 16) for i in (1, 3, 5)))
        sx += sw + 6
    label(d, (sx + 6, 72), "sampled palette", MUTE, 11)
    for i, fr in enumerate(frames):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + pad), 168 + r * (th + 30)
        im.paste(thumb(fr, tw), (x, y))
        d.rectangle([x, y, x + tw, y + th], outline=LINE)
        # safe-zone overlay (universal action-safe ~ centre 90%)
        mx, my = int(tw * 0.05), int(th * 0.05)
        d.rectangle([x + mx, y + my, x + tw - mx, y + th - my], outline=ACCENT)
        tc = f"{i/fps:5.1f}s"
        d.rectangle([x, y, x + 54, y + 16], fill=INK)
        label(d, (x + 4, y + 2), tc, (255, 255, 255), 11)
        if any(abs(ct - i/fps) < 0.5 for ct in cuts):
            d.rectangle([x + tw - 60, y, x + tw, y + 16], fill=ACCENT)
            label(d, (x + tw - 56, y + 2), "CUT", (255, 255, 255), 11)
    im.save(out); return out

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default="contact_sheets")
    ap.add_argument("--variant", default="all", choices=["all", "v1", "v2", "v3"])
    ap.add_argument("--fps", type=float, default=1)
    a = ap.parse_args()

    exe = ffmpeg_exe()
    info = probe(exe, a.video); info["name"] = os.path.basename(a.video)
    if not info.get("w"):
        sys.exit("could not probe video")
    os.makedirs(a.out, exist_ok=True)
    cuts = scene_cuts(exe, a.video)
    with tempfile.TemporaryDirectory() as td:
        frames = extract_frames(exe, a.video, a.fps, td)
        if not frames:
            sys.exit("no frames extracted")
        written = []
        if a.variant in ("all", "v1"):
            written.append(v1_grid(frames, a.fps, info, os.path.join(a.out, "contact_sheet_V1_grid.png")))
        if a.variant in ("all", "v2"):
            written.append(v2_filmstrip(frames, a.fps, cuts, info, os.path.join(a.out, "contact_sheet_V2_filmstrip.png")))
        if a.variant in ("all", "v3"):
            written.append(v3_qc(frames, a.fps, cuts, info, os.path.join(a.out, "contact_sheet_V3_qc.png")))
    for w in written:
        print("wrote", w)
    print(f"frames={len(frames)} cuts={len(cuts)} dur={info['duration']:.1f}s")

if __name__ == "__main__":
    main()
