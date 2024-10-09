# oapi-sdk-python-compact

![PyPI - Version](https://img.shields.io/pypi/v/lark-oapi-compact)
[![image](https://img.shields.io/pypi/pyversions/lark-oapi-compact.svg)](https://pypi.python.org/pypi/lark-oapi-compact)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![codecov](https://codecov.io/gh/StrayDragon/oapi-sdk-python-compact/graph/badge.svg?token=CF4OP0X9YL)](https://codecov.io/gh/StrayDragon/oapi-sdk-python-compact)


- 上游 https://github.com/larksuite/oapi-sdk-python 的默认分支 [v2_main](https://github.com/larksuite/oapi-sdk-python/tree/v2_main) 提供的API不全, 但是老分支 [main](https://github.com/larksuite/oapi-sdk-python/tree/main) 有一部分可以利用, 这个包将老分支的代码进行合并并兼容处理
- 增加一些方便使用的快捷函数, 见 [src/lark_oapi_compact/shortcut](./src/lark_oapi_compact/shortcut/README.md)
- 归档并弃用 https://github.com/StrayDragon/oapi-sdk-python


## Contributing

### 开发

0. 安装 ![`uv`](https://github.com/astral-sh/uv)
1. clone 项目后安装依赖 `uv sync --all-extras --dev`
2. 激活环境 `uv venv`
3. 运行 `pre-commit install`
4. 进行开发 :)

### 测试

0. 复制一份项目根下的 `.env.example` 文件, 保存为 `.env`, 修改相关的变量
1. 执行 `source .env` 加载测试用的环境变量
2. 参考 [.github/workflows/tests.yml](./.github/workflows/tests.yml), 调用相关命令测试
