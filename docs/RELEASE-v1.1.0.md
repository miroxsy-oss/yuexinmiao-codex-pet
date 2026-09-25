**月薪喵 · Yuexinmiao Codex Pet**

提供桌面九状态版与手机 Work 捂鼻扇风专用版。由 [@miroxsy-oss](https://github.com/miroxsy-oss) 整理、适配与维护。

Includes the nine-state desktop edition and the fanning edition for mobile Work. Curated, adapted, and maintained by [@miroxsy-oss](https://github.com/miroxsy-oss).

## 相比 v1.0.0 的变化 · Changes since v1.0.0

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

## 验证与限制 · Validation and limitations

桌面包 44 项检查通过；Work 图集校验无错误、无警告。iPhone 镜像中 Python 处理和搜索时已验证捂鼻扇风及不同动作帧，完成后图标隐藏。其他手机状态未确认。桌面播放器仍在非待机动作三遍后回待机，本包不修改应用播放器。

The desktop package passed 44 checks; Work atlas validation reported no errors or warnings. Actual iPhone Mirroring tests verified fanning with distinct motion frames during Python processing and search; the icon disappeared after completion. Other mobile states remain unverified. The desktop player still returns to idle after three repetitions of a non-idle animation; this package does not modify the application player.

## 下载与升级 · Downloads and updates

- 完整安装包 / Full installation package: `yuexinmiao-codex-pet-v1.1.0.zip`，含桌面安装器、两版图集、预览与说明。 / Includes the desktop installer, both atlases, previews, and instructions.
- 仅 Work / Work only: `yuexinmiao-work-fanning-v1.1.0.webp`，通过 ChatGPT 官方宠物上传入口上传并选中。 / Upload through ChatGPT’s official pet uploader and select it.
- 校验值 / Checksums: `SHA256SUMS.txt`。
- 最新中英对照文档 / Updated bilingual documentation: [README](https://github.com/miroxsy-oss/yuexinmiao-codex-pet#readme) · [安装与更新 / Installation and updates](https://github.com/miroxsy-oss/yuexinmiao-codex-pet/blob/main/docs/INSTALL.md)。已发布安装包保持原样，文档修订以仓库为准。 / Published installation archives remain unchanged; see the repository for documentation corrections.

更新时先验证新版，再按用户选择处理旧条目，并保留本机备份。本机安装不会自动更新手机账号中的宠物。

Validate the new version before handling older entries according to the user’s choice, retaining local backups. Local installation does not automatically update the account pet on your phone.

## 版本与使用范围 · Version and usage scope

新增向后兼容的 Work 专用版和安装更新选项，因此从 v1.0.0 升为 v1.1.0。两版的 `spriteVersionNumber` 均为 1：这是图集格式版本，不是项目发布版本。

The backward-compatible Work edition and installer update options warrant the minor-version change from v1.0.0 to v1.1.0. Both editions retain `spriteVersionNumber: 1`, which identifies the atlas format, not the project release.

个人非商业使用，非官方项目。第三方权利与素材来源见仓库 LICENSE.md 和 docs/ATTRIBUTION.md。

Personal, noncommercial use; an unofficial project. See the repository’s LICENSE.md and docs/ATTRIBUTION.md for third-party rights and asset sources.
