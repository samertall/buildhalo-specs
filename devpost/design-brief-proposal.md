---
status: proposal-not-official-skill-output
created: 2026-11-17
note: "Candidate only; run the official plan-lens interview in a saved SPECS Lens Studio project."
---

# Candidate design brief — BuildHalo

**This is a reference proposal, NOT a design brief produced or approved by the official Devpost Learn skill. Do not rename it to design-brief.md to claim eligibility.**

## The one spatial moment

A person assembles a three-piece tabletop phone stand. While looking at the base, they see a translucent upright support showing exactly where to insert it and which direction to move it. They pinch **Done** beside the stand; the guide snaps into an assembled position and advances to the next step.

## Why glasses?

- Draws in the world: ghost parts and placement arrows sit at the connection point at realistic scale.
- Leaves the body free: the user can manipulate the real assembly, advancing guidance with a simple pinch.
- Shares the working view: information appears where they are looking, without requiring camera-based recognition.
- A phone forces repeated attention shifts from physical work to a 2D illustration.

## Product or overlay

- Type: spatial assembly *overlay*, simulated on a virtual workbench in preview.
- Real-world recognition: intentionally NOT part of this MVP.
- Stand-in: virtual tabletop, base, upright and cradle; never label this automatic real-object recognition.

## Placement

- Workbench: approx. 38 × 25 cm, ~1.1 m ahead and below eye level.
- Ghost geometry and insertion cue: approx. 22 × 20 cm directly above the connection point.
- Step label: approx. 18 × 6 cm immediately beside the stand.
- Primary pinch target: approx. 11 × 5 cm near the object, centrally visible.
- Progress: small adjacent 1/3 indicator. All dimensions are **proposed defaults** for learner review and preview validation.

## Inputs

- **Place guide**: large pinch target instantiates workbench.
- **Done**: advances one step with visible feedback.
- **Show motion**: replays the guide animation without changing progress.
- **Back**: reverses step and correctly restores its visual state.
- **Try again**: restarts after success.
- Standard Spectacles Interaction Kit / UI Kit interaction, mouse-testable in Interactive Preview. No voice or custom two-hand gestures required.

## Progressive disclosure

1. Placement affordance only.
2. Base guide becomes solid when confirmed.
3. Ghost upright loops along a short insertion path; arrow disappears on completion.
4. Ghost cradle moves into top notch; user confirms.
5. Small completion ring and restart target.
6. No permanent head-locked dashboard or unnecessary full-scene effects.

## Done criteria — must each be observed in the actual Lens Studio preview

1. Clicking Place guide shows a world-scale workbench, base and 1/3 guide.
2. Done on step 1 changes progress to 2/3 and shows the ghost upright with an insertion cue.
3. Show motion replays an insertion animation without advancing progress.
4. Done and Back update and restore model state correctly.
5. Finishing step 3 shows success; Try again resets the whole task.

## Out of scope

Computer vision recognition, tracking physical parts, automatic assembly verification, connected multi-user Lenses, persistent spatial anchors, live AI calls, speech recognition, or device-only custom gestures.

## Risks and unverified decisions

The simulated workspace cannot validate physical alignment, real-world recognition, comfortable wear, or actual hand tracking. Asset APIs and supported SIK/UI Kit components must be checked in the installed Lens Studio/CLAD environment. This document contains **candidate assumptions**, not an interview with the entrant.

## Build notes for CLAD

- Only run **after** the official plan-lens interview creates an approved `devpost/design-brief.md`.
- Build a real SPECS Lens via Lens Studio MCP and Snap CLAD, using SIK and UI Kit mouse-driven preview interactions.
- Use centimeter scale; keep all main content visible, bright, readable, and near the task.
- Build the minimal working flow before decorative polish.
- Write and execute LEAF tests for the approved done criteria and report actual results.
- Do not record, identify, or follow people.

## After the build

Inspect Interactive Preview from normal standing positions with WASD, Q/E, mouse-look and click-to-pinch. Correct spatial placement and text legibility. Record the **actual Lens Studio preview** in a public <3-minute YouTube video; publish the real Lens project with the generated devpost folder. This proposal and browser storyboard alone are not submission evidence.
