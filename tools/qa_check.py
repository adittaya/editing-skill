#!/usr/bin/env python3
"""
qa_check.py — the runnable EDIT QA VALIDATOR.

Audits a project folder against the pack's mandatory lists, scores each item
OK / WEAK / MISSING / N/A, proposes an AI re-think fix for anything missing, and
writes EDIT-QA.md.

Usage:
    python qa_check.py PROJECT_DIR [--video build.mp4] [--out EDIT-QA.md]

It looks for, in PROJECT_DIR:
    SOURCE-ANALYSIS.json   CONCEPT.md   ASSETS-PROMPT.md   build.mp4   frames/

Deps: ffmpeg (system, or `pip install imageio-ffmpeg`) for the video analytics.
No network. Read-only on the project; writes only --out.
"""
import argparse, json, os, re, shutil, subprocess, sys

def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe: return exe
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception: return None

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)

# --- each item: (id, category, label, [keywords], mandatory, fix) -----------
# keywords are matched case-insensitively against the project's text artifacts.
F = [
 ("P1","Pipeline","SOURCE-ANALYSIS.json present",["source-analysis"],True,"Run STEP 0 and save SOURCE-ANALYSIS.json."),
 ("P2","Pipeline","CONCEPT.md present",["concept"],True,"Write CONCEPT.md (STEP 1)."),
 ("P3","Pipeline","ASSETS-PROMPT.md present",["assets-prompt","assets prompt"],True,"Write ASSETS-PROMPT.md (STEP 2)."),
 ("P4","Pipeline","Sentence table in CONCEPT",["sentence table","sentence"],True,"Add the sentence table (one row per sentence -> visual -> stressed word -> camera)."),
 ("P5","Pipeline","Camera-track plan",["camera-track","camera track","camera plan"],True,"Add the camera-track plan (READ/EMPHASIZE/REVEAL/FOLLOW/BREATHE)."),
 ("P6","Pipeline","Contact-sheet plan",["contact-sheet","contact sheet"],True,"Add the contact-sheet plan (which V1/V2/V3 variants)."),
 ("P7","Pipeline","Caption style declared",["caption style","caption-style","apple-clean","vox-highlighter","sticker-pop","outline-alpha","karaoke"],True,"Declare a caption style from CAPTION-STYLES.md."),

 ("A1","Advanced","Multi-track timeline",["multi-track","multitrack","v1/v2"],True,"Layer video/audio/effects; plan V1/V2/V3 + A1/A2."),
 ("A2","Advanced","Multi-camera editing",["multi-camera","multicam"],False,"Sync angles and cut on speaker/action where you have multiple angles."),
 ("A3","Advanced","Proxy editing",["proxy"],False,"Cut on proxies on heavy projects, then re-render the same cut list."),
 ("A4","Advanced","Keyframing",["keyfram"],True,"Keyframe every animated property, eased."),
 ("A5","Advanced","Motion tracking",["motion track","tracking","track "],False,"Bind the graphic to the moving object; lowpass the track."),
 ("A6","Advanced","Masking / rotoscoping",["mask","rotoscop"],False,"Isolate the subject frame-by-frame where a reveal/cut-out is needed."),
 ("A7","Advanced","Speed ramping / time remap",["speed ramp","time remap","ramp"],False,"Add a speed curve across the key beat."),
 ("A8","Advanced","Stabilisation / optical flow",["stabili","optical flow"],False,"Warp-stabilise shaky footage; optical flow for slow-mo."),
 ("A9","Advanced","Colour correction",["colour correct","color correct","white balance"],True,"Correct exposure/white balance/contrast FIRST."),
 ("A10","Advanced","Colour grading",["colour grade","color grade","lut","grade"],True,"Apply the look (LUT/film/split-tone) SECOND."),
 ("A11","Advanced","Scopes",["scope","waveform","vectorscope"],False,"Grade by the numbers with waveform/vectorscope/parade."),
 ("A12","Advanced","HDR",["hdr"],False,"HDR only if requested; tone-map to SDR for delivery."),
 ("A13","Advanced","Chroma key",["chroma","green screen","key"],False,"Key on flat green #00B140/blue: despill, choke, light wrap, garbage matte."),
 ("A14","Advanced","Compositing / VFX",["composit","vfx"],False,"Combine layers into one scene where needed."),
 ("A15","Advanced","3D camera tracking",["3d camera","3d track","camera track 3d"],False,"Solve the camera move and place 3D in real footage."),
 ("A16","Advanced","Advanced transitions",["transition","glitch","light leak","grain"],True,"Time a transition/effect to each cut or beat."),
 ("A17","Advanced","Audio: noise reduction / EQ / mix",["noise reduction","eq","duck","mix","loudness"],True,"NR, EQ, sync and multi-track mix; duck music under voice."),
 ("A18","Advanced","AI features",["auto subtitle","auto reframe","scene detection","ai background","ai colour"],False,"Use auto subtitles / AI matte / auto reframe / scene detect where they help."),

 ("M1","Modern","Anchor zoom in / zoom out",["zoom in","zoom out","anchor zoom"],True,"Add an anchor zoom to a detail and a zoom-out reveal."),
 ("M2","Modern","Motion tracing / follow",["motion trac","follow"],False,"Follow the cursor/action with a damped spring."),
 ("M3","Modern","Motion blur (velocity)",["motion blur"],False,"Blur only during fast motion; zero at rest."),
 ("M4","Modern","Bezier easing",["bezier","eas"],True,"Ease every move; curve the path, never linear."),
 ("M5","Modern","Mask / wipe reveal",["wipe","reveal"],False,"Draw-on reveals where a transition needs one."),
 ("M6","Modern","Parallax / 2.5D",["parallax","2.5d"],False,"Layers move at different rates."),
 ("M7","Modern","Freeze frame / hold",["freeze","hold"],False,"Hold on the moment that matters."),
 ("M8","Modern","Kinetic text / word-pop",["word-pop","word pop","kinetic text"],True,"Words appear on the beat; one accent keyword per line."),
 ("M9","Modern","Count-up numbers",["count-up","count up"],False,"Animate every stat to its value on the spoken word."),
 ("M10","Modern","Callouts & arrows",["callout","arrow"],False,"Draw-on annotations pointing at the thing."),
 ("M11","Modern","Readability zoom",["readab"],False,"Any UI text the viewer must read renders >=4% frame height."),
 ("M12","Modern","Cut-on-beat / cut-on-action",["cut on beat","cut-on-beat","beat"],True,"Land cuts on the beat or mid-movement."),
 ("M13","Modern","A sound for every cut",["sound design","sfx","whoosh","sound for every cut"],True,"Give every cut/graphic a sound; silence before the biggest hit."),
 ("M14","Modern","Seamless loop",["loop"],False,"End state = start state for social/web loops."),

 ("L1","Camera Law","One camera wrapper / one move",["one camera","camera wrapper"],True,"Route all camera motion through one wrapper; one move at a time."),
 ("L2","Camera Law","Every zoom has a reason",["read","emphasize","reveal","breathe","follow"],True,"Tag each zoom READ/EMPHASIZE/REVEAL/FOLLOW/BREATHE."),
 ("L3","Camera Law","No cut while zoomed",["cut while zoom","return to rest"],False,"Return to rest or hold before a cut."),

 ("S1","Sentence Law","Every sentence has a visual",["visual narration","sentence law","visual landing"],True,"Bind a visual event to every narration sentence."),
 ("S2","Sentence Law","Visual lands on stressed word",["stressed word","+/-100","+_100"],True,"Land the visual on the stressed word (+/-100 ms)."),

 ("C1","Captions","Styled caption style sheet",["style sheet","font","tracking","leading"],True,"Write the caption style sheet into CONCEPT.md."),
 ("C2","Captions","Transparent / alpha captions",["transparent","alpha","png"],False,"Use transparent PNG / alpha clips where a caption needs no box."),
 ("C3","Captions","Text-behind-subject",["text behind","behind subject"],False,"Composite the text under a clean subject matte."),
 ("C4","Captions","Caption timing (word-level)",["word-level","word level","timing"],True,"Time captions from the word-level JSON; <=2 lines; <=17 chars/s."),

 ("V1","Visual layer","Placements alternated",["placement","cutaway","overlay","behind"],False,"Alternate cutaway / overlay / behind-subject; one event per 6-10s."),
 ("V2","Visual layer","Captions additive, not the layer",["additive"],False,"Captions supplement; the visual still carries the idea."),

 ("R1","Render gate","Contact-sheet variants built",["v1","v2","v3"],True,"Build and present the V1/V2/V3 contact sheets and ask."),
 ("R2","Render gate","Sign-off recorded",["sign-off","signoff","approved"],True,"Get sign-off before the full render."),

 ("E1","Ethics","No fabricated facts",["no invent","verified","verify"],True,"Verify every number/quote; never fabricate."),
 ("E2","Ethics","Recreations labelled",["label","recreation","disclose"],True,"Label every recreation/animation/composite."),

 ("D1","Delivery","Loudness measured",["lufs","true peak","loudness"],True,"Measure integrated LUFS + true peak, don't guess."),
 ("D2","Delivery","Safe zones + captions file",["safe zone","srt","vtt"],True,"Check safe zones and ship a caption sidecar."),

 ("CF1","Camera","Zoom in / anchor zoom",["zoom in","anchor zoom"],True,"Anchor-zoom a key detail (origin on target), return to rest before the cut."),
 ("CF2","Camera","Zoom out / reveal",["zoom out"],True,"Pull back for context after a detail; wide<->detail rhythm."),
 ("CF3","Camera","Character / face zoom",["face zoom","character zoom","push to face"],False,"Push in to a face for emotion (the character-zoom beat)."),
 ("CF4","Camera","Push in / pull out (dolly)",["push in","pull out","dolly"],False,"Move the camera, not the lens."),
 ("CF5","Camera","Rack focus / focus pull",["rack focus","focus pull"],False,"Shift focus between subjects in-frame."),
 ("CF6","Camera","Pan / tilt / orbit",["pan","tilt","orbit"],False,"Reframe or arc the camera."),
 ("CF7","Camera","Whip pan / snap zoom",["whip","snap zoom","crash zoom"],False,"Fast pan or sudden zoom for a punch/transition."),
 ("CF8","Camera","Dolly zoom (Vertigo)",["dolly zoom","vertigo"],False,"Dolly + counter-zoom for disorientation."),
 ("CF9","Camera","Parallax move",["parallax"],False,"Layered depth as the camera travels."),
 ("CF10","Camera","Handheld vs stabilised",["handheld"],False,"Choose energy vs calm deliberately."),
 ("CF11","Camera","Drone / aerial",["drone","aerial"],False,"Aerial coverage where it serves."),
 ("CF12","Camera","Slow reveal / pull-back reveal",["pull-back","slow reveal"],False,"Start tight, reveal context."),

 ("T1","Transitions","Match cut / J-cut / L-cut",["match cut","j-cut","l-cut"],False,"Use audio-lead/trail and match cuts."),
 ("T2","Transitions","Dissolve / dip to black",["dissolve","dip to black"],False,"Signal a temporal/thematic shift."),
 ("T3","Transitions","Whip / zoom / blur transition",["blur transition","zoom transition","whip transition"],False,"Blend the cut with a camera move + blur."),
 ("T4","Transitions","Mask / wipe / iris",["wipe","iris"],False,"Shape-based transitions where they fit."),
 ("T5","Transitions","Light leak / film burn",["light leak","film burn"],False,"Organic transition accents."),
 ("T6","Transitions","Glitch / RGB split",["glitch","rgb split"],False,"Kinetic accent, short windows only."),

 ("SP1","Speed","Reverse",["reverse"],False,"Backwards reveal/reset."),
 ("SP2","Speed","Timelapse / hyperlapse",["timelapse","hyperlapse"],False,"Compress long time."),
 ("SP3","Speed","Strobe / posterize (12fps)",["12fps","posterize","strobe"],False,"The hand-animated stutter where it fits."),

 ("MO1","Motion","Shape morph",["morph"],False,"Morph one shape into another."),
 ("MO2","Motion","Puppet / rig animation",["puppet","rig"],False,"Character/pin animation where needed."),

 ("CO1","Colour","Colour match / skin-tone protection",["colour match","color match","skin tone"],False,"Match shots; protect skin."),
 ("CO2","Colour","LOG/HDR conversion + tone-map",["log","tone map"],False,"Convert LOG, tone-map HDR to SDR."),
 ("CO3","Colour","Vignette / grain / halation",["vignette","halation","grain"],False,"Finish textures."),

 ("VX1","VFX","3D camera tracking / matchmove",["3d camera","matchmove"],False,"Solve the move, place 3D in real footage."),
 ("VX2","VFX","Set extension / screen replacement",["set extension","screen replacement"],False,"Extend or replace in-scene surfaces."),
 ("VX3","VFX","Object removal / clean plate",["object removal","clean plate","clone"],False,"Remove rigs/objects."),
 ("VX4","VFX","Particles / shaders",["particle","shader"],False,"Procedural effects where they serve."),

 ("AU1","Audio","Sound design / SFX / foley",["sound design","sfx","foley"],True,"Design the sound; a sound for every cut."),
 ("AU2","Audio","Music beat mapping",["beat map","bpm"],False,"Drive cuts from the track's BPM."),
 ("AU3","Audio","Dialogue editing / VO",["dialogue","voiceover","adr"],False,"Clean dialogue; place VO."),

 ("WF1","Workflow","Nesting / pre-comp / adjustment layers",["nesting","pre-comp","adjustment layer"],False,"Structure the timeline properly."),
 ("WF2","Workflow","Batch export / render queue",["batch export","render queue"],False,"Deliver every ratio from one master."),
]

