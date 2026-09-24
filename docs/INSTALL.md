# 桌面与手机使用指南 · Desktop and mobile guide

一份现成图集，两条安装路径：桌面宠物安装到本机；Work 宠物上传到自己的 ChatGPT 账号。只下载或安装桌面包，不会自动更新手机中的宠物。

One ready-made atlas, two setup paths: install locally for the desktop pet, and upload to your ChatGPT account for Work. Downloading or installing the desktop package does not update the pet on your phone automatically.

## 1. 桌面端 · Desktop

1. 下载仓库 ZIP 并解压，进入解压目录。
2. macOS 运行 `python3 scripts/install.py`；Windows 运行 `python scripts/install.py`。需要先有 Python。
3. 打开 Codex 的「设置 → 宠物」，刷新列表，选择「月薪喵桌面宠物」。需要显示桌面浮窗时，在聊天中输入 `/pet`。
4. 更新后仍显示旧版：重新选择宠物；若仍未更新，结束当前工作后完全退出并重新打开应用。

1. Download and extract the repository ZIP; open the extracted folder.
2. On macOS run `python3 scripts/install.py`; on Windows run `python scripts/install.py`. Python must be installed.
3. Open Codex Settings → Pets, refresh the list, and select 「月薪喵桌面宠物」. Enter `/pet` in a chat to toggle the desktop overlay.
4. If an update still shows the old artwork, reselect the pet. If needed, finish active work before fully quitting and reopening the app.

安装器验证文件并备份不同的同名版本；不会自动替你切换界面选择。默认安装位置为 `~/.codex/pets/yuexinmiao-selected/`，设置了 `CODEX_HOME` 时以该目录为准。

The installer verifies files and backs up a different existing version of the same pet. It does not change the UI selection. The default location is `~/.codex/pets/yuexinmiao-selected/`, or the equivalent location under `CODEX_HOME` when configured.

## 2. 上传到 Work 账号 · Upload to your Work account

这一段建议在电脑浏览器完成，手机无需找本地宠物目录。

Complete this part in a desktop browser; you do not need to find a local pet folder on your phone.

