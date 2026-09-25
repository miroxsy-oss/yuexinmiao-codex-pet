# 按 WenNinghan v1 标准的自检 · Self-check against the WenNinghan v1 specification

> 更新：以下为 v1.0.0 的历史检查。当前分支已修正 idle / waving 外轮廓白边；新校验值见 CHECKSUMS.sha256，处理范围及对比见 [边缘修正](OUTLINE_FIX.md)。
>
> **Update:** This report describes v1.0.0. Idle/greeting light fringes have since been corrected. Current hashes are in `CHECKSUMS.sha256`; see [outline repairs](OUTLINE_FIX.md) for scope and comparisons.

日期：2026-09-25。对象：月薪喵 Codex Pet。安装图集 SHA-256：
`5a008b5e7bebfe222c36994ebbd1c724f3be98aa11bd35d72155cabaafb33431`<br>
Date: September 25, 2026. Subject: Yuexinmiao Codex Pet. The installed atlas’s historical SHA-256 was `5a008b5e7bebfe222c36994ebbd1c724f3be98aa11bd35d72155cabaafb33431`.

## 结论 · Conclusion

技术结构通过，达到参考项目公布的 v1 图集与报告检查项；保留用户已选定的视觉特征与状态语义例外。公开素材再分发授权尚未核实完整。<br>
The technical structure passed the reference project’s published v1 atlas/report checks while retaining user-selected visual characteristics and exceptions to state semantics. Permission to publicly redistribute every asset has not been fully verified.

| 检查 · Check | 结果 · Result |
| --- | --- |
| 1536×1872 / 8×9 / 192×208 | 通过 · Passed |
| WebP、RGBA、57 有效帧位 · WebP, RGBA, 57 active slots | 通过 · Passed |
| 9 行规定帧数、15 空白格透明 · Required frame counts in nine rows; 15 transparent unused cells | 通过 · Passed |
| 透明像素 RGB 残留 · Nonzero RGB in fully transparent pixels | 0 |
| hatch-pet inspect_frames | 0 错误 / 0 警告 · 0 errors / 0 warnings |
| hatch-pet validate_atlas（本机安装文件） · hatch-pet validate_atlas on installed file | 0 错误 / 0 警告 · 0 errors / 0 warnings |
| 包及重建独立检查 · Independent package and rebuild checks | 44 项通过 · 44 passed |
| 已批准源帧重新构建 · Rebuild from approved source frames | 图像像素及 WebP 文件均完全一致 · Pixel-identical and byte-identical WebP |
| 黑、白底全帧视觉复核 · Visual review of all frames on black and white | 完成，已知特征见下 · Completed; known characteristics below |
| 9 行 GIF 与浏览器动画 · Nine GIF rows and browser animation | 已检查 · Checked |
| 公开再分发许可 · Public redistribution permission | 未确认完整 · Not fully confirmed |

## v1.0.0 保留的视觉特征 · Retained visual characteristics in v1.0.0

- idle、waving 在深色底上有上游图像自带细白边（历史情况，v1.1.0 已修正）。<br>
  Idle and greeting had thin, upstream white fringes on dark backgrounds. This is historical and was corrected in v1.1.0.

- waving 是半身造型，底部水平截断；不是本次切格意外裁切。<br>
  Greeting uses a partial-body composition with a horizontal lower edge, not accidental cell cropping.

- 左右移动保留少量原素材运动短线；running 保留矩形桌面。<br>
  Left/right movement retains some original motion marks; working retains its rectangular desk.

- jumping 按明确选择播放捂鼻扇风，不符合通常的“跳起—落地”语义。<br>
  The jumping slot deliberately plays nose-covering and fanning rather than a jump/landing sequence.

- 部分动画包含重复帧，帧位仍遵守应用规范。GIF 编码器可能合并相同帧并累加时长。<br>
  Some animations repeat frames, while frame slots follow the application specification. GIF encoders may merge identical frames and accumulate their durations.

每格只有一只猫；在允许原有道具、运动线和半身造型的组合范围内，没有发现空帧、串格、新增裁切或逐帧缩放跳变。不同来源的画法差异仍然存在。<br>
Each cell contains one cat. Within the accepted props, motion marks, and partial-body compositions, no empty active frames, cell overlap, new clipping, or frame-to-frame scale jumps were found. Differences in drawing style between sources remain.

## 复现与证据边界 · Reproduction and evidence limits

`qa/frame-review.json` 与 `qa/installed-validation.json` 来自本机 hatch-pet 脚本默认参数检查。没有宣称运行 WenNinghan 仓库本人的旧版验证器；该仓库公开了结果和规范，本次按其相同规格运行当前本机验证器。<br>
`qa/frame-review.json` and `qa/installed-validation.json` were produced by local hatch-pet scripts using default parameters. This does not claim execution of WenNinghan’s older validator; the current local validator checked the same published specifications.

`qa/package-check.json` 为随包脚本独立复核结果。`qa/reproducibility.json` 记录本环境的逐字节重建结果。编码器版本变化可能导致压缩字节不同，图像像素一致仍是重建的关键检查。<br>
`qa/package-check.json` contains the bundled independent checks. `qa/reproducibility.json` records byte-identical rebuilding in the tested environment. Encoder-version changes may alter compressed bytes; identical decoded pixels remain the key reproduction check.

此处检查针对已安装文件与重放动画，未抓取当前桌面实时运行画面，也不包含 v2 的额外 16 向视线帧。<br>
This historical review examined installed files and replayed animation, not a capture of the live desktop application. It does not include v2’s additional 16-direction gaze frames.
