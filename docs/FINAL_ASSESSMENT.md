# 验证结论与边界 · Validation summary and limits

素材包的结构与重建通过随包检查；版本与当前校验结果见 [QA 范围](../qa/README.md)。安装器只处理本机文件，不能自动激活界面选择或上传 Work。

The bundled checks validate atlas structure and rebuilding. See [QA scope](../qa/README.md) for the package version and current results. The installer handles local files only; it does not activate UI selection or upload to Work.

桌面播放器的非待机动作可能三遍后回待机；图集映射正确并不保证动作覆盖整个任务时长。手机的全部状态分支也尚未验证。这些宿主行为不等于图集损坏，本包未修改应用播放器。

The tested desktop player can return to idle after three non-idle repetitions. Correct atlas mapping does not guarantee that an animation lasts for an entire task. All mobile state branches have not been verified either. These host behaviors do not mean the atlas is corrupt; this package does not modify the app player.

本项目为网络素材整理适配，不是角色原创或官方认证；完整素材包再分发许可尚未核实。见 [权利说明](ATTRIBUTION.md)。

This project curates and adapts collected artwork; it is not an original character or an officially certified package. Permission to redistribute all bundled artwork remains unverified. See the [rights notice](ATTRIBUTION.md).
