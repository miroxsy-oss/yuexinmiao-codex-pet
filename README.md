# 月薪喵 · Yuexinmiao Codex Pet

**v1.0.0 · 桌面九动作版 · Nine-animation desktop edition**

网络素材搜集、整理与适配维护：[@miroxsy-oss](https://github.com/miroxsy-oss)。角色及原始表情不是维护者原创。个人非商业使用，非官方项目。

Online-artwork curation, organization, adaptation, and maintenance by [@miroxsy-oss](https://github.com/miroxsy-oss). The character and original expressions are not the maintainer's original work. Personal, noncommercial use; unofficial project.

## 动作预览 · Animation previews

| 摸鱼待机 · Idle | 向右移动 · Right | 向左移动 · Left |
| --- | --- | --- |
| ![待机 · Idle](previews/animations/idle.gif) | ![向右 · Right](previews/animations/running-right.gif) | ![向左 · Left](previews/animations/running-left.gif) |
| 打招呼 · Greeting | 捂鼻扇风 · Fanning | 抱头崩溃 · Error |
| ![打招呼 · Greeting](previews/animations/waving.gif) | ![捂鼻扇风 · Fanning](previews/animations/jumping.gif) | ![崩溃 · Error](previews/animations/failed.gif) |
| 等你回来 · Waiting | 正在工作 · Working | 看看结果 · Review |
| ![等待 · Waiting](previews/animations/waiting.gif) | ![工作 · Working](previews/animations/running.gif) | ![审阅 · Review](previews/animations/review.gif) |

以上为素材循环预览，不保证应用持续显示对应动作。实际尺寸和宿主播放规则见 [离线预览](previews/size-and-playback.html)，下载后用浏览器打开。

These looping artwork previews do not guarantee continuous app-state display. Download and open the [offline preview](previews/size-and-playback.html) in a browser to inspect sizes and tested host playback rules.

## 安装 · Install

下载本 Release 的 `yuexinmiao-codex-pet-v1.0.0.zip`，解压后运行：

Download this release's `yuexinmiao-codex-pet-v1.0.0.zip`, extract it, and run:

```sh
python3 scripts/install.py
```

Windows 可使用 `python`。安装仅需 Python 标准库；完成后在 Codex 宠物选择器中选择「月薪喵 Codex Pet」。不同旧版会询问替换并备份还是并存，重复安装不新增同版条目。

On Windows, use `python`. Installation requires only Python's standard library. Select 「月薪喵 Codex Pet」 in the Codex pet picker afterward. For a different existing version, choose replacement with backup or keeping both; reinstalling the same package does not duplicate it.

[完整安装指南 · Full installation guide](docs/INSTALL.md) · [代理安装技能 · Agent installation skill](skills/install-yuexinmiao/SKILL.md)

## 手机 Work · Mobile Work

通过 ChatGPT 官方宠物设置上传 `dist/yuexinmiao-selected/spritesheet.webp` 并选中，手机使用相同账号和工作区。本机安装不会自动同步账号。

Upload `dist/yuexinmiao-selected/spritesheet.webp` through ChatGPT's official pet settings and select it. Use the same account and workspace on mobile. Local installation does not synchronize the account pet automatically.

v1.0.0 手机处理中历史实测为挠头看电脑；不承诺九种动作全部触发。捂鼻扇风专用 Work 图集属于 v1.1.0，不包含在这个历史版本里。需要该动作，请使用 [v1.1.0](https://github.com/miroxsy-oss/yuexinmiao-codex-pet/releases/tag/v1.1.0)。

Historical v1.0.0 mobile processing tests showed head-scratching at the computer; not all nine states are guaranteed to trigger. The separate Work fanning atlas belongs to v1.1.0 and is not included in this historical edition. Use [v1.1.0](https://github.com/miroxsy-oss/yuexinmiao-codex-pet/releases/tag/v1.1.0) for that gesture.

## 本次同版修订 · Same-version refresh

仅更新双语文案、安装提示、配置描述与检查记录组织。v1.0.0 的原图集与源帧保持不变，待机与打招呼的历史浅色边缘仍保留；边缘修复属于 v1.1.0，不冒充本版已有修复。

This refresh updates bilingual documentation, installer messages, manifest descriptions, and validation-record organization. The original v1.0.0 atlas and source frames remain unchanged, including historical light edges in idle and greeting. Those repairs belong to v1.1.0 and are not claimed for this edition.

## 开发与验证 · Development and validation

使用 Python 3.10 或以上；重建与图像检查需要安装依赖：

Use Python 3.10 or later; rebuilding and image checks require these dependencies:

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
python scripts/check_docs.py
python -m unittest discover -s tests -q
```

图集为 v1、1536×1872、57 有效帧位。当前结果见 [QA 范围](qa/README.md)，完整结构见 [图集规格](docs/REFERENCE.md)。本次没有重新进行手机 UI 测试。

The v1 atlas is 1536×1872 with 57 active frame slots. See [QA scope](qa/README.md) for current results and the [atlas specification](docs/REFERENCE.md) for its structure. This refresh did not repeat mobile UI tests.

[更新记录 · Changelog](CHANGELOG.md) · [参与维护 · Contributing](CONTRIBUTING.md) · [安全与反馈 · Security](SECURITY.md) · [使用条款 · Terms](LICENSE.md) · [素材权利 · Artwork rights](docs/ATTRIBUTION.md)

自动化检查配置覆盖 Linux、macOS 和 Windows；具体通过状态以 GitHub Actions 结果为准。这些是包与安装器测试，不是三个系统上的应用 UI 实测。

The workflow targets Linux, macOS, and Windows; consult GitHub Actions for actual results. These are package and installer checks, not live application UI tests on all three systems.
