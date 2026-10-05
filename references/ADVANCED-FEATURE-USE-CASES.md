# Advanced Feature Catalogue — the complete professional toolset

**This is the full catalogue.** Every build runs a **Feature Pass** (see the end)
over it: walk every group, decide which features apply, and record how each one
will be implemented *before* the build. "Mandatory" means: if the concept needs
it, you use it. Reading the catalogue is meant to make the agent *reach for the
feature* — and using the feature is what lifts the video to an industry standard.

The camera features (zoom in / zoom out, character/face zoom, focus pulls …) are
as mandatory as the exotic ones. A build that omits the fundamentals reads as
amateur even if it nails the flashy parts.

---

## 1 · Camera & framing
The grammar of the lens. Every move needs a reason (see the Camera Law).
- **Zoom in / zoom out** — anchor zoom to a detail (origin on the target) and a
  zoom-out reveal; the wide↔detail rhythm is the pacing engine.
- **Character zoom / face zoom** — push in to a person's face for emotion; the
  classic "character zoom in focus" beat.
- **Push in / pull out (dolly)** — move the camera, not the lens, for a natural
  perspective change.
- **Pan / tilt** — reframe across a scene or up a subject.
- **Truck / pedestal / crane / boom** — lateral, vertical and arcing moves.
- **Orbit / arc** — circle a subject for dimension.
- **Whip pan** — fast pan used as a transition.
- **Snap zoom / crash zoom** — a violent, sudden zoom for a punch.
- **Dolly zoom (Vertigo effect)** — dolly in while zooming out for disorientation.
- **Rack focus / focus pull** — shift focus from one subject to another in-frame.
- **Follow focus** — keep a moving subject sharp.
- **Parallax move** — layered depth as the camera travels.
- **Dutch angle / roll** — tilt the horizon for unease.
- **Handheld vs stabilised** — energy vs calm; choose deliberately.
- **Drone / aerial, top-down, worm's-eye, over-the-shoulder, POV.**
- **Slow reveal / pull-back reveal** — start tight, reveal the context.
- **Reframe / auto-reframe** — recompose for 9:16 / 1:1 / 4:5.

## 2 · Motion & animation
- **Keyframing** — animate position, scale, opacity, rotation, blur; nothing
  moves without keys.
- **Easing / bezier** — ease every move; curve the *path*, not just the timing.
- **Anchor-point control** — set the transform origin before animating.
- **Motion tracking** — point, planar or 3D; lowpass the track before binding.
- **Masking / rotoscoping** — frame-by-frame isolation; garbage matte.
- **Shape morph** — morph one shape into another.
- **Puppet / rig / character animation** — pins and skeletons.
- **Expressions / wiggle / auto-animate** — procedural motion.
- **Text animators / range selectors** — per-word and per-character animation.
- **Spring / follow** — damped follow for organic motion.

## 3 · Speed & time
- **Speed ramp** — slow→fast or fast→slow across a beat.
- **Time remap** — a full speed curve with easing.
- **Reverse** — play a clip backwards for a reveal or a reset.
- **Freeze frame / hold** — stop on the moment that matters.
- **Slow motion (optical flow)** — smooth slow-mo without stutter.
- **Timelapse / hyperlapse / fast motion.**
- **Strobe / echo / posterize time** — the 12fps stutter, ghost trails.
- **Frame blending** — interpolation between frames.
- **Jump cut** — compress time; a stylistic cut.

## 4 · Transitions & cutting
- **Hard cut · J-cut · L-cut · match cut · cut on action · cut on beat.**
- **Cross dissolve · dip to black / white.**
- **Whip-pan / zoom / blur transition** — the Vox camera-blur transition.
- **Mask / wipe / iris / shape wipe.**
- **Light leak / film burn / luma wipe.**
- **Glitch / RGB split / datamosh.**
- **Morph cut · slide / push · 3D flip · cube.**
- **Match-frame / invisible (seamless) cut.**
- **Speed-warp transition** — blur + zoom + speed at the cut.

## 5 · Text & titling
- **Kinetic typography · word-pop · karaoke.**
- **Lower thirds · titles · end cards · chyrons.**
- **Text behind subject · text on a path · type-on / draw-on.**
- **Highlight · underline · hand-drawn circle** (the highlighter, the circle).
- **Sticker captions · transparent (alpha) captions.**
- **Count-ups · stat cards · data labels.**
- **Subtitles / captions · SRT / VTT sidecar.**

## 6 · Colour
- **Correction** — exposure, white balance, contrast, curves, levels FIRST.
- **Grading** — LUT, film emulation, split-tone, teal-orange, bleach bypass.
- **Scopes** — waveform, vectorscope, RGB parade, histogram; grade by numbers.
- **Colour match** between shots; **skin-tone protection.**
- **LOG → Rec.709 conversion · HDR grading · SDR tone-mapping.**
- **Vignette · grain · halation · bloom.**

