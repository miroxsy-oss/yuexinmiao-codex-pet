# 检查记录范围 · Validation record scope

当前包：package-check.json 为本次桌面结构检查；有 Work 专用版时，work-package-check.json 为其检查。current-validation.json 记录本次图集哈希和重建结果。以下检查可重跑，不代表当前手机或桌面 UI 已再次实测。

Current package: package-check.json contains the desktop structural checks; work-package-check.json checks the optional Work edition when present. current-validation.json records this pass's atlas hashes and rebuild results. These checks are reproducible and do not claim a fresh phone or desktop UI test.

history/pre-doc-refresh/ 保存文档修订前的历史证据。旧图集校验值、部署状态和截图结论只适用于各自的采样时点，不能当作当前版本的测试结果。文件内的历史数字予以保留，不补写不存在的实测。

history/pre-doc-refresh/ stores evidence collected before the documentation refresh. Old hashes, deployment states, and screenshot conclusions apply to their original observation points, not the current package. Historical measurements are retained; no unperformed device tests are added.

手机不是未测试：此前 iPhone 镜像已经验证对应版本的处理动画。本次逐字节确认图集不变，沿用既有实测结论；未重新测试不等于既有测试失败，未覆盖分支仍不作保证。

Mobile was tested previously: iPhone Mirroring verified the processing animation of the corresponding edition. This refresh confirms the atlas is byte-identical and retains that evidence. Not repeating a test does not invalidate its prior result; untested branches remain unverified.
