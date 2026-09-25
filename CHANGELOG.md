# 版本记录 · Changelog

## 1.1.0 — 2026-09-26

- 修正摸鱼待机、打招呼的外轮廓浅色残留，同步 README、动图与交互预览。<br>
  Removed light fringes from idle and greeting outlines and synchronized the README, GIFs, and interactive preview.

- 手机 Work 从 v1.0.0 的「挠头思考」改为经典「捂鼻扇风」。已测试的思考、搜索和计算处理中只观察到同一组动画，因此选择更有辨识度的招牌动作。其他手机状态仍待确认，不代表官方只支持一种状态。<br>
  Mobile Work changes from v1.0.0’s head-scratching animation to the signature nose-covering and fanning gesture. Only one animation group was observed during tested reasoning, search, and computation stages, so the more recognizable gesture was chosen. Other mobile states remain unverified; this does not establish that mobile officially supports only one state.

- 桌面九种动作、帧数与时序不变；Work 专用版单独调整 review 帧映射，复用原始像素，不重绘角色。<br>
  Desktop retains all nine animations, frame counts, and timing. The separate Work edition remaps the review frames using existing pixels, without redrawing the character.

- 补充实机截图、官方默认宠物对照、手机测试范围与正确上传文件说明。<br>
  Added device screenshots, comparison with the official default pet, mobile test scope, and instructions identifying the correct upload file.

- 本机更新可选择替换并备份或并存；Work 新版验证后按用户选择删除指定旧条目或保留。<br>
  Local updates offer replacement with a backup or keeping both versions. After validating the new Work entry, remove the identified older entries or retain them according to the user’s choice.

- 统一 Codex Pet 命名，保留发布宣传图。<br>
  Standardized the Codex Pet naming and retained the launch poster.

两版图集均为 `spriteVersionNumber: 1`。详细验证与升级说明见 [v1.1.0 发布说明](docs/RELEASE-v1.1.0.md)。

Both atlases use `spriteVersionNumber: 1`. See the [v1.1.0 release notes](docs/RELEASE-v1.1.0.md) for validation and upgrade details.

### 同版本修订 · Same-version refresh — 2026-09-26

v1.1.0 与 v1.0.0 的同名安装包同步双语文案、配置描述、安装提示、校验值和维护说明。整理历史 QA，清理工程比较文案。两个版本原有图集与动作均保留，不新增版本。

The existing v1.1.0 and v1.0.0 installation archives receive synchronized bilingual documentation, manifest descriptions, installer messages, checksums, and maintenance guidance. Historical QA is separated and engineering comparisons removed. Both versions retain their original atlases and animations; no new version is created.

## 1.0.0

首次公开发布，包含九种动画状态、安装器、预览和检查记录。

First public release, including nine animation states, the installer, previews, and validation records.
