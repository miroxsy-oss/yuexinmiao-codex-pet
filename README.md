# 月薪喵 · Yuexinmiao Codex Pet

**[下载 v1.1.0 · Download](https://github.com/miroxsy-oss/yuexinmiao-codex-pet/releases/tag/v1.1.0)** · [本次更新 / Release notes](docs/RELEASE-v1.1.0.md)

**让月薪喵陪你写代码，也陪你摸会儿鱼。**<br>
**A little desktop companion for coding sessions and well-earned breaks.**

为 **Codex 桌面应用**适配的动态宠物，提供 9 种动作状态，并附手机 **ChatGPT Work 捂鼻扇风专用版**。直接使用现成动画，无需重新生成图片。

An animated pet for the **Codex desktop app**, with nine animation states and a signature fanning edition for mobile ChatGPT Work. Install the ready-made artwork without generating new images.

由 **[@miroxsy-oss](https://github.com/miroxsy-oss)** 搜集网络素材，完成动作编排、尺寸适配、测试与打包，并维护分享。

Collected from online sources, with animation sequencing, sizing, testing, packaging, and maintenance by **[@miroxsy-oss](https://github.com/miroxsy-oss)**.

**个人使用 · 非商业用途 · 非官方项目**<br>
**Personal use · Noncommercial · Unofficial project**

## 使用效果预览 · In-use preview

<table>
<thead>
<tr>
<th width="50%" align="center">Codex 桌面浮窗 · Desktop overlay</th>
<th width="50%" align="center">iPhone Work 任务内 · In-task pet</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><img src="previews/animations/v1.1.0/desktop-idle.gif" width="160" alt="摸鱼待机动图 · Animated desktop idle"></td>
<td align="center"><img src="previews/animations/v1.1.0/work-mini.gif" width="64" alt="迷你捂鼻扇风动图 · Miniature Work fanning animation"></td>
</tr>
<tr>
<td align="center"><strong>摸鱼待机 · Relaxing while idle</strong></td>
<td align="center"><strong>处理中捂鼻扇风 · Fanning during processing</strong></td>
</tr>
</tbody>
</table>

原始素材动图预览，非屏幕录像。桌面采用已测试的待机节奏；手机实际尺寸与播放由 Work 控制。<br>
Animated artwork previews, not screen recordings. Desktop uses the tested idle timing; Work controls actual mobile size and playback.

## 桌面九种动作 · Nine desktop animations

**[实际尺寸与播放预览 / Size and playback preview](previews/size-and-playback.html)**：下载后用浏览器打开，可切换 32–192 px、深浅背景和实际播放规则。下方 GIF 仅用于循环展示动作，不承诺应用持续显示该状态。

Download and open the preview in a browser to compare 32–192 px sizes, light/dark backgrounds, and the tested app playback behavior. The looping GIFs below showcase artwork, not continuous task-status behavior.


| 摸鱼待机 · Idle | 向右移动 · Move right | 向左移动 · Move left |
| :---: | :---: | :---: |
| ![摸鱼待机 / Idle](previews/animations/v1.1.0/idle.gif) | ![向右移动 / Move right](previews/animations/v1.1.0/running-right.gif) | ![向左移动 / Move left](previews/animations/v1.1.0/running-left.gif) |
| **打招呼 · Greeting** | **捂鼻扇风 · Nose-covering and fanning** | **抱头崩溃 · Error reaction** |
| ![打招呼 / Greeting](previews/animations/v1.1.0/waving.gif) | ![捂鼻扇风 / Nose-covering and fanning](previews/animations/v1.1.0/jumping.gif) | ![失败反馈 / Error reaction](previews/animations/v1.1.0/failed.gif) |
| **等你回来 · Waiting** | **正在工作 · Working** | **看看结果 · Review** |
| ![等待 / Waiting](previews/animations/v1.1.0/waiting.gif) | ![工作 / Working](previews/animations/v1.1.0/running.gif) | ![审阅 / Review](previews/animations/v1.1.0/review.gif) |

## 快速安装 · Quick start

下载上方 Release 中的 `yuexinmiao-codex-pet-v1.1.0.zip` 并解压，在解压后的目录运行以下命令。安装完成后，在 Codex 的宠物选择器中选择 **「月薪喵 Codex Pet」**。

Download and extract `yuexinmiao-codex-pet-v1.1.0.zip` from the release above, then run this command in the extracted directory. In the Codex pet picker, select **「月薪喵 Codex Pet」**.

```sh
python scripts/install.py
```

macOS 如果没有 `python` 命令，请使用 `python3`。安装器会核验文件完整性；发现不同的旧版时，先询问替换并备份还是并存保留。安装仅使用 Python 标准库，不需要 API Key 或图片生成服务。

On macOS, use `python3` if `python` is unavailable. The installer verifies file integrity and asks whether to replace an older version with a backup or keep both. Installation uses only the Python standard library; no API key or image-generation service is required.

### 让 Codex 帮你安装 · Ask Codex to install it

把本仓库链接发给 Codex，并告诉它：<br>
Give Codex the repository link and ask:

> 请安装这个仓库里的「月薪喵 Codex Pet」，保留我原来的宠物，直接使用现成素材。
>
> Install the Yuexinmiao Codex Pet from this repository. Keep my existing pet and use the ready-made assets.

仓库提供 [安装技能](skills/install-yuexinmiao/SKILL.md)，供代理读取后复用安装流程。<br>
An [installation skill](skills/install-yuexinmiao/SKILL.md) is included so agents can follow the existing installation workflow.

<details>
<summary>手动安装与路径 · Manual installation and paths</summary>

将 `dist/yuexinmiao-selected/` 文件夹复制到下列目录。<br>
Copy the `dist/yuexinmiao-selected/` folder into the appropriate directory below.

| 系统 · Platform | 默认目录 · Default directory |
| --- | --- |
| macOS | `~/.codex/pets/` |
| Windows | `%USERPROFILE%\.codex\pets\` |

如果设置了 `CODEX_HOME`，使用其下的 `pets/` 目录。宠物文件夹内应包含 `pet.json` 和 `spritesheet.webp`。

If `CODEX_HOME` is set, use its `pets/` subdirectory. The pet folder must contain `pet.json` and `spritesheet.webp`.

内部目录名保留为 `yuexinmiao-selected`，界面显示名称为「月薪喵 Codex Pet」。若列表没有刷新，请重新打开宠物选择器或重启 Codex。

The internal folder name remains `yuexinmiao-selected`; the display name is 「月薪喵 Codex Pet」. Reopen the pet picker or restart Codex if the list does not refresh.

</details>

## 手机 Work 与跨端使用 · Mobile Work and cross-device setup

**桌面用九状态版，手机 Work 推荐捂鼻扇风专用版。** 两者分别安装、分别选择；本机安装不会自动同步到账号。

**Use the nine-state desktop edition locally and the fanning edition for mobile Work.** Local installation and account upload are separate.

| 使用位置 · Where | 文件 · File | 显示方式 · Appearance |
| --- | --- | --- |
| 本机 Codex · Desktop | `dist/yuexinmiao-selected/` | 保留九种动作，由桌面应用触发 · Nine animations, triggered by the desktop app |
| 手机／网页 Work · Mobile / web | `dist/yuexinmiao-work-fanning/spritesheet.webp` | 手机已测试的处理中场景播放捂鼻扇风 · Fanning during tested mobile processing stages |

### 相比 v1.0.0 的变化 · What changed since v1.0.0

**手机 Work：挠头思考 → 捂鼻扇风；桌面：保留全部九种动作。** 已测试的手机思考、搜索和 Python 处理中只观察到同一组动画，因此 v1.1.0 的 Work 专用版改用更有辨识度的招牌动作。上方小动图展示的就是这组素材，原始帧保持不变。<br>
**Mobile Work: head-scratching → nose-covering and fanning. Desktop: all nine animations retained.** Only one animation group was observed during tested mobile reasoning, search, and Python processing, so the v1.1.0 Work edition uses the more recognizable signature gesture. The miniature preview above shows these unchanged source frames.

2026-09-26 的 iPhone 镜像实测已确认新版在 Python 处理与搜索时播放捂鼻扇风，完成后图标隐藏。官方默认宠物在同类场景中也未见明显的动作组切换。**这不等于手机官方只支持一种状态**；等待授权、失败等其他分支仍待验证。<br>
iPhone Mirroring tests on September 26, 2026 confirmed fanning during Python processing and search, with the icon hidden after completion. The official default pet also showed no clear animation-group switch in comparable scenarios. **This does not establish that mobile officially supports only one state**; approval waits, failures, and other branches remain unverified.

[实机截图与完整测试范围 · Device captures and full test scope](docs/MOBILE_WORK.md)

### 怎么使用 · Setup

在电脑浏览器的 ChatGPT「设置 → 虚拟宠物」上传 **`dist/yuexinmiao-work-fanning/spritesheet.webp`**，命名为「月薪喵 Work · 捂鼻扇风」，选中并刷新确认。手机使用相同账号与工作区，重新进入 Work；可在「设置 → 个性化 → 宠物」核对当前选择。若仍显示旧图标，重新打开 App 后再测试。

Upload **`dist/yuexinmiao-work-fanning/spritesheet.webp`** in ChatGPT’s web pet settings, name it 「月薪喵 Work · 捂鼻扇风」, select it, and verify after reloading. Use the same account and workspace on your phone and check the selection under Settings → Personalization → Pet. Reopen the app if cached artwork remains.

Work 使用账号级图集，网页版也会读取这一版；本机 Codex 九状态版独立保留。更新时优先检查原条目是否支持替换图集；若必须新建，先验证新版，再按用户选择清理旧版并保留本机备份。

The Work atlas is account-level and also applies on the web; the local nine-state Codex edition remains separate. Prefer replacing the existing atlas when supported; otherwise validate the new entry before removing an old version according to the user’s choice, keeping local backups.

👉 **[完整安装、更新与手机验收指南 · Full setup and verification guide](docs/INSTALL.md)** · **[实测范围 · Test scope](docs/MOBILE_WORK.md)**

## 检查与兼容性 · Validation and compatibility

**[官方公开要求逐项审计 / Audit against public OpenAI requirements](docs/OFFICIAL_AUDIT.md)**：v1 为官方明确支持的格式；本地 v2 创作建议不能作为否定 v1 兼容性的依据。

Version 1 is explicitly supported by the official install documentation. Local v2 creation guidance does not invalidate v1 compatibility.


采用 Codex 自定义宠物 v1 格式：9 种状态、57 个有效帧位、透明 WebP 图集。<br>
Uses the Codex custom-pet v1 format: nine states, 57 active frame slots, and a transparent WebP atlas.

| 检查项 · Check | 结果 · Result |
| --- | --- |
| 图集结构 · Atlas structure | 有效帧非空、未用格透明、无切格越界 · Active frames nonempty, unused cells transparent, no cell-edge clipping |
| 安装更新测试 · Installer update tests | 6 项通过 · 6 passed |
| 独立包检查 · Independent package checks | 桌面 44、Work 14 项通过 · Desktop 44, Work 14 passed |
| 源帧重建 · Rebuild from source frames | 与已验证图集逐字节一致 · Byte-identical to the validated atlas |

仓库附带自动检查配置、黑白底预览与完整检查记录。已修正待机和打招呼动作的外轮廓白边；打招呼仍保留原素材的半身造型，详见 [自检报告](docs/SELF_CHECK.md)。

The repository includes automated checks, previews on black and white backgrounds, and validation records. Exterior light fringes in idle and greeting have been corrected; the greeting retains its original partial-body composition. See the [validation report](docs/SELF_CHECK.md) for details.

适用于支持自定义宠物的 **Codex 桌面应用**；Work 专用图集也已通过 ChatGPT 网页官方上传入口用于 Work。手机使用路径与验证边界见上方教程。本项目不是独立桌宠程序或通用 App 皮肤。

Designed for the **Codex desktop app** with custom-pet support. The Work-specific atlas has also been uploaded through ChatGPT’s official web UI for Work. See the guide above for the mobile workflow and validation limits. This is not a standalone Codex Pet application or a general app theme.

### 状态显示限制 · Status-display limitation

**已知桌面播放器行为：动作不一定持续对应整个任务过程。**
**Known desktop-player behavior: an animation may not represent the entire task duration.**

本机桌面应用的实际播放器会将非待机动作播放三遍后回到待机；例如工作动作约 2.46 秒后会显示抱鱼待机，即使任务仍在运行。图集映射正确不代表宠物持续显示任务状态。手机 Work 专用版已验证捂鼻扇风播放；未确认全部手机状态及其回退时序。详见 [状态核验报告 / State audit](docs/STATE_AUDIT.md)。

The tested desktop player returns to idle after three repetitions of a non-idle animation. For example, working falls back after about 2.46 seconds even if the task continues. Correct atlas mapping does not guarantee continuous task-state display. The mobile Work fanning edition was verified in action; its complete state mapping and fallback timing remain unverified.

## 开发与自定义 · Development and customization

只想使用宠物，完成安装即可。需要重建或检查图集时，使用 Python 3.10 或以上运行：

For everyday use, installation is all you need. To rebuild or validate the atlas, run the following with Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
python scripts/check_docs.py
python scripts/build_work.py
python scripts/check_work.py
python -m unittest discover -s tests -q
```

最终源帧位于 `source/frames/`，动作映射见 `source/selection.json`，当前检查结果保存在 `qa/`，旧实测记录单独保存在 `qa/history/`。

Approved source frames are in `source/frames/`, animation mappings are in `source/selection.json`, and current validation results are in `qa/`, with earlier device evidence separated into `qa/history/`.

## 使用与权利 · Usage and rights

本项目由 **@miroxsy-oss** 完成素材整理、动作适配、测试、打包与维护。原角色及图像素材的权利归相应权利人所有，本项目不主张拥有这些原始素材的版权，也不代表官方授权或合作。

**@miroxsy-oss** handles asset curation, animation adaptation, testing, packaging, and maintenance. Rights to the original character and image assets remain with their respective rights holders. This project claims no ownership of that original artwork and implies no official authorization or affiliation.

仅供个人、非商业使用。禁止将分享者有权许可的本项目内容用于销售、收费分发、商业推广或商用产品。第三方素材的使用与再分发范围以原权利人授权为准；目前完整素材包的公开再分发许可尚未确认。

For personal, noncommercial use only. Contributions that the maintainer has the right to license may not be sold, distributed for a fee, or used in commercial promotions or products. Third-party asset use and redistribution remain subject to the relevant rights holders' permissions; permission to publicly redistribute the complete asset package has not yet been confirmed.

详细说明见 [使用条款](LICENSE.md) 与 [素材与权利说明](docs/ATTRIBUTION.md)。<br>
See the [usage terms](LICENSE.md) and [artwork and rights](docs/ATTRIBUTION.md) for details.

## 支持这个项目 · Support the project

如果你喜欢这只猫，或它帮你省下了反复生成、选帧和调试的时间，欢迎点一个 **Star ⭐**。遇到显示或安装问题，欢迎通过 Issue 反馈；分享时也欢迎附上原仓库链接。

If you enjoy this little companion, or it saves you time generating, selecting, and tuning animation frames, please consider giving the project a **Star ⭐**. Report display or installation issues through Issues, and link back to the repository when sharing it.

---

**桌面宠物 · Codex 自定义宠物 · 桌面美化**<br>
**Codex Pet · Codex Custom Pet · Desktop Customization · Yuexinmiao**

更新时的旧版处理与 iPhone 镜像验收流程见 [安装指南](docs/INSTALL.md)。Work 新版验证后，由用户选择清理旧条目或保留；本机备份始终保留。

See the [installation guide](docs/INSTALL.md) for older-version handling and iPhone Mirroring verification. After validating the new Work entry, the user chooses whether to remove or retain older entries; local backups are retained.

## 项目宣传图 · Project poster

<details>
<summary>展开宣传图 · View the poster</summary>

![月薪喵项目宣传图 · Yuexinmiao launch poster](docs/images/launch-poster.png)

</details>

[参与维护 · Contributing](CONTRIBUTING.md) · [安全与反馈 · Security](SECURITY.md) · [图集规格 · Atlas contract](docs/REFERENCE.md) · [当前与历史检查 · Validation scope](qa/README.md)

自动化检查配置覆盖 Linux、macOS 和 Windows；具体通过状态以 GitHub Actions 结果为准。这些是包与安装器测试，不是三个系统上的应用 UI 实测。

The workflow targets Linux, macOS, and Windows; consult GitHub Actions for actual results. These are package and installer checks, not live application UI tests on all three systems.
