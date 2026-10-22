# 桌面与手机使用指南 · Desktop and mobile guide

两份现成图集分别面向桌面九状态显示和手机 Work 捂鼻扇风显示。安装器只写入本机目录；新版客户端可能自动将本机宠物迁移到账号。安装桌面包不等于已正确更新手机所需图集，更新前后都应核对账号列表和当前选中项。

Two ready-made atlases serve the nine-state desktop display and the mobile Work fanning display. The installer only writes local files, but newer clients may automatically migrate local pets into the account. Installing the desktop package does not establish that the phone has the intended atlas; check the account library and active selection before and after updates.

## 1. 桌面端 · Desktop

1. 下载 v1.1.0 Release 附件 `yuexinmiao-codex-pet-v1.1.0.zip` 并解压，进入解压目录。<br>
   Download and extract the v1.1.0 release asset `yuexinmiao-codex-pet-v1.1.0.zip`; open the extracted folder.

2. macOS 运行 `python3 scripts/install.py`；Windows 运行 `python scripts/install.py`。需要先有 Python。<br>
   On macOS run `python3 scripts/install.py`; on Windows run `python scripts/install.py`. Python must be installed.

3. 打开 Codex 的「设置 → 宠物」，刷新列表，选择「月薪喵 Codex Pet」。需要显示桌面浮窗时，在聊天中输入 `/pet`。<br>
   Open Codex Settings → Pets, refresh the list, and select 「月薪喵 Codex Pet」. Enter `/pet` in a chat to toggle the desktop overlay.

4. 更新后仍显示旧版：重新选择宠物；若仍未更新，结束当前工作后完全退出并重新打开应用。<br>
   If an update still shows the old artwork, reselect the pet. If needed, finish active work before fully quitting and reopening the app.

安装器发现不同的旧版时，会先询问替换还是并存。替换会把旧版移到 pets 目录外的 pet-backups 中，宠物列表只保留新版；并存会给新版分配独立 ID。重复安装相同版本不会新增条目。不会自动替你切换界面选择。默认安装位置为 `~/.codex/pets/yuexinmiao-selected/`，设置了 `CODEX_HOME` 时以该目录为准。

For an existing different version, the installer asks whether to replace it with a backup in `pet-backups` outside the `pets` directory or keep both under separate IDs. Reinstalling the same version does not create another entry. It does not change the UI selection. The default location is `~/.codex/pets/yuexinmiao-selected/`, or the equivalent location under `CODEX_HOME` when configured.

## 2. 安装或更新 Work 账号宠物 · Install or update the account pet

优先让 Codex 使用官方 Work Pets MCP 完成账号操作；只有缺少所需能力时才使用网页官方入口。以下流程同时适用于首次安装和更新，避免每次都增加一只宠物。

Prefer the official Work Pets MCP in Codex for account operations. Use the official web controls only when a required capability is unavailable. This workflow covers both first installation and updates, without creating another pet each time.

1. 确认已授权的工具连接使用与手机相同的账号和工作区。调用 `list_pets` 并读取所有分页，记录已有条目的稳定 ID、名称、是否自定义及当前选中项。名称可能重复，缩略图也可能相同；不能只凭外观判断旧版。<br>
   Confirm that the authorized tool connection uses the same account and workspace as the phone. Call `list_pets` through all pages and record each relevant stable ID, name, custom-pet status, and the active selection. Names can repeat and thumbnails can match; appearance alone does not identify an older edition.

2. 已有目标条目时，沿用其稳定 `pet_id`，通过 `update_pet` 更新；仅改名称或描述时只提交对应字段。不要用 `create_pet` 代替更新。目标不明确时，先向用户确认具体条目。<br>
   For an existing target, retain its stable `pet_id` and use `update_pet`. For a name or description change, submit only those fields. Do not substitute `create_pet` for an update. Resolve ambiguous targets with the user before making changes.

3. 更换图集前，下载并备份现有图集，检查当前工具的 schema、验证要求与上传流程。使用 **`dist/yuexinmiao-work-fanning/spritesheet.webp`**，而不是 GIF、截图、ZIP 或 `pet.json`。本包为有效的 v1 资产；已有 v1 的运行记录不等于当前替换接口已验证接受它。如果工具只接受 v2 或无法验证 v1，保留现有宠物并报告限制，不修改版本号绕过验证、不强制转换，也不重建副本。<br>
   Before replacing artwork, download and back up the stored atlas, then inspect the current tool schema, validation requirements, and upload procedure. Use **`dist/yuexinmiao-work-fanning/spritesheet.webp`**, not a GIF, screenshot, ZIP, or `pet.json`. This package contains valid v1 assets; past v1 runtime success does not prove compatibility with the current replacement API. If tools only accept v2 or cannot validate v1, preserve the existing pet and report the limit. Do not bypass validation by relabeling the version, force a conversion, or create a duplicate.

