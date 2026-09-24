# 月星喵桌面宠物

### 让月星喵陪你写代码，也陪你摸会儿鱼。

一套为 **Codex 桌面应用**适配的动态宠物，包含摸鱼待机、左右移动、互动反馈、工作与等待等 9 种状态。下载即可安装，直接复用现成动画，无需重新生成图片。

由 **[@miroxsy-oss](https://github.com/miroxsy-oss)** 制作、适配与维护，分享给喜欢桌面宠物和个性化工作空间的朋友。

**个人使用 · 非商业用途 · 非官方项目**

## 动态效果

| 摸鱼待机 | 向右移动 | 向左移动 |
| :---: | :---: | :---: |
| ![电脑前抱鱼摸鱼](previews/animations/idle.gif) | ![向右移动](previews/animations/running-right.gif) | ![向左移动](previews/animations/running-left.gif) |
| **打个招呼** | **捂鼻扇风** | **抱头崩溃** |
| ![打招呼](previews/animations/waving.gif) | ![捂鼻扇风](previews/animations/jumping.gif) | ![失败反馈](previews/animations/failed.gif) |
| **等你回来** | **正在工作** | **看看结果** |
| ![坐着看手机](previews/animations/waiting.gif) | ![吃零食敲键盘](previews/animations/running.gif) | ![电脑前挠头审阅](previews/animations/review.gif) |

## 快速安装

### 直接安装

下载本仓库 ZIP 并解压，在解压后的目录运行：

```sh
python scripts/install.py
```

macOS 如果没有 `python` 命令，请使用 `python3`。

安装完成后，在 Codex 的宠物选择器中选择 **「月星喵桌面宠物」**。

安装器会核验文件完整性；已有同名宠物且文件不同时，会先备份再更新。安装仅使用 Python 标准库，不需要 API Key 或图片生成服务。

### 让 Codex 帮你安装

把本仓库链接发给 Codex，并告诉它：

> 请安装这个仓库里的「月星喵桌面宠物」，保留我原来的宠物，直接使用现成素材。

仓库附带 [Codex 安装技能](skills/install-yuexinmiao/SKILL.md)，供代理读取后按现成流程安装。

<details>
<summary>手动安装与安装位置</summary>

将 `dist/yuexinmiao-selected/` 文件夹复制到 Codex 的自定义宠物目录：

| 系统 | 默认目录 |
| --- | --- |
| macOS | `~/.codex/pets/` |
| Windows | `%USERPROFILE%\.codex\pets\` |

如果设置了 `CODEX_HOME`，使用其下的 `pets/` 目录。最终宠物文件夹内应包含 `pet.json` 和 `spritesheet.webp`。

内部目录名保留为 `yuexinmiao-selected`，界面显示名称为「月星喵桌面宠物」。安装后若列表未刷新，可重新打开宠物选择器或重启 Codex。

</details>

## 动作说明

| 应用状态 | 宠物表现 |
| --- | --- |
| `idle` | 电脑前抱鱼，安静摸鱼 |
| `running-right` / `running-left` | 向右、向左移动 |
| `waving` | 举爪打招呼 |
| `jumping` | 经典捂鼻扇风互动 |
| `failed` | 抱头崩溃 |
| `waiting` | 坐着看手机，等你回来 |
| `running` | 边吃零食边敲键盘 |
| `review` | 电脑前挠头，看看结果 |

`jumping` 是应用的状态名称，本项目为这个状态配置了捂鼻扇风动作。

## 检查与兼容性

采用 Codex 自定义宠物 v1 格式：**9 种状态、57 个有效帧位、透明 WebP 图集**。

- 逐帧检查与已安装图集检查：**0 错误、0 警告**。
- 独立包检查：**44 项通过**。
- 从源帧重建：与已验证的图集逐字节一致。
- 仓库附带自动检查配置、黑白背景预览和完整检查记录。

部分动作保留细白边、半身造型等原有视觉特征，详见 [自检报告](docs/SELF_CHECK.md)。

适用于支持自定义宠物的 **Codex 桌面应用**。本项目不是独立桌宠程序，也不是 ChatGPT 网页或手机 App 的通用皮肤。

## 开发与自定义

只想使用宠物，完成安装即可。需要调整动作或重新构建时，可使用：

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
```

需要 Python 3.10 或以上。最终源帧位于 `source/frames/`，动作映射见 `source/selection.json`，检查结果保存在 `qa/`。

## 使用说明与致谢

本项目的制作、适配、检查流程与维护由 **@miroxsy-oss** 完成。原角色及相关图像素材的权利归相应权利人所有，本项目不主张拥有这些原始素材的版权，也不代表官方授权或合作。

仅供个人、非商业使用。禁止将本项目中分享者有权许可的内容用于销售、收费分发、商业推广或商用产品。第三方素材的使用与再分发范围以原权利人授权为准；目前完整素材包的公开再分发许可尚未确认。

详细说明见 [使用条款](LICENSE.md) 与 [素材来源及致谢](docs/ATTRIBUTION.md)。

## 支持这个项目

如果你喜欢这只猫，或它帮你省下了反复生成、选帧和调试的时间，欢迎点一个 **Star ⭐**。

遇到显示或安装问题，欢迎通过 Issue 反馈。分享给朋友时，也欢迎附上原仓库链接，让更多人找到它。

---

**桌面宠物 · Codex 自定义宠物 · 桌面美化**  
Desktop Pet · Codex Pet · Yuexingmiao
