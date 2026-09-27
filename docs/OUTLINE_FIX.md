# 深色背景边缘修正 · Dark-background outline repairs

v1.1.0 使用 R3 修正版。处理摸鱼待机 6 帧和打招呼 4 帧，去除白底污染以及棕色外轮廓中的浅色细线，并仅对轮廓透明度做轻度抗锯齿。没有整体模糊、重绘角色或修改动作帧序与播放时长。其他 47 帧保持逐字节一致。

v1.1.0 includes the R3 correction. Six idle frames and four greeting frames were cleaned of white-background contamination and light lines along brown outlines, with gentle antialiasing limited to outline transparency. No overall blur, character redraw, frame reordering, or timing change was applied. The other 47 frames remain byte-identical.

![左 R2，右 R3，三倍显示 · R2 left, R3 right, at 3×](images/outline-before-after.png)

这是现有位图的边缘修复，不是 SVG 矢量化；固定分辨率图集放大后仍有分辨率上限。结构检查不等于所有尺寸下的视觉完美。修正版已包含于 v1.1.0；手机测试范围见 [Work 说明](MOBILE_WORK.md)。

This repairs existing bitmap edges rather than converting them to SVG vectors; a fixed-resolution atlas still has limits when enlarged. Structural checks do not establish visual perfection at every size. The corrected assets are included in v1.1.0; see the [Work report](MOBILE_WORK.md) for mobile test scope.

执行 `scripts/build.py` 可从修正后的源帧重建。`clean_light_outline.py` 仅用于原版帧的一次性转换，不要重复处理已修正版。

Run `scripts/build.py` to rebuild from the corrected source frames. `clean_light_outline.py` is a one-time conversion for original frames; do not apply it repeatedly to corrected frames.

仅当维护原始素材确实需要一次性边缘处理时，使用 Python 3.11 或以上安装 requirements-maintenance.txt。普通安装、图集重建和校验不需要 NumPy；不要重复处理已修正源帧。

Only for necessary one-time maintenance of original edges, use Python 3.11 or later with requirements-maintenance.txt. Normal installation, atlas rebuilding, and validation do not require NumPy. Do not reprocess already-corrected source frames.

维护依赖按 Python 版本选择：3.11 使用 NumPy 2.3.5，3.12 及以上使用 2.5.3。CI 在 Windows、macOS、Linux 的 Python 3.11 和 3.12 上校验全部 57 帧的内存处理结果；不会覆盖素材。

Maintenance dependencies select NumPy 2.3.5 on Python 3.11 and 2.5.3 on Python 3.12+. CI checks in-memory processing of all 57 frames on Windows, macOS, and Linux with Python 3.11 and 3.12; it does not overwrite artwork.
