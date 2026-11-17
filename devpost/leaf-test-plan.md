# LEAF and preview test plan — proposal only

> **Execution status: NOT RUN.** This is a planned acceptance matrix for the eventual CLAD-built SPECS Lens; it does not demonstrate actual tests.

| ID | Initial state | Preview interaction | Expected result | Status |
|---|---|---|---|---|
| L01 | Startup | Pinch/click Place guide | World-positioned guide and step 1/3 appear | NOT RUN |
| L02 | Step 1 | Pinch/click Done | Base becomes solid; animated upright guide and 2/3 appear | NOT RUN |
| L03 | Step 2 | Pinch/click Show motion | Upright insertion animation replays; progress stays at 2/3 | NOT RUN |
| L04 | Step 2 | Done then Back | Correctly restores step 2, hides cradle, shows upright ghost | NOT RUN |
| L05 | Step 3 | Done | Success message and completed geometry appear | NOT RUN |
| L06 | Complete | Try again | Resets to step 1 without stale visual elements | NOT RUN |
| L07 | Any | Move camera with WASD and mouse-look | Workbench remains world-placed instead of head-locked | NOT RUN |
| L08 | Step 2 | Hover actionable control | Hover state clearly visible | NOT RUN |

## Required evidence

CLAD must build in Lens Studio MCP using SIK/UI Kit, execute LEAF tests against interactables in SPECS Interactive Preview, and produce a report with actual test identifiers, observed results and failures. Check runtime Logger and manual legibility. Real physical alignment, comfort, and hand-tracking performance **cannot** be established in laptop preview.

**Do not change NOT RUN to PASS without actual test execution.**
