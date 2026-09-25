# 桌面与手机使用指南 · Desktop and mobile guide

两份用途不同的现成图集，两条安装路径：桌面宠物安装到本机；Work 宠物上传到自己的 ChatGPT 账号。只下载或安装桌面包，不会自动更新手机中的宠物。

Two ready-made editions, two setup paths: install locally for the Codex Pet, and upload to your ChatGPT account for Work. Downloading or installing the desktop package does not update the pet on your phone automatically.

## 1. 桌面端 · Desktop

1. 下载仓库 ZIP 并解压，进入解压目录。<br>
   Download and extract the repository ZIP; open the extracted folder.

2. macOS 运行 `python3 scripts/install.py`；Windows 运行 `python scripts/install.py`。需要先有 Python。<br>
   On macOS run `python3 scripts/install.py`; on Windows run `python scripts/install.py`. Python must be installed.

3. 打开 Codex 的「设置 → 宠物」，刷新列表，选择「月薪喵 Codex Pet」。需要显示桌面浮窗时，在聊天中输入 `/pet`。<br>
   Open Codex Settings → Pets, refresh the list, and select 「月薪喵 Codex Pet」. Enter `/pet` in a chat to toggle the desktop overlay.

4. 更新后仍显示旧版：重新选择宠物；若仍未更新，结束当前工作后完全退出并重新打开应用。<br>
   If an update still shows the old artwork, reselect the pet. If needed, finish active work before fully quitting and reopening the app.

安装器发现不同的旧版时，会先询问替换还是并存。替换会把旧版移到 pets 目录外的 pet-backups 中，宠物列表只保留新版；并存会给新版分配独立 ID。重复安装相同版本不会新增条目。不会自动替你切换界面选择。默认安装位置为 `~/.codex/pets/yuexinmiao-selected/`，设置了 `CODEX_HOME` 时以该目录为准。

For an existing different version, the installer asks whether to replace it with a backup in `pet-backups` outside the `pets` directory or keep both under separate IDs. Reinstalling the same version does not create another entry. It does not change the UI selection. The default location is `~/.codex/pets/yuexinmiao-selected/`, or the equivalent location under `CODEX_HOME` when configured.

## 2. 上传到 Work 账号 · Upload to your Work account

这一段建议在电脑浏览器完成，手机无需找本地宠物目录。

Complete this part in a desktop browser; you do not need to find a local pet folder on your phone.

