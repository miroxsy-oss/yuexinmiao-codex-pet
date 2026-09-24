# 月薪喵桌面宠物 · Yuexinmiao Desktop Pet

**让月薪喵陪你写代码，也陪你摸会儿鱼。**  
**A little desktop companion for coding sessions and well-earned breaks.**

为 **Codex 桌面应用**适配的动态宠物，提供 9 种动作状态。直接安装现成动画，无需重新生成图片。

An animated pet for the **Codex desktop app**, with nine animation states. Install the ready-made artwork without generating new images.

由 **[@miroxsy-oss](https://github.com/miroxsy-oss)** 搜集网络素材，完成动作编排、尺寸适配、测试与打包，并维护分享。

Collected from online sources, with animation sequencing, sizing, testing, packaging, and maintenance by **[@miroxsy-oss](https://github.com/miroxsy-oss)**.

**个人使用 · 非商业用途 · 非官方项目**  
**Personal use · Noncommercial · Unofficial project**

## 动态效果 · Preview

| 摸鱼待机 · Idle | 向右移动 · Move right | 向左移动 · Move left |
| :---: | :---: | :---: |
| ![摸鱼待机 / Idle](previews/animations/idle.gif) | ![向右移动 / Move right](previews/animations/running-right.gif) | ![向左移动 / Move left](previews/animations/running-left.gif) |
| **打招呼 · Greeting** | **捂鼻扇风 · Nose-covering gesture** | **抱头崩溃 · Error reaction** |
| ![打招呼 / Greeting](previews/animations/waving.gif) | ![捂鼻扇风 / Nose-covering gesture](previews/animations/jumping.gif) | ![失败反馈 / Error reaction](previews/animations/failed.gif) |
| **等你回来 · Waiting** | **正在工作 · Working** | **看看结果 · Review** |
| ![等待 / Waiting](previews/animations/waiting.gif) | ![工作 / Working](previews/animations/running.gif) | ![审阅 / Review](previews/animations/review.gif) |

## 快速安装 · Quick start

下载仓库 ZIP 并解压，在解压后的目录运行以下命令。安装完成后，在 Codex 的宠物选择器中选择 **「月薪喵桌面宠物」**。

Download and extract the repository ZIP, then run the following command from the extracted directory. In the Codex pet picker, select **「月薪喵桌面宠物」**.

```sh
python scripts/install.py
```

macOS 如果没有 `python` 命令，请使用 `python3`。安装器会核验文件完整性，并在更新不同的同名版本前创建备份。安装仅使用 Python 标准库，不需要 API Key 或图片生成服务。

On macOS, use `python3` if `python` is unavailable. The installer verifies file integrity and backs up a different existing version before replacing it. Installation uses only the Python standard library; no API key or image-generation service is required.

### 让 Codex 帮你安装 · Ask Codex to install it

把本仓库链接发给 Codex，并告诉它：

> 请安装这个仓库里的「月薪喵桌面宠物」，保留我原来的宠物，直接使用现成素材。

Give Codex the repository link and ask:

> Install the Yuexinmiao desktop pet from this repository. Keep my existing pet and use the ready-made assets.

仓库提供 [安装技能](skills/install-yuexinmiao/SKILL.md)，供代理读取后复用安装流程。  
An [installation skill](skills/install-yuexinmiao/SKILL.md) is included so agents can follow the existing installation workflow.

<details>
<summary>手动安装与路径 · Manual installation and paths</summary>

将 `dist/yuexinmiao-selected/` 文件夹复制到下列目录。  
Copy the `dist/yuexinmiao-selected/` folder into the appropriate directory below.

| 系统 · Platform | 默认目录 · Default directory |
| --- | --- |
| macOS | `~/.codex/pets/` |
| Windows | `%USERPROFILE%\.codex\pets\` |

如果设置了 `CODEX_HOME`，使用其下的 `pets/` 目录。宠物文件夹内应包含 `pet.json` 和 `spritesheet.webp`。

If `CODEX_HOME` is set, use its `pets/` subdirectory. The pet folder must contain `pet.json` and `spritesheet.webp`.

内部目录名保留为 `yuexinmiao-selected`，界面显示名称为「月薪喵桌面宠物」。若列表没有刷新，请重新打开宠物选择器或重启 Codex。

The internal folder name remains `yuexinmiao-selected`; the display name is 「月薪喵桌面宠物」. Reopen the pet picker or restart Codex if the list does not refresh.

</details>

## 动作说明 · Animation states

| 应用状态 · State | 宠物表现 · Animation |
| --- | --- |
| `idle` | 电脑前抱鱼摸鱼 · Relaxing with a fish by the monitor |
| `running-right` | 向右移动 · Moving right |
| `running-left` | 向左移动 · Moving left |
| `waving` | 举爪打招呼 · Raising paws in greeting |
| `jumping` | 经典捂鼻扇风 · Covering the nose and fanning |
| `failed` | 抱头崩溃 · Holding the head in frustration |
| `waiting` | 坐着看手机 · Sitting and checking the phone |
| `running` | 边吃零食边敲键盘 · Snacking while typing |
| `review` | 电脑前挠头审阅 · Scratching the head at the computer |

`jumping` 是应用的状态名称，本项目为它配置了捂鼻扇风动作。  
`jumping` is the app's state name; this pet uses the nose-covering and fanning gesture for that state.

## 检查与兼容性 · Validation and compatibility

采用 Codex 自定义宠物 v1 格式：9 种状态、57 个有效帧位、透明 WebP 图集。  
Uses the Codex custom-pet v1 format: nine states, 57 active frame slots, and a transparent WebP atlas.

| 检查项 · Check | 结果 · Result |
| --- | --- |
| 逐帧检查 · Frame inspection | 0 错误、0 警告 · 0 errors, 0 warnings |
| 已安装图集检查 · Installed atlas validation | 0 错误、0 警告 · 0 errors, 0 warnings |
| 独立包检查 · Independent package checks | 44 项通过 · 44 checks passed |
| 源帧重建 · Rebuild from source frames | 与已验证图集逐字节一致 · Byte-identical to the validated atlas |

仓库附带自动检查配置、黑白底预览与完整检查记录。部分动作保留细白边、半身造型等原有视觉特征，详见 [自检报告（中文）](docs/SELF_CHECK.md)。

The repository includes automated checks, previews on black and white backgrounds, and validation records. Some animations retain thin light outlines or partial-body compositions from the source artwork. See the [validation report (Chinese)](docs/SELF_CHECK.md) for details.

适用于支持自定义宠物的 **Codex 桌面应用**；不是独立桌宠程序，也不是 ChatGPT 网页或手机 App 的通用皮肤。

Designed for the **Codex desktop app** with custom-pet support. This is not a standalone desktop-pet application or a general theme for ChatGPT on the web or mobile.

## 开发与自定义 · Development and customization

只想使用宠物，完成安装即可。需要重建或检查图集时，使用 Python 3.10 或以上运行：

For everyday use, installation is all you need. To rebuild or validate the atlas, run the following with Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
```

最终源帧位于 `source/frames/`，动作映射见 `source/selection.json`，检查结果保存在 `qa/`。

Approved source frames are in `source/frames/`, animation mappings are in `source/selection.json`, and validation results are in `qa/`.

## 使用说明与致谢 · Usage and credits

本项目由 **@miroxsy-oss** 完成素材整理、动作适配、测试、打包与维护。原角色及图像素材的权利归相应权利人所有，本项目不主张拥有这些原始素材的版权，也不代表官方授权或合作。

**@miroxsy-oss** handles asset curation, animation adaptation, testing, packaging, and maintenance. Rights to the original character and image assets remain with their respective rights holders. This project claims no ownership of that original artwork and implies no official authorization or affiliation.

仅供个人、非商业使用。禁止将分享者有权许可的本项目内容用于销售、收费分发、商业推广或商用产品。第三方素材的使用与再分发范围以原权利人授权为准；目前完整素材包的公开再分发许可尚未确认。

For personal, noncommercial use only. Contributions that the maintainer has the right to license may not be sold, distributed for a fee, or used in commercial promotions or products. Third-party asset use and redistribution remain subject to the relevant rights holders' permissions; permission to publicly redistribute the complete asset package has not yet been confirmed.

详细说明见 [使用条款（中文）](LICENSE.md) 与 [素材来源及致谢（中文）](docs/ATTRIBUTION.md)。  
See the [usage terms (Chinese)](LICENSE.md) and [asset attribution (Chinese)](docs/ATTRIBUTION.md) for details.

## 支持这个项目 · Support the project

如果你喜欢这只猫，或它帮你省下了反复生成、选帧和调试的时间，欢迎点一个 **Star ⭐**。遇到显示或安装问题，欢迎通过 Issue 反馈；分享时也欢迎附上原仓库链接。

If you enjoy this little companion, or it saves you time generating, selecting, and tuning animation frames, please consider giving the project a **Star ⭐**. Report display or installation issues through Issues, and link back to the repository when sharing it.

---

**桌面宠物 · Codex 自定义宠物 · 桌面美化**  
**Desktop Pet · Codex Custom Pet · Desktop Customization · Yuexinmiao**