1. 登录 [ChatGPT](https://chatgpt.com)，使用与手机相同的账号和工作区。
2. 打开设置中的「虚拟宠物 / Pets」。部分界面版本位于「个性化 → Pet → Select pet」；也可以从 Work 首页的宠物打开选择器。
3. 点击「上传虚拟宠物」，名称填写「月薪喵桌面宠物」。选择仓库中的 **`dist/yuexinmiao-selected/spritesheet.webp`**，不要选择 GIF 预览、截图、ZIP 或 `pet.json`。
4. 上传后选中新条目，刷新网页，确认仍然选中；回到 Work 首页查看「电脑前抱鱼」待机形象。
5. 更新时可以上传新版并切换到它，保留旧条目方便回退；确认新版前不必删除旧宠物。

1. Sign in to [ChatGPT](https://chatgpt.com) with the same account and workspace as your phone.
2. Open Pets in Settings. Some versions place it under Personalization → Pet → Select pet. The pet on the Work home screen may also open the picker.
3. Choose Upload pet, name it 「月薪喵桌面宠物」, and select **`dist/yuexinmiao-selected/spritesheet.webp`** from this repository—not a GIF preview, screenshot, ZIP, or `pet.json`.
4. Select the uploaded entry, reload the page, and confirm it stays selected. On the Work home screen, look for the cat holding a fish beside the monitor.
5. For updates, upload and select the new version while keeping the old entry available for rollback.

本图集为透明 WebP，1536×1872，约 0.5 MB。上传功能是否提供取决于账号和工作区；入口名称可能变化。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets)

The atlas is a transparent 1536×1872 WebP, approximately 0.5 MB. Upload availability depends on your account and workspace, and menu labels may change. [Official Pets documentation](https://learn.chatgpt.com/docs/pets)

## 3. 手机端查看与测试 · View and test on mobile

完成账号上传后，再进行手机检查。这是 Work 内的宠物显示，不是 iPhone 主屏幕上的悬浮桌宠。

After uploading to your account, check the mobile app. This concerns the pet inside Work, not a floating pet on the iPhone home screen.

1. 在手机 ChatGPT 中确认使用相同账号、相同工作区，退出当前 Work 页面后重新进入。
2. 查看 Work 中是否出现新版月薪喵。若仍是旧版，先确认网页端选中新版且刷新后保持，再完全关闭并重新打开手机 App。
3. 在 Work 发起一个简短任务，例如「计算 1 到 100 的平方和，并解释公式」，观察任务进行时宠物是否显示及运动；完成后观察状态变化。
4. 手机没有显示时，不要反复重装 Mac 本地包。确认账号、工作区与 App 版本，并检查系统是否开启减少动态效果。网页可用不能作为手机已通过测试的证据。

1. In ChatGPT on your phone, use the same account and workspace, then leave and reopen Work.
2. Look for the updated pet. If the old version remains, first confirm the new selection survives a web page reload, then fully close and reopen the mobile app.
3. Start a short Work task, such as “Calculate the sum of squares from 1 to 100 and explain the formula.” Observe the pet during the task and after completion.
4. If it does not appear, reinstalling the Mac package is not a mobile fix. Check the account, workspace, app version, and reduced-motion setting. A successful web test is not proof of mobile support.

**当前验证范围：**桌面安装文件与配置已核对；新版账号上传、选中、刷新持久化及网页 Work 首页显示已验证。2026-09-25 通过 iPhone 镜像在手机 Work 发送测试消息，连续采集到「正在处理」旁月薪喵的不同动画帧，任务正常完成。手机运行状态已验证；未逐一验证九种状态，且该运行造型为新旧版共有，不能单凭它独立证明手机已切换全部新版动作。不承诺所有手机版本都支持。

**Validation so far:** local installation files and configuration checked; new account upload, selection persistence, and the web Work home-screen display verified. On 2026-09-25, test messages were sent in mobile Work through iPhone Mirroring. Sequential captures showed different Yuexinmiao frames beside the processing indicator, and the task completed normally. Mobile running animation is verified; all nine states were not tested. This working pose is shared by both versions, so it alone does not independently prove every updated action has reached the phone. Support across all mobile versions is not guaranteed.

## 4. 交给 Codex 复用 · Reuse with Codex

下载仓库后，把仓库链接或本地目录交给 Codex，并使用这段提示词：

After downloading the repository, give Codex its link or local folder and use this prompt:

> 请按 docs/INSTALL.md 安装「月薪喵桌面宠物」，复用 dist 中的现成图集，不重新生成。保留旧宠物和备份。先安装桌面版；如具备已登录浏览器控制能力，再通过 ChatGPT 官方宠物上传界面上传到我的账号并选中。刷新验证后，分别报告本地安装、网页显示、手机实机测试的结果。手机无法直接验证时明确标注待确认。遇到登录或工具权限限制，只告诉我真正剩余的必要操作。

> Follow docs/INSTALL.md to install Yuexinmiao Desktop Pet using the prebuilt atlas in dist; do not regenerate it. Preserve existing pets and backups. Install locally first. If authenticated browser control is available, use ChatGPT’s official pet upload UI to upload and select it in my account. Reload to verify persistence, then report local installation, web display, and mobile device testing separately. Mark mobile testing as pending if you cannot verify it. If login or tool permissions block progress, report only the necessary remaining action.

代理入口：[安装技能](../skills/install-yuexinmiao/SKILL.md)。普通安装不需要图片生成；账号上传需要登录会话和可用的浏览器操作工具，安装脚本不会代为上传。

Agent entry point: [installation skill](../skills/install-yuexinmiao/SKILL.md). Normal installation requires no image generation. Account upload requires a signed-in session and a browser-control tool; the installer does not upload automatically.
