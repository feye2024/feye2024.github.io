# 本地预览网页

## 日常使用

在网站文件夹中打开终端，运行：

```bash
bash run_server.sh
```

然后在浏览器打开 [http://127.0.0.1:4000](http://127.0.0.1:4000)。保持终端运行，修改并保存 `_pages/about.md` 后，预览页面会自动刷新。修改 `_config.yml` 后需要停止并重新启动预览。

结束预览时，在运行服务的终端按 `Ctrl+C`。

## 同时预览 AIRE Lab

另开一个终端，在同一网站文件夹中运行：

```bash
bash lab-site/run_server.sh
```

Lab 的独立本地地址是 [http://127.0.0.1:4001](http://127.0.0.1:4001)。两个服务同时运行时，个人主页导航栏最右边的 **AIRE Lab** 会在新标签页打开这个地址。Lab 内的 Home、People、Publications、Opening 都在同一页。

Lab 的人员和 Opening 在 `lab-site/index.md` 中修改；研究介绍在 `lab-site/_includes/home-intro.md`，论文列表在 `lab-site/_includes/publications.md`。保存后自动刷新。样式在 `lab-site/assets/css/main.css`。

## 发布到 GitHub

正式地址：

- 个人主页：[https://feye2024.github.io/](https://feye2024.github.io/)
- AIRE Lab：[https://feye2024.github.io/aire-lab/](https://feye2024.github.io/aire-lab/)

确认本地效果后，把需要发布的修改 commit 并 push 到 `main`。第一次发布需一并提交 `.github/workflows/deploy-pages.yml`、`scripts/check_site_build.py`、`lab-site/` 和本次配置修改。

GitHub 的 **Settings → Pages → Source** 使用 **GitHub Actions**。工作流 **Deploy personal homepage and AIRE Lab** 会先构建个人主页，再把 Lab 构建到 `aire-lab/`，检查页面及资源路径后一起发布。可在仓库的 Actions 页面查看结果；只有发布成功后，线上内容才会更新。

生产构建只读取各自的 `_config.yml`。本地启动脚本额外读取 `docs/local-preview.yml` 和 `lab-site/_config.local.yml`，因此本地仍使用 `4000`、`4001`，正式链接不会包含这些端口。修改配置文件后需要重启对应预览服务。
