# 图集结构与检查依据 · Atlas structure and validation basis

本项目按公开产品文档与实际图集结构进行检查，不属于官方认证。

This project validates its atlas against public product documentation and its actual structure; this is not official certification.

| 项目 · Item | 约定 · Contract |
| --- | --- |
| 图集 · Atlas | 1536×1872，透明 WebP · Transparent WebP |
| 格子 · Cells | 8×9，每格 192×208 · 8×9, 192×208 per cell |
| 格式版本 · Sprite version | 1 |
| 有效帧位 · Active slots | 57 |
| 各行动作帧数 · Frames per row | 6 / 8 / 8 / 4 / 5 / 8 / 6 / 6 / 6 |
| 未用格子 · Unused cells | 15，全部透明 · 15, fully transparent |

行顺序：idle、running-right、running-left、waving、jumping、failed、waiting、running、review。机器标识保留英文；jumping 槽位使用捂鼻扇风动作。

Row order: idle, running-right, running-left, waving, jumping, failed, waiting, running, review. Machine identifiers remain in English; the jumping slot uses the nose-covering and fanning gesture.

公开依据：[Pets](https://learn.chatgpt.com/docs/pets) 与 [Commands / Pets](https://learn.chatgpt.com/docs/reference/commands#pets)。具体版本的校验值见根目录 CHECKSUMS.sha256；格式合格不保证所有客户端都触发全部动作。

Public sources: [Pets](https://learn.chatgpt.com/docs/pets) and [Commands / Pets](https://learn.chatgpt.com/docs/reference/commands#pets). See CHECKSUMS.sha256 in the package root for version-specific hashes. Valid formatting does not guarantee that every client triggers every animation.
