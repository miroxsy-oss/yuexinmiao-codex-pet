# v1.1.0 — 边缘修复与 Work 显示适配

本次同时提供 Codex 桌面九状态版与手机 Work 捂鼻扇风专用版。

- 修正摸鱼待机、打招呼的外轮廓浅色残留，统一 README、动图与交互预览。
- 手机 Work 从 v1.0.0 的「挠头思考」改为 v1.1.0 专用版的经典「捂鼻扇风」：目前在已测试的思考、搜索和计算处理场景中，只观察到同一组动画，未见其他动作切换，因此选择更有辨识度、更能代表月薪喵的招牌动作。其他手机状态是否可触发仍待确认，不代表官方已明确只支持一种状态。本机 Codex 九种动作保持不变。
- README 增加手机实际显示、官方默认宠物对照结果、未确认状态及正确上传文件说明。
- 本地安装更新可选择替换并备份或并存；Work 新版验证后按用户选择清理旧条目。
- 统一 Codex Pet 命名，保留发布宣传图。

验证：桌面包 44 项检查通过；Work 图集校验无错误、无警告；iPhone 镜像中 Python 处理和搜索时播放捂鼻扇风。其他手机状态未确认。桌面播放器三遍后回待机的已知行为仍存在，本包不修改应用播放器。

## 下载与升级

- 完整安装包：`yuexinmiao-codex-pet-v1.1.0.zip`，含桌面安装器、两版图集、预览和说明。
- 只更新手机 Work：下载 `yuexinmiao-work-fanning-v1.1.0.webp`，通过 ChatGPT 官方宠物上传入口上传并选中。
- 本机更新可选择替换并备份或保留旧版；Work 新版实机验证后再处理旧条目。

本次从 v1.0.0 升至 v1.1.0：新增向后兼容的 Work 专用版与安装更新选项，按语义化版本惯例增加次版本号。spriteVersionNumber 仍为 1，它是图集格式版本，不是项目发布版本。

English: v1.1.0 adds the Work fanning edition and explicit update choices while keeping desktop compatibility. It also fixes light outlines and documents real-device results. Other mobile states remain unverified. Sprite format version stays at 1.
