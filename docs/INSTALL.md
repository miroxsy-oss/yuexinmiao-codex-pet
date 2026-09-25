# v1.0.0 安装与更新 · v1.0.0 installation and updates

## 本机 · Desktop

1. 下载并解压 `yuexinmiao-codex-pet-v1.0.0.zip`。<br>
   Download and extract `yuexinmiao-codex-pet-v1.0.0.zip`.
2. 在目录中运行 `python3 scripts/install.py`；Windows 可用 `python`。<br>
   Run `python3 scripts/install.py` in the directory; on Windows, use `python`.
3. 已有不同版本时，选择替换并备份或并存。未明确选择的非交互更新会停止。<br>
   If another version exists, choose replacement with a backup or keeping both. Noninteractive updates stop without an explicit choice.
4. 在 Codex 宠物设置中选择「月薪喵 Codex Pet」；列表未更新时重新打开选择器。<br>
   Select 「月薪喵 Codex Pet」 in Codex pet settings; reopen the picker if its list is stale.

默认位置为 `~/.codex/pets/yuexinmiao-selected/`，也支持 CODEX_HOME。替换备份位于 Codex 数据目录下的 pet-backups，而不是 pets。安装不改变当前界面选择。

The default location is `~/.codex/pets/yuexinmiao-selected/`; CODEX_HOME is supported. Replacement backups go in pet-backups under the Codex data directory, outside pets. Installation does not change the active UI selection.

手动安装时复制整个 dist/yuexinmiao-selected 文件夹到 pets，保留 pet.json 与 spritesheet.webp。已有版本先备份，避免覆盖后无法恢复。

For manual installation, copy the entire dist/yuexinmiao-selected folder into pets, retaining pet.json and spritesheet.webp. Back up an existing copy before replacement so it can be restored.

## Work 账号 · Work account

1. 电脑浏览器登录与手机相同账号和工作区，在宠物设置上传 `dist/yuexinmiao-selected/spritesheet.webp`。<br>
   Sign in through a desktop browser with the same account and workspace as your phone, then upload `dist/yuexinmiao-selected/spritesheet.webp` in pet settings.
2. 选中宠物并刷新确认；本机安装不代替这一步。<br>
   Select the pet and reload to verify persistence; local installation does not replace this step.
3. 手机重新进入 Work，发起短任务并观察至少两个不同动作帧。历史测试显示本版为挠头思考；其他状态未全覆盖。<br>
   Reopen Work on mobile, start a short task, and observe at least two distinct frames. Historical tests showed head-scratching for this edition; other states were not fully covered.
4. 更新前检查是否支持替换已有图集；若必须新建，先验证新版，再由用户决定删除指定旧条目或保留。永久删除前确认。<br>
   Check for an existing-atlas replacement option first. If a new entry is necessary, validate it before asking whether to delete identified older entries or keep them. Confirm permanent deletion before execution.

代理优先使用 MCP，再使用受支持 API/CLI；GUI 用于必要操作及实际显示验证。手机实测优先 iPhone 镜像；不能用网页成功代替手机实测。

Agents should prefer MCP, then supported APIs/CLIs, and use GUI control for necessary interactions and actual display verification. Prefer iPhone Mirroring for mobile tests; web success does not prove phone behavior.

自动化更新参数二选一：`--existing replace` 或 `--existing keep-both`，应先取得用户的明确选择。安装与图集格式检查不代表第三方素材授权。

For automated updates, choose either `--existing replace` or `--existing keep-both` after obtaining the user's explicit choice. Installation and atlas checks do not establish third-party artwork permissions.
