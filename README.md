# 会飞的豆奶包

会飞，也会自己倒豆奶的 Python 小项目。用于「小白 AI 进阶之路」第 008 期的 clone、pull、Fork 与 Pull Request 教学。

## 准备与运行

需要 Python 3.10 或以上版本，无需第三方依赖。

从本页右上方的绿色 **Code** 按钮复制 HTTPS 地址，或直接运行：

```bash
git clone https://github.com/zy1506141070/flying-dounaibao.git
cd flying-dounaibao
```

```bash
python3 dounaibao.py
python3 -m unittest -v
```

## 文件

| 文件 | 用途 |
| --- | --- |
| `dounaibao.py` | 飞行与倒豆奶的实现 |
| `test_dounaibao.py` | 飞行、输入校验与液体守恒检查 |
| `CHANGELOG.md` | 版本更新说明 |
| `CONTRIBUTING.md` | 贡献代码的步骤 |
| `LICENSE` | MIT 开源许可证 |

## 已知问题

v1.0.0 中豆奶包一只手握杯、杯身倾角过大，倒出 200 ml 时会洒出 50 ml。可在 Issues 中报告现象，并通过新分支和 Pull Request 提出修复。

## 版本与贡献

发布版本见本仓库 **Releases**。想参与改进，先阅读 [贡献说明](CONTRIBUTING.md)。

## 开源许可

示例代码采用 [MIT License](LICENSE)。本仓库不包含视频人物图、个人声音或第三方品牌素材。