4. 只有当前工具验证通过后，才准备上传并把返回的 `upload_session_id` 交给 `update_pet`，验证返回的 ID 与原 ID 一致。首次安装、且确认没有对应条目时，才使用创建流程；同样须先验证格式。不要自动把桌面九状态条目当成 Work 专用条目覆盖。<br>
   Only after current-tool validation succeeds, prepare the upload and pass the returned `upload_session_id` to `update_pet`; verify that the returned ID matches the original. Use the creation flow only for a first installation after confirming no corresponding entry exists, with the same format checks. Do not automatically overwrite a nine-state desktop entry as if it were the Work edition.

5. 用户要求启用时调用 `select_pet`，然后重新读取完整列表，确认同一 ID 的保存内容与选中状态。仅更新内容时保留原有选择；继续检查实际 Work 画面。待机缩略图仍可能是「电脑前抱鱼」，这不能单独证明捂鼻扇风版没有生效。<br>
   Call `select_pet` when activation was requested, then read the full library again to verify the saved entry and active state by ID. Preserve the prior selection for an update-only request, and check the live Work display. The idle thumbnail may still show the cat holding a fish beside the monitor; that alone does not show that the fanning edition failed to apply.

6. 客户端迁移或历史安装留下重复项时，先验证需保留的版本，再按用户选择删除或保留具体旧 ID。删除前说明名称、ID 和永久删除影响；沿用本会话对这些明确条目的有效授权。只删除已批准的自定义旧条目，保留官方及其他宠物，最后再次核对剩余列表和选中项。<br>
   If client migration or earlier installations left duplicates, first validate the edition to retain, then follow the user’s choice for the specific older IDs. Before deletion, identify the name, ID, and permanent effect; honor valid authorization already given for those exact entries in the session. Delete only approved older custom pets, preserve built-in and unrelated pets, and recheck the library and active selection afterward.

