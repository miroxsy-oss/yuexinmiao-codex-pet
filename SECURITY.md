# 安全与问题反馈 · Security and issue reporting

本项目提供静态宠物素材、Python 安装器与构建脚本。常规安装不需要密码、API Key 或管理员权限；不要把凭据粘贴到 Issue。

This project provides static pet assets, a Python installer, and build scripts. Normal installation needs no password, API key, or administrator privileges. Never paste credentials into an issue.

优先使用最新发布包；v1.0.0 保留用于历史兼容。若校验值不符、安装器出现意外写入或附件含异常可执行内容，请停止安装，并通过仓库 Issue 报告版本、文件名和可公开的复现信息。不要公开个人路径、凭据或可被滥用的敏感细节；需要保密处理时先询问维护者可用的私密渠道。

Prefer the latest release; v1.0.0 is retained for historical compatibility. Stop installation if checksums mismatch, the installer writes unexpectedly, or an archive contains unexpected executable content. Report the version, file name, and non-sensitive reproduction details through Issues. Do not disclose personal paths, credentials, or sensitive exploit details; first ask the maintainer for an available private channel when confidential handling is needed.

检查范围：安装前核验 pet.json 与图集；替换旧版前保留回滚备份；应用实际状态、网页上传和手机显示需各自验证。公开 CI 只证明所列自动检查，不代表所有系统与应用版本均已实测。

Validation scope: verify pet.json and the atlas before installation, retain a rollback backup when replacing an older version, and verify app state, web upload, and mobile display separately. Public CI establishes only its listed checks, not testing of every OS and application version.

## 防止误上传 · Prevent accidental uploads

.gitignore 排除常见凭据、私有配置、证书和日志，但不会自动删除已经提交的内容。提交前检查暂存区；不要把真实凭据写入示例文件。使用 GitHub noreply 邮箱，截图只保留宠物效果，隐藏账号、通知、对话与本机路径。

.gitignore excludes common credentials, private configuration, certificates, and logs, but does not remove files already committed. Inspect staged changes and never put real credentials in examples. Use a GitHub noreply email and crop screenshots to the pet, excluding accounts, notifications, conversations, and local paths.

CI 使用只读权限、固定 SHA 的 Actions 和经 SHA256 核验的密钥扫描器。扫描输出脱敏，不上传含疑似凭据的报告。依赖更新通过定期 Pull Request 复核，不自动合并。

CI uses read-only permissions, SHA-pinned actions, and a checksum-verified secret scanner. Scan output is redacted; reports containing suspected credentials are not uploaded. Periodic dependency update pull requests require review and are not automatically merged.

## 安装边界 · Installation boundaries

安装器不联网、不执行 shell、不读取凭据，也不要求管理员权限。写入范围为明确选择的 Codex 数据目录中的 pets 与 pet-backups；拒绝通过这两个目录的符号链接重定向写入。备份与取消、失败回滚均有测试。

The installer does not access the network, execute a shell, read credentials, or require administrator privileges. It writes to pets and pet-backups under the selected Codex data directory and rejects symlink redirection through those directories. Backup, cancellation, and rollback behavior are tested.

校验值能发现内容损坏，但若安装包与校验文件同时被替换，不能仅凭自带校验值证明来源可信。请从本仓库的发布页取得文件并核对发布校验值。

Checksums detect corruption, but a package and its accompanying checksum file can both be replaced. Bundled checksums alone do not authenticate the publisher. Obtain files from this repository's release page and compare the published checksums.

## 疑似泄露时 · Suspected exposure

不要在 Issue、截图或日志中贴出秘密值。只描述文件位置和脱敏特征；由凭据所有者确认撤销或轮换。清理历史、替换 Release 附件、撤销令牌或修改账号认证方式，需要单独确认，不能用删除当前文件代替轮换已泄露凭据。

Never paste secret values into issues, screenshots, or logs. Report only the location and redacted characteristics; the credential owner should confirm revocation or rotation. History cleanup, release-asset replacement, token revocation, and authentication changes require separate confirmation. Deleting a current file does not replace rotating an exposed credential.
