# BuildHalo — Spatial Assembly Assistant

**Learn AR with SPECS · 2026, Round 2**

> **Project status: CONCEPT AND BROWSER PROTOTYPE ONLY.** This repository does **not** yet contain a functioning Lens Studio SPECS Lens. The Devpost Learn `plan-lens` interview, official approved design brief, CLAD build, Lens Studio preview, and LEAF tests have **not** been completed.

BuildHalo explores a better kind of assembly instruction: spatial 3D guidance where a user is already working, instead of a manual or phone that competes for attention. Its single focused use case is a three-piece tabletop phone stand. The proposed Lens shows a translucent *ghost component*, a short insertion trajectory, and one large pinch control next to the assembly point.

## Current experience

- [Browser concept prototype](concept-preview/index.html): self-contained HTML/CSS/JavaScript storyboard. **This is not Lens Studio and cannot qualify as the competition's working Lens.**
- [Candidate design brief](devpost/design-brief-proposal.md): a proposal for the learner to review through the *official* Devpost Learn skill; it is **not** `devpost/design-brief.md`.
- [LEAF acceptance plan](devpost/leaf-test-plan.md): proposed tests, **none executed yet**.
- [CLAD build prompt](PROMPT_FOR_CLAD.md): use only after the official design brief is approved.
- [Video production guide](devpost/video-production.md): record the actual Lens Studio preview when it exists.
- [Final submission checklist](devpost/final-submission-checklist.md): requirements and evidence gates.
- [Local preflight](tools/preflight.py): file-presence checks only; no claim of runtime or LEAF validation.

## Planned interaction flow

1. **Place guide** — instantiate a virtual work area at comfortable working distance.
2. **Step 1/3: Align base** — a footprint cues the base position; **Done** advances.
3. **Step 2/3: Slide upright** — translucent upright and insertion path illustrate the placement; **Show motion** replays it.
4. **Step 3/3: Attach cradle** — preview the fitting motion; **Back** can revisit a step.
5. **Complete** — show an unobtrusive success state; **Try again** resets the task.

This is designed to use world-positioned elements, real-world scale, readable light text, and SIK/UI Kit interactions compatible with the mouse-driven Interactive Preview. It intentionally **does not claim live object recognition or hand-tracking validation**.

## Official build workflow (required before Devpost submission)

1. Create a fresh **SPECS → Base Template** project in Lens Studio and save the project folder containing `.esproj` and `.mcp.json`.
2. Connect a coding agent to Lens Studio MCP and install Snap's **CLAD** plugin.
3. From that project root, install the competition skills: `npx skills add challengepost/learn-specs --all -y`.
4. Run `plan-lens`, participate in its interview, approve the decisions, and keep the **actual** `devpost/design-brief.md` in the Lens project.
5. In a fresh agent session, instruct CLAD to implement the approved brief in Lens Studio through MCP.
6. Validate the full flow in SPECS Interactive Preview and run LEAF tests; record observed outcomes.
7. Push the **actual** Lens Studio project source and `devpost/` directory into this repository.
8. Record a **real Lens Studio preview demonstration under 3 minutes** and publish it on YouTube. Add this repository and real video URLs to Devpost.

**The separate browser concept video does not meet the required real Lens Studio preview demonstration.**

## Links

- [Learn AR with SPECS](https://learn-specs.devpost.com/)
- [Official skill pack](https://github.com/challengepost/learn-specs)
- [Competition resources](https://learn-specs.devpost.com/resources)
- [Existing Devpost draft](https://devpost.com/submit-to/32079-learn-ar-with-specs/manage/submissions/1295202/edit)

**Prepared:** November 17, 2026 · **Deadline:** December 8, 2026, 01:00 Asia/Amman.
