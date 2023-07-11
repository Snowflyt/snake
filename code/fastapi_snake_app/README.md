# FastAPI Snake App

基于 Python FastAPI 框架的贪吃蛇 Demo 后端。需配合客户端使用。

FastAPI 的文档可参考 [FastAPI 中文文档](https://fastapi.tiangolo.com/zh/)。

主要代码在 `fastapi_snake_app/game.py` 中，其余代码为 FastAPI 框架的配置。

## 软件架构

- 语言: Python
- 主要使用框架: FastAPI
- 包管理器: Poetry
- 其他: Pylint

## 安装

建议使用依赖管理工具 Poetry 安装依赖，这也是开发所使用的工具。

确保你的电脑上已经安装了 Python >= 3.10 及 pip，然后运行以下命令安装 Poetry.

```bash
pip install poetry
```

然后进入本项目的根目录，运行以下命令即可。

```bash
poetry install
```

## 启动

运行以下命令启动项目：

```bash
poetry run start
```

> **Tips:**
>
> 如果这一步出错，尝试在设置中找到“区域与语言-管理语言设置-更改系统区域设置”，勾选“Beta 版: 使用 Unicode UTF-8 提供全球语言支持(U)”，然后重新启动电脑再尝试。
