> 历史记录：以下为 v1.0.0 审计时的状态、尺寸与校验值，不是当前发布状态。当前变化见 [v1.1.0 发布说明](RELEASE-v1.1.0.md)，手机验证见 [Work 说明](MOBILE_WORK.md)。
>
> Historical record: the status, dimensions, and hashes below reflect the v1.0.0 audit, not the current release status. See the [v1.1.0 release notes](RELEASE-v1.1.0.md) and [mobile Work report](MOBILE_WORK.md) for subsequent changes.

# 最终兼容性与发布判断 · Final compatibility and release assessment

## 本轮优化 · This pass

新增离线实际尺寸预览（32、48、80、128、192 px），支持深浅背景；默认复现已核验的官方桌面播放规则，可切换纯动作展示。README 明确 GIF 为动作展示，避免把循环预览等同于实际状态持续显示。未修改应用、签名或已选动作。

Added an offline size preview with five sizes, light/dark backgrounds, and the verified desktop playback behavior as its default. A separate showcase mode demonstrates looping artwork. README clarifies that GIF loops do not promise persistent status display. No app, signature, or approved animation was modified.

重新测试五组无损 WebP 编码，均逐像素相等；现有 498198 字节最小，保留原图集。透明边缘细白线、半身底边和各动作的风格差异未进行不可逆的猜测修补。没有宣称清晰度或动作本身得到提升。

Five lossless WebP encoding variants were pixel-identical; the existing 498198-byte atlas was the smallest and was retained. Thin light outlines, half-body boundaries, and source style differences were not altered through speculative cleanup. No improved artwork sharpness or motion is claimed.

## 官方依据澄清 · Official-source clarification

以 [官方公开要求审计](OFFICIAL_AUDIT.md) 为技术兼容性结论。下表 v2 与动作语义为本地制作流程的对照，不是官方公开的 v1 上传门槛；没有 v2 视线帧不能判为 v1 不合格。

Use the [public-requirements audit](OFFICIAL_AUDIT.md) for compatibility. The v2/style comparisons below concern local production guidance, not public v1 upload requirements.

## 分项结论 · Decisions

|项目 / Item|结论 / Verdict|
|---|---|
|官方当前接受的 v1 图集格式 / Accepted v1 format|兼容；结构检查通过 / Compatible; structural checks pass|
|本地技能 v2 创作流程 / Local v2 workflow|不符合；无额外 16 向视线帧 / Not met; no 16-direction look rows|
|严格动作语义 / Strict animation semantics|不完全符合；jumping 为用户选定扇风，idle 带道具，waving 为半身 / Partial; intentional fanning jump, props in idle, half-body greeting|
|持续任务状态表达 / Persistent task-state display|不通过用户要求；受播放器行为限制 / Does not meet the user requirement; app-player limitation|
|手机 / Mobile|运行时动画观察通过；非九状态全覆盖 / Processing animation observed; not all nine states verified|
|GitHub 技术打包 / Technical repository readiness|具备安装包、源码、预览与文档；CI 尚未在 GitHub 运行 / Package, source, previews and docs prepared; GitHub CI not run|
|完整素材公开再分发 / Public redistribution of all artwork|授权未确认完整；不能认定可直接公开分发 / Permissions not fully established; cannot clear the full asset release|

这是“兼容官方已支持 v1 格式的非官方自定义宠物”，不是“官方认证”或“完全符合最新 v2 创作标准”。能上传并显示不代表官方认证，也不代表获得图片再分发授权。

This is an unofficial custom pet compatible with the supported v1 format, not an officially certified pet or full compliance with the latest v2 creation workflow. Successful upload and display do not confer certification or redistribution rights.

完整素材包建议待许可确认后再公开。若仅分享你有权发布的安装工具与工作流，可准备不含第三方图像、源帧和预览的独立仓库；这将不再是开箱即用的完整宠物包。本次没有创建或上传 GitHub 仓库。

Defer public release of the complete artwork package until permissions are established. A separate repository containing only tools and workflow material you have the right to publish is an alternative, excluding third-party artwork, source frames, and previews; it would not be a ready-to-use full pet package. No GitHub repository was created or uploaded.

参考 / References: [Official Pets](https://learn.chatgpt.com/docs/pets), [GitHub licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). v2 创作检查依据本机 hatch-pet 技能；它的创作规则不等于旧版 v1 文件不受应用支持。

The v2 creation checks refer to the local hatch-pet skill. Its production rules do not imply that the application rejects older v1 files.