## 7 · Compositing & VFX
- **Chroma key** — flat green (#00B140) / blue; despill, choke, light wrap,
  garbage matte.
- **Rotoscoping · tracking · planar track · 3D camera tracking (matchmove).**
- **Set extension · screen replacement · camera projection.**
- **Particles · simulations · shaders.**
- **Light wrap · glow · lens flare · light leak.**
- **Object removal · clone / stamp · clean plate · rig removal.**
- **2.5D parallax · sky replacement · green-screen comp.**
- **Motion-graphics templates (MOGRT-style) · pre-comps / nesting.**

## 8 · Audio
- **Noise reduction** — de-noise, de-hum, de-click, room-tone removal.
- **EQ · compression · limiting.**
- **Audio sync** — waveform / timecode.
- **Multi-track mixing** — dialogue / music / SFX buses; duck music 12–18 dB.
- **Sound design · SFX · foley.**
- **Music editing · beat mapping** (drive cuts from the BPM).
- **Dialogue editing · ADR · voiceover.**
- **Spatial / surround** (only where the delivery needs it).
- **Loudness normalisation** — integrated LUFS + true-peak ceiling.

## 9 · AI & smart features
- **Auto subtitles (speech-to-text)** — word-level timing drives captions AND
  the narration plan.
- **AI background removal / AI matte** — no green screen needed.
- **Auto reframing** — 9:16 / 1:1 / 4:5.
- **Scene detection & auto cutting** — build a cut list from scene changes.
- **AI colour / exposure correction** — first pass, then grade by hand.
- **Generative fill / object removal.**
- **AI upscale · AI denoise.**
- **Face / object detection · smart tracking.**

## 10 · Stills & design craft (every generated asset)
- Layer-based editing · layer masks · blending modes.
- Frequency separation (skin retouch) · dodge & burn.
- Content-aware fill / object removal · perspective correction.
- RAW processing · tone curves · HDR merge · panorama stitch.
- AI-assisted selection · non-destructive workflow.
- Vector editing (bezier) · gradient mesh · typography controls (kerning,
  tracking, leading) · symbol/asset libraries · artboards · grid systems ·
  multi-format export.

## 11 · Workflow & delivery
- **Multi-track timeline** — V1/V2/V3 + A1/A2, never a flat single track.
- **Multi-camera editing** — sync angles, cut on speaker/action.
- **Proxy editing** — cut proxies, re-render the same cut list on the originals.
- **Nesting / pre-comps · adjustment layers · render queue.**
- **Batch export** — every ratio/resolution from one master.
- **Colour management · project templates · collaboration.**

---

## The Camera Law (mandatory wherever there is a camera)
1. **One camera wrapper only** — all zooms/pans from a single master camera;
   never local ad-hoc transforms on nested elements.
2. **One camera move at a time** — never stack camera transforms.
3. **Every zoom has a reason** — READ / EMPHASIZE / REVEAL / FOLLOW / BREATHE.
   Constant zoom = no zoom.
4. **Do not cut while zoomed** — return to rest or hold the scene.
5. **Motion blur only during fast motion** — `blur = clamp(v*k, 0, max)`, zero at
   rest (start k ≈ 0.012, max ≈ 24 px). **Anchor zoom** sets the origin on the
   target; **follow** keeps the subject in a safe zone with a damped spring.

## The Sentence Law (mandatory)
Every narration sentence gets its own visual event, bound to its stressed word
(±100 ms). No visual-less sentences; no sentence-less visuals.

---

## THE FEATURE PASS (mandatory — run it while writing CONCEPT.md)

**When the concept is being written, walk this entire catalogue and decide, for
every feature, whether it applies and how it will be implemented.** The concept
is not finished until every applicable feature has a row. This is the step where
the agent thinks about *how it will build the advanced features* before building.

Write a **FEATURE MAP** into CONCEPT.md:

| # | Feature | Applies? | Where (scene / timecode / sentence) | How (implementation) | Why (the job it does) |
|---|---|---|---|---|---|
| 1 | Zoom in / anchor zoom | yes | 0:03 on the logo | scale 1.0→1.15, origin on logo, ease-out 400 ms | read the mark |
| 2 | Character zoom | yes | 0:11 on the founder's face | push to face, hold 1.5 s | emotion |
| 3 | Rack focus | no | — | — | — |
| … | … | … | … | … | … |

Rules for the Feature Pass:
- **Every group is visited** (camera, motion, speed, transitions, text, colour,
  compositing, audio, AI, stills, workflow) — no group is skipped.
- Every "yes" row has a **where**, a **how** and a **why**. A "yes" with no how is
  not a plan.
- Every "no" is deliberate — the feature was considered and does not serve this
  concept.
- The map feeds the **asset manifest** (STEP 2) and the **QA gate**
  (`edit-qa-validator`, `tools/qa_check.py`), which re-checks that every "yes"
  actually made it into the edit.

## The test
Walk the timeline. For each feature the concept needed, ask: **"is it there, and
is it doing a job?"** A missing needed feature — a flat single track, an ungraded
image, no zoom on the key detail, a jittery tracked label, a static sentence —
means the edit is not finished.
