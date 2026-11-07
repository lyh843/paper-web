# 素材与真实数据演示

## 原论文图像

`localpfn-fig1-circles.png`、`localpfn-fig3-architecture.png` 和 `localpfn-fig2-scaling.png` 是新版正文使用的原图裁剪，分别来自官方 PDF 第2、5、4页。裁剪信息和指纹见上层 `provenance.json`。

其他旧裁图保留用于审计与旧版阅读，不代表新版 HTML 全部嵌入了它们。旧版自包含网页及其引用的5张旧图已一并归档。

## Iris 数据与出处

引用：Fisher, R. (1936). *Iris* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C56C76>。

- 数据集说明：<https://archive.ics.uci.edu/dataset/53/iris>。
- 原始文件：<https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data>，2026-10-18 获取。
- UCI 标注许可：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。`iris.data` 保留下载字节；计算和演示划分属于本解读新增。
- SHA-256：`6f608b71a7317216319b4d27b4d9bc84e6abd734eda7872b71a458569e2656c0`。
- 版本提示：使用 UCI 的历史 `iris.data` 文件，不是更正后的 `bezdekIris.data`。UCI 页面注明第35/38条记录与 Fisher 原始数据有差异；此处不静默修正，确保行号与统计量能按所引用文件重算，也不声称它与 TabZilla 的 Iris 副本逐行相同。

## 重算范围

运行：

```bash
python assets/compute-iris-example.py
```

脚本仅用 Python 标准库，从本地 `iris.data` 读取，输出 `iris-example.json`。每类前40/接5/末5条作为训练/验证/测试；仅在训练集拟合标准化，计算第150条测试行的四个精确近邻，以及训练锚点139附近的共享上下文切分。每一步均可离线重算。

这不是论文的 TabZilla fold，也不是 LoCalPFN 精度实验。没有加载模型、运行前向、计算内部激活或进行微调。JSON 中的距离是实际计算值，网络输出概率未计算，正文中的 softmax (0,1,2) 分数例子仅为数学教学。
