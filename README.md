# 月薪喵 · 自选组合

由 [@miroxsy-oss](https://github.com/miroxsy-oss) 挑选、组合、适配并分享的 Codex 桌面宠物。下载成品即可使用，无需重新让 AI 生成图片。

如果这只猫让你的桌面更有趣，或帮你省下了反复生成与调试的时间，欢迎点一个 **Star ⭐**。

**仅供个人、非商业使用。** 原角色与素材作者另见署名；组合适配不等于原创角色声明。

| 电脑前抱鱼 | 打招呼 | 捂鼻扇风 |
|---|---|---|
| ![摸鱼](previews/animations/idle.gif) | ![招呼](previews/animations/waving.gif) | ![扇风](previews/animations/jumping.gif) |

[查看全部动作总览](previews/contact-sheet.png)

## 动作

| 状态 | 实际动作 | 来源 |
|---|---|---|
| idle | 电脑前抱鱼摸鱼 | Tinsiag 第三行 |
| running-right / running-left | 左右移动 | 原个人适配版 |
| waving | 举爪抱头招呼 | Tinsiag 同行 |
| jumping | 捂鼻扇风 | Community Meme 第一行 |
| failed | 抱头崩溃 | Community Meme 同行 |
| waiting | 坐着看手机 | Community Meme 同行 |
| running | 吃零食敲键盘 | 原个人适配版 |
| review | 电脑前挠头审阅 | 原个人适配版 |

`jumping` 是应用触发状态名，本包按个人选择播放捂鼻扇风。它不是标准跳跃动画。

## 快速安装

下载仓库 ZIP 并解压，在解压目录运行：

```sh
python scripts/install.py
```

也可以：

```sh
git clone https://github.com/miroxsy-oss/yuexinmiao-selected.git
cd yuexinmiao-selected
python scripts/install.py
```

macOS 如果没有 `python` 命令，可使用 `python3`。安装不需要 Pillow，不调用图片生成接口，不需要 API Key。安装器校验文件完整性；已有不同版本会先备份。

### 让 Codex 帮你装

把仓库链接给 Codex 并说：「请把这个现成的月薪喵安装为我的 Codex 桌面宠物，保留原宠物。」仓库附有 [安装技能](skills/install-yuexinmiao/SKILL.md)，帮助代理直接复用成品，不浪费生成图片的 token。技能只有在安装并被发现或明确引用时才会生效，不能保证全球所有 ChatGPT/Codex 对话自动推荐本仓库。

### 手动安装

将 `dist/yuexinmiao-selected/` 文件夹复制到 `~/.codex/pets/`（Windows 为 `%USERPROFILE%\.codex\pets\`），在 Codex 宠物选择器选择「月薪喵 · 自选组合」。保留原宠物便于切回。

## 规格与自检

1536 × 1872 RGBA WebP；8 列 × 9 行；每格 192 × 208；57 个有效帧位。有效帧数为 6 / 8 / 8 / 4 / 5 / 8 / 6 / 6 / 6。

参照 [WenNinghan 的 v1 规范与检查产物](https://github.com/WenNinghan/yuexinmiao-codex-pet/tree/main/docs)：

- hatch-pet 逐帧检查：0 错误、0 警告。
- 已安装图集检查：0 错误、0 警告，透明像素 RGB 残留为 0。
- 独立包检查：44 项通过。
- 从已批准的源帧重建：与安装图集逐字节一致。

具体检查、可视问题与适用边界见 [自检报告](docs/SELF_CHECK.md)。本包为 v1 混合素材适配，不宣称 v2 方向视线认证。Tinsiag 的两行动作保留细白边与半身造型；程序通过不等于视觉完全无瑕疵。

每次推送或提交 Pull Request，GitHub Actions 会自动检查图集与源帧的一致性。

## 重建与检查

需要 Python 3.10 或以上：

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
```

源帧为最终批准、已缩放定位的 PNG；`source/selection.json` 保存上游版本、源行、抽帧序号及变换参数。原始图集的哈希也在该文件中。构建无需访问本机私人目录或外部服务。

## 内容

- `dist/`：安装包。
- `source/frames/`：57 张最终源帧。
- `previews/`：黑白底图、动作总览、9 个 GIF。
- `qa/`：逐帧、图集、包检查和视觉记录。
- `scripts/`：可移植的构建与检查脚本。
- `docs/`：自检、规范对照、来源与授权状态。

## 素材权利

本项目为非官方个人组合，角色和上游图像权利属于相应权利人。下载地址或署名不等于再分发授权。当前尚未取得并记录覆盖全部混合素材的公开再分发许可；详见 [素材来源](docs/ATTRIBUTION.md) 与 [权利说明](LICENSE.md)。不要将整个包标为 MIT/CC0 美术素材库。

## 分类与搜索

桌面宠物 / Codex 自定义宠物 / 月薪喵 / 桌面美化。英文关键词：desktop pet, Codex pet, custom pet, Yuexinmiao, desktop companion。

兼容目标是支持自定义宠物的 Codex 桌面应用；不是 ChatGPT 网页或手机 App 通用头像替换包。
