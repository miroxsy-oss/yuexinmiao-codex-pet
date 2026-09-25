# 手机 Work 显示与验证范围

2026-09-26，通过真实 iPhone 镜像测试，未用浏览器窄屏模拟。

| 图集 | 思考／处理 | 联网搜索 | 完成后 |
| --- | --- | --- | --- |
| 原九状态月薪喵 | 挠头看电脑 | 挠头看电脑 | 状态图标隐藏 |
| 官方默认 Codex（对照） | 官方动画循环 | 未见明显动作组切换 | 状态图标隐藏 |
| Work 捂鼻扇风专用版 | Python 处理时捂鼻扇风 | 捂鼻扇风 | 状态图标隐藏 |

这里只描述已采样的实际行为，不保证捕获每个瞬间。其他客户端、等待授权、失败等分支未验证；移动端完整状态映射仍需官方说明或进一步实测，不能宣称“官方只支持一种状态”。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets)说明显示取决于使用界面，并未列出完整 iPhone 状态映射。

## 从 v1.0.0 到 v1.1.0：为什么更换动作

手机 Work 从 v1.0.0 的「挠头思考」改为 v1.1.0 专用版的经典「捂鼻扇风」：目前在已测试的思考、搜索和计算处理场景中，只观察到同一组动画，未见其他动作切换，因此选择更有辨识度、更能代表月薪喵的招牌动作。其他手机状态是否可触发仍待确认，不代表官方已明确只支持一种状态。本机 Codex 九种动作保持不变。

## Work 专用版的差异

- 文件：`dist/yuexinmiao-work-fanning/spritesheet.webp`，透明 WebP，1536×1872，spriteVersionNumber 1。
- 仅第 8 行 review 改为原第 4 行捂鼻扇风素材；五张原帧映射为六个槽位 `[0,1,2,2,3,4]`，中间帧有意重复一次。
- 像素原样复用，无重绘、缩放或调色；其余八行不变。本机安装器仍安装九状态桌面版。
- Work 使用账号级选择，网页版也会使用此图集；不是仅 iPhone 私有的覆盖设置。
- 宠物出现时播放目标动作，任务结束后的隐藏由 Work 决定；不是屏幕常驻浮窗。
- 手机存在设置同步／缓存延迟。首次测试仍显示旧宠物，不计为通过；重新进入应用并核对个性化设置后，已验证新动作及多帧变化。

![手机处理阶段的四次采样（局部放大）](images/mobile-work-motion.png)

公开仓库仅含宠物局部截图，不包含个人设置、账号或完整对话截图。当前维护者账号已启用新版并清理旧 Work 条目；下载者需在自己的账号上传、选择和验证。

English: The fanning edition reuses approved pixels in the observed mobile review slot, leaving the local nine-state edition intact. Reasoning/tool-processing samples and the official control do not establish that mobile supports only one state. Other states remain unverified. The upload is account-level, also affecting web Work. Full device screenshots are not included in this public package.
