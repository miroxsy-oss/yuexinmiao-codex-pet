> 历史记录：以下为 v1.0.0 审计时的状态、尺寸与校验值，不是当前发布状态。当前变化见 [v1.1.0 发布说明](RELEASE-v1.1.0.md)，手机验证见 [Work 说明](MOBILE_WORK.md)。
>
> Historical record: the status, dimensions, and hashes below reflect the v1.0.0 audit, not the current release status. See the [v1.1.0 release notes](RELEASE-v1.1.0.md) and [mobile Work report](MOBILE_WORK.md) for subsequent changes.

# 官方公开要求审计 · Public official requirements audit

核验日期 / Checked: 2026-09-25。对象 / Package: 月薪喵 Codex Pet。
本次范围为技术兼容性；不评价再分发许可。No redistribution-permission assessment in this technical audit.

## 公开依据 · Public sources

1. [OpenAI — Pets](https://learn.chatgpt.com/docs/pets)，特别是 Upload a custom pet、Understand pet status、Create a custom pet。
2. [OpenAI — Commands / Pets](https://learn.chatgpt.com/docs/reference/commands#pets)，安装链接的 `spriteVersionNumber` 参数。

两篇均已实际打开核对。Both pages were opened and checked.

## 文档明确规定的格式 · Explicit format requirements

|依据 / Source|要求 / Requirement|当前文件 / Current file|结论 / Result|
|---|---|---|---|
|Pets|PNG 或 WebP / PNG or WebP|WebP|通过 / Pass|
|Pets|透明 / Transparent|RGBA，Alpha 0–255|通过 / Pass|
|Pets|1536×1872|1536×1872|通过 / Pass|
|Pets|≤20 MiB|498198 bytes，约 0.475 MiB|通过 / Pass|
|Commands|版本参数支持 1 或 2，默认 1 / Versions 1 and 2; default 1|spriteVersionNumber=1|支持 / Supported|

**结论：满足这两篇文档中可核验的适用格式要求。v1 是官方明确支持的版本，缺少 v2 视线帧不是 v1 不合格。**

**Result: the package meets the applicable, verifiable format requirements in these documents. Version 1 is explicitly supported; missing v2 look frames do not invalidate v1.**

## 额外工程核查 · Additional engineering checks

以下为本机程序、验证脚本和实际使用证据，不冒充公开文档逐条规定：

- 安装文件与发布文件逐字节一致，SHA256：`5a008b5e7bebfe222c36994ebbd1c724f3be98aa11bd35d72155cabaafb33431`。
- 本地 atlas 验证脚本复跑：0 错误、0 警告；独立包检查 44 项通过。
- 9 行、57 有效帧位、15 透明空格，符合已安装应用的 v1 行定义。
- 网页账号上传、激活与刷新保持已验证；手机处理动画已观察，未完成九状态实机全覆盖。

These are engineering findings, not additional published rules: installed and packaged files are byte-identical; the atlas validator reports zero errors/warnings; 44 package checks pass; nine rows, 57 active slots and 15 empty slots match the installed app. Web upload/selection persistence and mobile processing animation were observed. Full nine-state device testing is incomplete.

## 不能混用的标准 · Separate standards

本地创作流程不能替代官方公开的接收要求，也不能证明其中每项风格建议都是官方强制标准。

Local production workflows do not replace public acceptance requirements or establish official mandates for every style guideline.

本次查阅的官方文章未规定宠物必须全身、不能有电脑道具、每个动作必须写实，也未承诺悬停持续跳舞或动作必须持续到气泡消失。因此，已选扇风动作、半身造型和道具不能据此直接判为违反官方公开要求。它们与本地创作建议的差异仍可记录为设计取舍。

The reviewed articles do not mandate full-body art, prohibit computer props, prescribe literal motions, or promise continuous hover/task animation. These design choices therefore cannot be declared violations on the basis of those articles alone.

## 功能体验的独立结论 · Separate experience finding

当前桌面播放器三遍后回待机，不满足用户要求的持续状态一致性；这是另一个验收维度，详见 [状态审计](STATE_AUDIT.md)。不能据此说图集格式不合格，也不能因格式通过就说体验问题已解决。未修改应用本体或签名。

The desktop player's fallback to idle still fails the user's persistent-status requirement; see the [state audit](STATE_AUDIT.md). This does not invalidate the atlas format, and passing format checks does not fix that experience. No application or signature changes were made.

建议项目描述 / Suggested description:

> 兼容 OpenAI 官方文档所支持 v1 格式的非官方自定义宠物；已通过本地结构检查与部分实机测试。
>
> An unofficial custom pet compatible with the v1 format supported in OpenAI documentation, with local structural validation and partial device testing.

本审计不构成 OpenAI 官方认证。This audit is not OpenAI certification.
