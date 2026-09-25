# 图集自检 · Atlas validation

适用安装包：v1.0.0。当前脚本结果见 [QA 范围](../qa/README.md)，文件校验值见根目录 CHECKSUMS.sha256。

Package: v1.0.0. See [QA scope](../qa/README.md) for current script results and CHECKSUMS.sha256 in the package root for file hashes.

桌面采用透明 WebP、1536×1872、8×9 格、每格 192×208、57 有效帧位。检查要求有效帧非空、15 个未用格全透明、各格无边界裁切、源帧重建像素一致。脚本：`python scripts/check.py`。

The desktop atlas uses transparent WebP, 1536×1872 pixels, an 8×9 grid of 192×208 cells, and 57 active slots. Checks require nonempty active frames, 15 transparent unused cells, no cell-edge clipping, and identical pixels when rebuilt from source frames. Run `python scripts/check.py`.

动作帧数依次为 6/8/8/4/5/8/6/6/6。jumping 槽位按设计使用捂鼻扇风；打招呼保留原素材半身构图。多来源素材有画法差异，这不是重新设计的原创角色。

Frame counts are 6/8/8/4/5/8/6/6/6. The jumping slot deliberately uses fanning; greeting retains its partial-body composition. Collected assets have drawing-style differences; this is not an original character redesign.

安装更新测试覆盖首次安装、重复安装、替换备份、并存、取消和失败回滚。自动检查不等于所有尺寸下视觉完美，也不代表九种状态都已在每种客户端触发。

Installer tests cover first and repeated installation, replacement backups, keeping both versions, cancellation, and rollback after failure. Automated checks do not establish visual perfection at every size or all nine states being triggered on every client.

历史实机证据位于 qa/history/，不作为此次文案修订后重新实测的证明。宿主行为限制见 [状态说明](STATE_AUDIT.md)，图集约定见 [规格](REFERENCE.md)。

Historical device evidence is in qa/history/ and is not proof of a new device test after this documentation refresh. See [host behavior](STATE_AUDIT.md) and the [atlas contract](REFERENCE.md).
