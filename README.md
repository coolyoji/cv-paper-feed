# Daily CV Paper Feed

这个仓库会每天自动生成一个计算机视觉论文阅读网页：

- `docs/index.html`：网页版本，适合直接打开或用 GitHub Pages 发布。
- `docs/literature.md`：Markdown 版本，适合复制到 Notion / Obsidian。
- `data/latest_papers.json`：脚本抓取与筛选后的结构化结果。

主题优先级：

1. 伪装目标检测 / 分割：COD, COS, VCOD, OVCOS, UCOD。
2. 可迁移的泛 CV 方法：VLM/MLLM、SAM、开放词汇分割、training-free、diffusion、异常检测、遥感、多模态、视频、边界/频域/深度等。

## 本地更新

```powershell
python scripts/update_papers.py
```

然后打开：

```text
docs/index.html
```

## GitHub 自动更新

`.github/workflows/update-literature.yml` 会每天运行一次，更新 `docs/literature.md`、`docs/index.html` 和 `data/latest_papers.json`。

如果启用 GitHub Pages，建议发布目录选择：

```text
Branch: main
Folder: /docs
```

