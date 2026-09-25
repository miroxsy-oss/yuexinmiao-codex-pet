# 安全与问题反馈 · Security and issue reporting

本项目提供静态宠物素材、Python 安装器与构建脚本。常规安装不需要密码、API Key 或管理员权限；不要把凭据粘贴到 Issue。

This project provides static pet assets, a Python installer, and build scripts. Normal installation needs no password, API key, or administrator privileges. Never paste credentials into an issue.

优先使用最新发布包；v1.0.0 保留用于历史兼容。若校验值不符、安装器出现意外写入或附件含异常可执行内容，请停止安装，并通过仓库 Issue 报告版本、文件名和可公开的复现信息。不要公开个人路径、凭据或可被滥用的敏感细节；需要保密处理时先询问维护者可用的私密渠道。

Prefer the latest release; v1.0.0 is retained for historical compatibility. Stop installation if checksums mismatch, the installer writes unexpectedly, or an archive contains unexpected executable content. Report the version, file name, and non-sensitive reproduction details through Issues. Do not disclose personal paths, credentials, or sensitive exploit details; first ask the maintainer for an available private channel when confidential handling is needed.

检查范围：安装前核验 pet.json 与图集；替换旧版前保留回滚备份；应用实际状态、网页上传和手机显示需各自验证。公开 CI 只证明所列自动检查，不代表所有系统与应用版本均已实测。

Validation scope: verify pet.json and the atlas before installation, retain a rollback backup when replacing an older version, and verify app state, web upload, and mobile display separately. Public CI establishes only its listed checks, not testing of every OS and application version.
