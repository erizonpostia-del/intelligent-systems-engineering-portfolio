# Public Build Report / 公开版构建报告

Build date: 2026-07-14.

## Included source

Public ROS package: `src/robotics/tb3_course_task`.

- Included files: two Python scripts, one launch file, `package.xml`, and `CMakeLists.txt`.
- Excluded source: all `beginner_tutorials` files, VM exports, archive files, bytecode, build products, and installed RViz configurations.

## Maps and configuration

- Public: `house_map_full.{pgm,yaml}` and `world_map.{pgm,yaml}` as paired course/example-provided ROS1 simulation map resources.
- Public YAML adjustment: image paths are relative in the copies; the private originals were not changed.
- RViz: no custom RViz configuration was published because no user-created or confirmed modified configuration was recovered. The included maps are not claimed as personal mapping output.

## Media

- Public ROS1 simulation media: two redacted screenshots.
- Public team physical media: one redacted Navigation2 context screenshot.
- Not public: physical video (manual teleoperation and team-reported RViz goal-directed movement), physical mapping screenshots, raw logs, and unredacted screenshots.

## Attribution and privacy

Code provenance and contribution boundaries are recorded in `docs/代码来源与归属 Code Attribution.md`. Public copies have no recovered personal maintainer identifier or private absolute map paths. Selected screenshots were cropped rather than altered in meaning.

## Known Limitations

- **Verified contribution categories:** `house_auto_avoid.py` is user-confirmed as independently implemented; `world_outer_loop.py` is user-confirmed as independently implemented with course guidance.
- **Not recovered:** the original build, launch, and map-loading commands.
- **Not claimed:** DQN materials are outside this public ROS reconstruction.
- No Git staging, commit, or push operation was performed.
