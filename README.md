# issue as a service

[![issue as a Service](https://img.shields.io/badge/iaas-issue%20as%20a%20service-brightgreen)](https://github.com/maguowei/iaas)
[![github workflow](https://github.com/maguowei/iaas/workflows/issue%20as%20a%20service/badge.svg)](https://github.com/maguowei/iaas/actions)

**注意: 本项目只是用于学习和演示, 切勿滥用。以免违反 `GitHub Actions` 的使用条款（资源滥用）。**

利用 `GitHub Actions` 执行 `issue` `comment` 中包含的 `bash script` 代码快

Example: [iaas/issues/16](https://github.com/maguowei/iaas/issues/16)

## 使用

使用 [`Use this template`](https://github.com/maguowei/iaas/generate) 按钮创建项目

1. 创建的`issue` 需要打上 `iaas` 标签, 如果`issue` 创建时标题以 `iaas` 作为开头，则会自动打上该标签。
2. 代码块需要以`Markdown`中的代码块格式标记，且为合法的 `bash script`
3. 默认只有代码块的创建者为仓库主人时代码块才会自动触发 `Action` 运行代码
4. 默认会将当前目录下所有文件打包上传到 `artifact`, 注意文件大小限制 [actions/upload-artifact issues/9](https://github.com/actions/upload-artifact/issues/9); 且需要注意 `artifacts` 不是永久保留 [About workflow artifacts](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/persisting-workflow-data-using-artifacts#about-workflow-artifacts)

## TODO

- [ ] Python script support
- [ ] [upload-release-asset](https://github.com/actions/upload-release-asset) support 文件的永久保存（提供选项）
