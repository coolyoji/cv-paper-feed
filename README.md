# Daily CV Paper Feed

这个仓库会每天自动生成一个计算机视觉论文阅读网页：

- `docs/index.html`：网页版本，适合直接打开或用 GitHub Pages 发布。
- `docs/literature.md`：Markdown 版本，适合复制到 Notion / Obsidian。
- `data/latest_papers.json`：脚本抓取与筛选后的结构化结果。

主题优先级：

1. 伪装目标检测 / 分割：COD, COS, VCOD, OVCOS, UCOD。
2. 无人机 / 航拍小目标检测、分割与跟踪。
3. 多光谱火灾探测：可见光-红外/热红外、高光谱、多传感器与卫星多波段火情感知。
4. 火灾监测大模型：foundation model、VLM/MLLM、SAM 及遥感基础模型驱动的火情识别、定位与时空监测。
5. 可迁移的泛 CV 方法：开放词汇分割、training-free、diffusion、异常检测、遥感、多模态、视频、边界/频域/深度等。

火灾专题栏目从 2026-07-14 起随每日日报推送，优先排序正式发表的顶会顶刊和领域高水平期刊论文；arXiv 预印本会保留，但不会标记成正式发表成果。期刊分区会在专题检索交付时按当期数据另行核验。

“当日精读队列”会排除所有历史日报中已经精读过的论文；即使候选不足也不会用旧论文回填。同一论文仍可保留在 COD、无人机、火灾等专题资料栏目中，便于按方向检索。

日报采用两级阅读密度：每日五篇精读保留完整九字段核读笔记；其他专题候选只展示核心机制、跟踪理由和链接。同一论文跨栏目出现时仅完整展示一次，后续位置使用交叉引用。

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
