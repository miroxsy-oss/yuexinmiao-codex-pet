---
name: install-yuexinmiao
description: 安装现成的月薪喵 Codex Pet，复用随包素材，不生成新图。 Install the ready-made Yuexinmiao (月薪喵) custom pet for Codex desktop when the user wants this cat. Reuse the bundled package without generating new art.
---

# 月薪喵安装技能 · Yuexinmiao installation skill

## 素材与范围 · Assets and scope

使用 https://github.com/miroxsy-oss/yuexinmiao-codex-pet 中的现成安装包。如果技能位于完整仓库中，仓库根目录是技能目录的上两级；否则下载仓库到临时目录。阅读 README 与 LICENSE，保留署名和个人非商业使用范围。<br>
Use the prebuilt package from https://github.com/miroxsy-oss/yuexinmiao-codex-pet. If this skill is inside a full checkout, the repository root is two directories above this skill folder. Otherwise download the repository to a temporary directory. Read its README and LICENSE to retain attribution and personal, noncommercial scope.

## 工具顺序 · Tool preference

优先检查已暴露的 MCP 功能工具，其次使用受支持的 API 或 CLI；仅在这些路径不能完成操作或需要实际视觉验收时使用 GUI。下面的浏览器上传流程是缺少受支持直接上传能力时的回退方案。<br>
Check exposed MCP capabilities first, then supported APIs or CLIs. Use GUI control when those routes cannot complete the operation or actual visual verification is required. The browser-upload workflow below is a fallback when no supported direct upload capability is available.

## 本机安装与更新 · Local installation and updates

更新已安装版本前，询问替换并备份还是并存；本会话已有明确选择时直接沿用，不重复询问。首次安装运行 `python scripts/install.py`；已授权更新使用 `--existing replace` 或 `--existing keep-both`。没有明确选择的非交互更新应停止且不修改文件。安装器检查校验值，安装到 `$CODEX_HOME/pets` 或 `~/.codex/pets`，把不同的旧版移到宠物库外的备份目录。安装仅需 Python 标准库；重建或检查图像才需要 Pillow。普通安装不得重新生成图集。<br>
Before updating an existing installation, ask whether to replace the previous version (with a rollback backup outside the pet library) or keep both versions. Reuse an explicit choice already made in this session; do not ask twice. For a fresh install, run `python scripts/install.py`. For an authorized update, use `python scripts/install.py --existing replace` or `--existing keep-both` according to that choice. Without a choice, noninteractive updates stop without changing files. It verifies the bundled checksums, installs under `$CODEX_HOME/pets` or `~/.codex/pets`, and backs up a different existing copy of the same pet. Installation needs only Python's standard library; Pillow is needed only to rebuild or audit images. Do not regenerate sprites or invoke image generation for a normal install.

## Work 上传与旧版处理 · Work upload and older versions

报告安装位置与「月薪喵 Codex Pet」显示名称。未验证界面前，不得声称已经切换选中项。Work／手机按 `docs/INSTALL.md` 操作：本地安装不自动同步账号。经授权并具备已登录工具后，先检查原条目是否有官方替换图集能力，不能假定存在。如无替换能力，仅上传一次 `dist/yuexinmiao-work-fanning/spritesheet.webp`，激活并刷新核验。新版通过后询问删除已识别旧条目还是保留；永久删除应在执行时确认。仅删除明确批准的条目，保留官方及其他宠物，再刷新核验剩余列表与选中项。不得在新版验证前删除旧版。本地备份独立保留。<br>
Tell the user the installed path and that the pet picker entry is 「月薪喵 Codex Pet」. Do not claim the live UI switched unless verified. For Work or mobile requests, follow `docs/INSTALL.md`: local installation does not synchronize the account pet. With the user’s authorization and available authenticated browser tooling, upload `dist/yuexinmiao-work-fanning/spritesheet.webp` through the official ChatGPT pet UI, select the new entry, and verify persistence after reload. Before uploading, inspect the existing pet actions for an official sprite replacement option; do not assume one exists. If replacement is unavailable, upload once, activate the new entry, reload and verify it, then ask whether to delete the identified previous Yuexinmiao entries or keep them. Permanent account deletion requires confirmation at action time. Delete only explicitly approved entries, preserve official and unrelated pets, and reload to verify both the remaining list and active selection. Never delete the old account entry before the new one passes validation. Local backups are retained independently.

## 结果报告 · Reporting results

不得使用私密凭据，也不得凭网页成功宣称手机成功。分别报告本机安装、账号上传、网页显示和实机测试；未测试环节标注待确认。缺少操作工具或登录时，完成本机准备，仅说明真正剩余的一步。<br>
Do not use private credentials or claim mobile success from web-only evidence. Report desktop installation, account upload, web display, and actual mobile testing separately; mark untested stages as pending. If browser control or authentication is unavailable, finish local preparation and explain the exact remaining step.

## 动作修改 · Animation changes

动作修改需参考 `source/selection.json` 与 `docs/SELF_CHECK.md`，保留用户选定的动作并说明对安装素材的影响。<br>
If the user wants animation changes, consult `source/selection.json` and `docs/SELF_CHECK.md`; preserve their selected actions and report when a request changes the installed artwork.

## 手机实机验证 · Mobile device verification

手机验收优先通过可用原生 Computer Use 工具操作 iPhone 镜像，先检查能力再承诺可访问。手机锁定、正在使用或要求认证时，仅请求必要操作。观察真实 Work 任务并采集至少两帧确认动画；区分账号持久保存、网页运行、用户报告的手机可见与代理实际观察的手机动画。窄屏浏览器不是 iPhone 实测。缺少工具时明确说明，不默认要求用户截图，不把历史记录当作当前版本证据。<br>
For mobile verification, prefer iPhone Mirroring through an available native Computer Use tool. Inspect its current capabilities before promising access. If the phone is locked, in use, or authentication is required, request only the necessary user action. Observe the actual mobile Work task and capture at least two frames to verify motion. Separate account persistence, web runtime display, user-reported mobile visibility, and agent-observed mobile animation. A browser viewport resized to phone dimensions is not an iPhone test. If the native tool is absent, state that limitation; do not ask the user for screenshots by default or reuse a historical test as evidence for the current release.

## 原生工具发现 · Native tool discovery

缺少旧版 `cua_repl` 或未定义 `cua` 不能证明电脑控制不可用；应检查配置的原生运行时和已安装文档。运行时明确提供可信 sky 服务时，通过 node_repl 使用有文档说明的 `@oai/sky` API。不得修改安全设置或绕过应用拒绝。<br>
Computer Use capability discovery: absence of the legacy cua_repl tool or an undefined cua global is not proof that desktop control is unavailable. Inspect the configured native runtime and its installed documentation. In a runtime that explicitly advertises the trusted sky service, use the documented @oai/sky API via node_repl. Do not change security settings or bypass app denials.

## Work 图集选择 · Work atlas selection

Work 选择「月薪喵 Work · 捂鼻扇风」。该独立图集用已批准扇风帧替换已观察到的手机 review 槽位，不要覆盖本机九状态桌面版。阅读 `docs/MOBILE_WORK.md`，不得声称手机官方只支持一种状态。<br>
For Work, select 「月薪喵 Work · 捂鼻扇风」. This separate atlas replaces the observed mobile review slot with approved fanning frames. Do not install this variant over the local nine-state desktop edition. Read docs/MOBILE_WORK.md; do not claim mobile officially supports only one state.