def read_text(path):
    try: return open(path, encoding="utf-8", errors="ignore").read().lower()
    except Exception: return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?", default=".")
    ap.add_argument("--video", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    P = os.path.abspath(a.project)
    out = a.out or os.path.join(P, "EDIT-QA.md")

    # gather all text artifacts in the project
    text = ""
    for root, _, files in os.walk(P):
        if "/frames" in root or root.endswith("frames"): continue
        for f in files:
            if f.lower().endswith((".md", ".json", ".txt")):
                text += "\n" + read_text(os.path.join(root, f))

    # video analytics
    vinfo = {}
    video = a.video or next((os.path.join(P, f) for f in os.listdir(P)
                             if f.lower().endswith(".mp4")), None) if os.path.isdir(P) else None
    exe = ffmpeg_exe()
    if video and exe and os.path.exists(video):
        err = run([exe, "-i", video]).stderr
        m = re.search(r"(\d{2,5})x(\d{2,5})", err)
        if m: vinfo["res"] = m.group(0)
        m = re.search(r"Duration:\s*(\d+):(\d+):([0-9.]+)", err)
        if m: vinfo["dur"] = int(m.group(1))*3600+int(m.group(2))*60+float(m.group(3))
        cuts = run([exe,"-i",video,"-filter:v","select='gt(scene,0.3)',showinfo","-f","null","-"]).stderr
        vinfo["cuts"] = len(re.findall(r"pts_time:", cuts))
        l = run([exe,"-i",video,"-af","ebur128=peak=true","-f","null","-"]).stderr
        mi = re.search(r"I:\s*(-?[0-9.]+)\s*LUFS", l)
        if mi: vinfo["lufs"] = float(mi.group(1))
        tp = re.findall(r"Peak:\s*(-?[0-9.]+)", l)
        if tp: vinfo["tp"] = float(tp[-1])

    # file-presence items are checked by existence, not by keyword
    files = {f.lower() for f in os.listdir(P)} if os.path.isdir(P) else set()
    present = {
        "P1": any(f.endswith("source-analysis.json") or f=="source-analysis.json" for f in files),
        "P2": any(f.endswith("concept.md") for f in files),
        "P3": any(f.endswith("assets-prompt.md") or f.endswith("assets_prompt.md") for f in files),
    }
    rows=[]; ok=weak=miss=na=0
    for i,(fid,cat,lab,kws,mand,fix) in enumerate(F):
        if fid in present:
            hit = present[fid]
        else:
            hit = any(k in text for k in kws) if kws else False
        # file-presence items are OK only if the file exists
        verdict = "OK" if hit else ("MISSING" if mand else "N/A")
        if not hit and not mand: verdict="N/A"
        if hit: ok+=1
        elif mand: miss+=1
        else: na+=1
        rows.append((fid,cat,lab,verdict,mand,fix))

    needed = ok+miss
    score = round(100*ok/needed,1) if needed else 0.0
    L=[]
    L.append(f"# EDIT-QA - {os.path.basename(P)}\n")
    L.append(f"## Score: {ok}/{needed} = {score}%  |  MISSING: {miss}  |  N/A: {na}\n")
    if vinfo:
        L.append("## Video analytics\n")
        for k,v in vinfo.items(): L.append(f"- **{k}**: {v}")
        if vinfo.get("dur") and vinfo.get("cuts"):
            L.append(f"- **ASL**: {round(vinfo['dur']/max(1,vinfo['cuts']),2)} s")
        L.append("")
    L.append("## PASS 1 - Audit\n")
    L.append("| # | Category | Item | Verdict |")
    L.append("|---|---|---|---|")
    for fid,cat,lab,v,mand,fix in rows:
        L.append(f"| {fid} | {cat} | {lab}{' *' if mand else ''} | {v} |")
    L.append("\n`*` = mandatory for most builds.\n")
    L.append("## PASS 2 - AI re-think (fixes for what is missing)\n")
    L.append("| Item | What to add | How | Why it improves the video |")
    L.append("|---|---|---|---|")
    for fid,cat,lab,v,mand,fix in rows:
        if v=="MISSING":
            L.append(f"| {lab} | {fix} | see the skill's feature section | closes a gap the viewer would otherwise feel |")
    if not any(r[3]=="MISSING" for r in rows):
        L.append("| - | none | - | no gaps detected |")
    L.append("\n## PASS 3 - Revalidate\n")
    L.append("Re-run `qa_check.py` after the fixes and confirm MISSING -> 0 on all")
    L.append("star-mandatory items. Paste the diff here.\n")
    L.append(f"## Verdict: {'PASS' if miss==0 else 'LOOP'}\n")
    open(out,"w",encoding="utf-8").write("\n".join(L))
    print(f"wrote {out}  score={score}%  missing={miss}  n/a={na}")

if __name__ == "__main__":
    main()
