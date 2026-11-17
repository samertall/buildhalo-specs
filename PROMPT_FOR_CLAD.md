# CLAD implementation handoff

> **Use only after** the Devpost Learn `plan-lens` skill has run within a real SPECS Lens Studio project and created an approved `devpost/design-brief.md` there.

Read `devpost/design-brief.md` and build BuildHalo for SPECS using the **CLAD plugin through the active Lens Studio MCP server**. Implement an actual three-step assembly flow on a world-positioned simulated tabletop, with SIK / UI Kit interactions that work in mouse-driven SPECS Interactive Preview.

Begin with the full basic state flow. Add scaled virtual phone-stand geometry, animated translucent ghost-part insertion, restrained progress labels, bright text suitable for additive displays, and optional subtle feedback. The virtual model is a **stand-in**, not real camera-based object recognition.

Implement `Place guide`, `Done`, `Show motion`, `Back` and `Try again` exactly as specified in the **approved official** brief. Get all interaction components from the active installed API rather than guessing. Test with LEAF for every done criterion, inspect Logger, fix errors, rerun tests, and save observed test results to `devpost/`. Report PASS / FAIL / NOT TESTED accurately; do not claim test success without execution.

Do not represent the browser storyboard as a Lens Studio preview and do not claim eligibility or Devpost submission until a real SPECS Lens and demo video exist.