**网页回退：**在已登录的 [ChatGPT](https://chatgpt.com) 设置中查找「虚拟宠物 / Pets」，部分版本位于「个性化」。先核对已有条目及其编辑能力；只有首次安装才上传并命名为「月薪喵 Work · 捂鼻扇风」。网页入口、编辑功能及接受的格式会随版本变化，不能假定一定有上传或替换按钮；缺少能力时保留当前版本并说明剩余限制。

**Web fallback:** In signed-in [ChatGPT](https://chatgpt.com) settings, find Pets, sometimes under Personalization. Inspect existing entries and available edit controls first. Upload and name a new entry 「月薪喵 Work · 捂鼻扇风」 only for a first installation. UI locations, edit capabilities, and accepted formats can change. Do not assume an upload or replacement button exists; preserve the current edition and report the remaining limitation when the capability is absent.

本图集为透明 WebP，1536×1872，小于 20 MiB，`spriteVersionNumber: 1`。这些是本包参数，不代表当前上传接口一定接受该格式；应以实际工具验证结果为准。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets)

The atlas is a transparent 1536×1872 WebP under 20 MiB, with `spriteVersionNumber: 1`. These package properties do not establish acceptance by the current upload API; use actual tool validation results. [Official Pets documentation](https://learn.chatgpt.com/docs/pets)

## 3. 手机端查看与测试 · View and test on mobile

确认账号中的内容及选中状态后，再进行手机检查。这是 Work 内的宠物显示，不是 iPhone 主屏幕上的悬浮桌宠。

After verifying the saved account entry and active selection, check the mobile app. This concerns the pet inside Work, not a floating pet on the iPhone home screen.

1. 在手机 ChatGPT 中确认使用相同账号、相同工作区，退出当前 Work 页面后重新进入。<br>
   In ChatGPT on your phone, use the same account and workspace, then leave and reopen Work.

2. 查看 Work 中是否出现新版月薪喵。若仍是旧版，先确认网页端选中新版且刷新后保持，再完全关闭并重新打开手机 App。<br>
   Look for the updated pet. If the old version remains, first confirm the new selection survives a web page reload, then fully close and reopen the mobile app.

3. 在 Work 发起一个简短任务，例如「计算 1 到 100 的平方和，并解释公式」，观察任务进行时宠物是否显示及运动；完成后观察状态变化。<br>
   Start a short Work task, such as “Calculate the sum of squares from 1 to 100 and explain the formula.” Observe the pet during the task and after completion.

4. 手机没有显示时，不要反复重装 Mac 本地包。确认账号、工作区与 App 版本，并检查系统是否开启减少动态效果。网页可用不能作为手机已通过测试的证据。<br>
   If it does not appear, reinstalling the Mac package is not a mobile fix. Check the account, workspace, app version, and reduced-motion setting. A successful web test is not proof of mobile support.

**代理验收流程：**如果原生电脑控制工具可用，优先通过 iPhone 镜像打开手机 Work，观察真实任务运行并采集至少两帧以验证动画。手机锁定或正被使用时，只请求必要操作。浏览器手机尺寸预览不能替代实机测试。工具缺失时明确标注，不能用旧测试记录代替本版本验收。

**Agent validation:** Prefer iPhone Mirroring through an available native Computer Use tool. Observe an actual mobile Work task and capture at least two frames for motion verification. Request only the necessary action if the phone is locked or in use. A narrow browser viewport is not a mobile device test. Report missing tooling and do not reuse historical testing as current-release evidence.

**历史实机验证范围（2026-09-26，不代表新版客户端复测）：**Work 专用版已上传、激活并刷新确认；手机个性化设置显示新版。iPhone 镜像中，Python 处理及联网搜索阶段均实际播放捂鼻扇风，任务完成后图标隐藏。本机九状态版图集未改变。原九状态图集和官方默认宠物对照时，在已测试场景中都未见明显动作组切换；这不证明手机只能使用一种状态。等待授权、失败等其他分支仍未确认，详见 [手机实测说明](MOBILE_WORK.md)。

**Historical device verification, September 26, 2026 (not a retest of newer clients):** the Work edition was uploaded, activated, and verified after reload and in mobile settings. Actual iPhone Mirroring tests showed fanning during Python processing and web search; the icon disappeared after completion. The local nine-state atlas remained unchanged. The original atlas and official default pet showed no clear animation-group switch in tested scenarios; this does not prove that mobile supports only one state. Approval waits, failures, and other branches remain unverified; see the [mobile test report](MOBILE_WORK.md).

## 4. 交给 Codex 复用 · Reuse with Codex

下载仓库后，把仓库链接或本地目录交给 Codex，并使用这段提示词：

After downloading the repository, give Codex its link or local folder and use this prompt:

> 请按 docs/INSTALL.md 安装「月薪喵 Codex Pet」，复用 dist 中的现成图集，不重新生成。如已装不同旧版，沿用我的更新选择；尚无选择则问我替换并备份还是并存。Work 优先用官方 MCP 读取全部宠物，确认目标 ID 和当前选择；有原条目就用 update_pet 原 ID 更新，不重复新建。先验证当前工具接受 v1，再替换图集；否则保持现有宠物并说明限制。需要使用网页时按同样原则操作。启用「月薪喵 Work · 捂鼻扇风」并核验保存；旧条目仅按我对具体 ID 的明确授权处理。手机优先通过 iPhone 镜像验证；分别报告本地安装、账号内容、网页显示和手机实测，未测项如实标注。

> Follow docs/INSTALL.md to install Yuexinmiao Codex Pet using the prebuilt assets in dist without regenerating them. If a different older version is installed, honor my existing update choice, or ask whether to replace it with a backup or keep both if I have not chosen. For Work, use official MCP tools first to list all pets and resolve the target ID and active selection. Update an existing entry with update_pet using the same ID; do not create duplicates. Verify current-tool support for v1 before replacing the atlas; otherwise preserve the existing pet and explain the limitation. Apply the same principles if web controls are needed. Activate 「月薪喵 Work · 捂鼻扇风」 and verify persistence. Handle older entries only with my explicit authorization for their specific IDs. Prefer iPhone Mirroring for device testing; report local installation, saved account content, web display, and mobile testing separately, identifying untested steps.

代理入口：[安装技能](../skills/install-yuexinmiao/SKILL.md)。普通安装不需要图片生成；账号操作需要已授权的官方工具连接，或回退到已登录的官方网页。安装脚本本身不上传，但客户端可能随后迁移本机宠物，应重新盘点账号列表。

Agent entry point: [installation skill](../skills/install-yuexinmiao/SKILL.md). Normal installation needs no image generation. Account actions require an authorized official tool connection or, as fallback, the signed-in official web UI. The installer itself does not upload; the client may later migrate local pets, so inventory the account library again.

## 自动化安装的明确选择 · Explicit choice for automation

检测到不同旧版，但既无交互终端也未指定更新策略时，安装器停止且不修改文件。代理取得用户选择后使用对应参数：

If a different version is installed and neither an interactive terminal nor an explicit update policy is available, the installer stops without changing files. After obtaining the user’s choice, use the corresponding option below:

```sh
python3 scripts/install.py --existing replace
python3 scripts/install.py --existing keep-both
```

两条命令二选一。replace 将旧条目移到回滚备份；keep-both 保留旧条目并安装独立副本。安装器只管理本机目录，不能删除 Work 账号条目。历史上使用不同 ID 的手动安装版本，由代理列出并在用户确认后处理，不能按名称模糊匹配批量删除。

Choose one command: `replace` moves the previous entry to a rollback backup; `keep-both` retains it and installs a separate copy. The installer manages local directories only, not account pets. Independently installed legacy IDs must be inventoried and handled with user confirmation; never delete by a fuzzy display-name match.


## 工具使用顺序 · Tool preference

代理优先检查可用 MCP 功能工具，再使用受支持的 API 或 CLI。仅当这些方式不能完成操作，或需要验证实际界面／动画时使用 GUI；手机动画验收仍需真实设备证据。不能因为工具名称不同而假定能力不存在，也不能为追求自动化绕过认证或权限。

Agents should check available MCP capabilities first, then use supported APIs or CLIs. Use GUI control when those routes cannot complete an operation or when actual UI/animation verification is required. Mobile animation acceptance still requires real-device evidence. Different tool names do not prove a capability is absent, and automation must not bypass authentication or permissions.