1. 登录 [ChatGPT](https://chatgpt.com)，使用与手机相同的账号和工作区。<br>
   Sign in to [ChatGPT](https://chatgpt.com) with the same account and workspace as your phone.

2. 打开设置中的「虚拟宠物 / Pets」。部分界面版本位于「个性化 → Pet → Select pet」；也可以从 Work 首页的宠物打开选择器。<br>
   Open Pets in Settings. Some versions place it under Personalization → Pet → Select pet. The pet on the Work home screen may also open the picker.

3. 点击「上传虚拟宠物」，名称填写「月薪喵 Work · 捂鼻扇风」。选择仓库中的 **`dist/yuexinmiao-work-fanning/spritesheet.webp`**，不要选择 GIF 预览、截图、ZIP 或 `pet.json`。<br>
   Choose Upload pet, name it 「月薪喵 Work · 捂鼻扇风」, and select **`dist/yuexinmiao-work-fanning/spritesheet.webp`** from this repository—not a GIF preview, screenshot, ZIP, or `pet.json`.

4. 上传后选中新条目，刷新网页，确认仍然选中；回到 Work 首页查看「电脑前抱鱼」待机形象。<br>
   Select the uploaded entry, reload the page, and confirm it stays selected. On the Work home screen, look for the cat holding a fish beside the monitor.

5. 更新前先检查原条目是否有替换图集入口。当前手动编辑仅有名字和描述；若无法替换，上传新版、激活并验证刷新后持久保存。<br>
   First inspect whether the existing entry supports sprite replacement. The currently observed manual editor only exposes name and description. If replacement is unavailable, upload, activate, and verify the new version after reloading.

6. 新版验证后，询问用户要删除指定旧版还是保留。永久删除必须在执行时确认；只删除明确批准的旧月薪喵条目，不删除官方或其他宠物。最后刷新核验剩余列表和当前选中项。<br>
   After validation, ask whether to delete the identified older Yuexinmiao entries or keep them. Confirm permanent deletion at action time, remove only approved entries, and reload to verify the remaining library and active selection. Preserve official and unrelated pets.

本图集为透明 WebP，1536×1872，小于 20 MiB。上传功能是否提供取决于账号和工作区；入口名称可能变化。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets)

The atlas is a transparent 1536×1872 WebP, under 20 MiB. Upload availability depends on your account and workspace, and menu labels may change. [Official Pets documentation](https://learn.chatgpt.com/docs/pets)

## 3. 手机端查看与测试 · View and test on mobile

完成账号上传后，再进行手机检查。这是 Work 内的宠物显示，不是 iPhone 主屏幕上的悬浮桌宠。

After uploading to your account, check the mobile app. This concerns the pet inside Work, not a floating pet on the iPhone home screen.

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

**当前验证范围（2026-09-26）：**Work 专用版已上传、激活并刷新确认；手机个性化设置显示新版。iPhone 镜像中，Python 处理及联网搜索阶段均实际播放捂鼻扇风，任务完成后图标隐藏。本机九状态版图集未改变。原九状态图集和官方默认宠物对照时，在已测试场景中都未见明显动作组切换；这不证明手机只能使用一种状态。等待授权、失败等其他分支仍未确认，详见 [手机实测说明](MOBILE_WORK.md)。

**Verified September 26, 2026:** the Work edition was uploaded, activated, and verified after reload and in mobile settings. Actual iPhone Mirroring tests showed fanning during Python processing and web search; the icon disappeared after completion. The local nine-state atlas remained unchanged. The original atlas and official default pet showed no clear animation-group switch in tested scenarios; this does not prove that mobile supports only one state. Approval waits, failures, and other branches remain unverified; see the [mobile test report](MOBILE_WORK.md).

## 4. 交给 Codex 复用 · Reuse with Codex

下载仓库后，把仓库链接或本地目录交给 Codex，并使用这段提示词：

After downloading the repository, give Codex its link or local folder and use this prompt:

> 请按 docs/INSTALL.md 安装「月薪喵 Codex Pet」，复用 dist 中的现成图集，不重新生成。如已装旧版，先问我替换并备份还是并存；保留回滚备份。先安装桌面版；如具备已登录浏览器控制能力，再通过 ChatGPT 官方宠物上传界面将 dist/yuexinmiao-work-fanning/spritesheet.webp 上传到我的账号并选中。新版刷新验证后，问我删除指定旧条目还是保留，永久删除前确认。手机优先通过 iPhone 镜像验证。分别报告本地安装、网页显示、手机实机测试的结果。手机无法直接验证时明确标注待确认。遇到登录或工具权限限制，只告诉我真正剩余的必要操作。

> Follow docs/INSTALL.md to install Yuexinmiao Codex Pet using the prebuilt atlas in dist; do not regenerate it. If an older version exists, ask whether to replace it with a backup or keep both. Retain rollback backups. Install locally first. If authenticated browser control is available, use ChatGPT’s official pet upload UI to upload and select dist/yuexinmiao-work-fanning/spritesheet.webp in my account. Reload to verify persistence, ask whether to remove the identified old entries or keep them, and confirm permanent deletion at action time. Prefer iPhone Mirroring for device testing. Then report local installation, web display, and mobile device testing separately. Mark mobile testing as pending if you cannot verify it. If login or tool permissions block progress, report only the necessary remaining action.

代理入口：[安装技能](../skills/install-yuexinmiao/SKILL.md)。普通安装不需要图片生成；账号上传需要登录会话和可用的浏览器操作工具，安装脚本不会代为上传。

Agent entry point: [installation skill](../skills/install-yuexinmiao/SKILL.md). Normal installation requires no image generation. Account upload requires a signed-in session and a browser-control tool; the installer does not upload automatically.

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
