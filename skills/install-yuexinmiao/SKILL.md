---
name: install-yuexinmiao
description: 安装现成月薪喵 v1.0.0 宠物，不重新生成素材。 Install the prebuilt Yuexinmiao v1.0.0 pet without regenerating artwork.
---

# 安装月薪喵 · Install Yuexinmiao

读取仓库根目录 README.md、LICENSE.md 与 docs/INSTALL.md。技能目录上两级为仓库根目录。仅复用 dist/yuexinmiao-selected，不生成新图，不把本版说成含 v1.1.0 Work 捂鼻扇风专用图集。

Read README.md, LICENSE.md, and docs/INSTALL.md in the repository root, two levels above this skill directory. Reuse dist/yuexinmiao-selected without generating new art. Do not claim this version includes the v1.1.0 Work fanning atlas.

运行 python scripts/install.py。检测到不同旧版时询问替换备份还是并存；沿用本会话已明确的选择。通过 --existing replace 或 --existing keep-both 执行授权更新，保留回滚备份。安装成功不代表 UI 已选中。

Run python scripts/install.py. For a different existing version, ask whether to replace with a backup or keep both; reuse a clear choice already made in this session. Use --existing replace or --existing keep-both for an authorized update and retain rollback backups. Successful installation does not prove UI selection.

Work 上传使用同一目录中的 spritesheet.webp；优先检查可用 MCP，其次受支持 API/CLI，再按需要使用 GUI。新版账号条目激活并刷新验证后，询问保留旧条目还是永久删除，删除前确认。手机通过真实设备或 iPhone 镜像验收，不能用旧截图或浏览器窄屏代替。

For Work, upload spritesheet.webp from the same directory. Prefer available MCP tools, then supported APIs/CLIs, and GUI as needed. After activating and reloading the new account entry, ask whether to retain or permanently delete older entries and confirm before deletion. Validate mobile behavior on a real device or through iPhone Mirroring, not old screenshots or a narrow browser.

分别报告文件安装、网页选中与手机实测结果。缺少认证或工具时只说明真正剩余的操作，不虚构完成。

Report file installation, web selection, and mobile device tests separately. If authentication or tools are missing, state the actual remaining action without inventing success.
