# LaTeX-batch-builder

****

**我需要有人来帮我在 Windows 上打包和测试这个程序。更多细节见 [这个 issue](https://github.com/ayhe123/LaTeX-batch-builder/issues/1)**

****

[English documentation](README.md)

自动编译多个 LaTeX 文件、删除编译产生的临时文件的工具

可以一次编译同一目录下所有的 `.tex` 文件，根据文档内容执行不同的编译命令，支持自定义编译命令和要删除的临时文件

## 使用方法

### 环境要求

需要安装主流的 LaTeX 发行版（比如 TeX Live、MacTeX）。确保能在终端使用 `xelatex`：

```bash
xelatex --version
```

### 打包好的程序

在[这里](https://github.com/ayhe123/LaTeX-batch-builder/releases)下载打包好的程序（打包用的是 `pyinstaller`），不需要安装 Python

如果当前目录(Windows 是程序所在的目录, MacOS 双击程序的话是 `~`)下没有 `settngs.json` 文件，程序会使用默认设置，可以在这时导出默认设置的 `settngs.json`

### 运行源程序

只需要有 Python 3（测试环境：Python 3.8），不需要安装其他的 Python 包

克隆这个仓库，在仓库的目录下运行 `LaTeX_batch_builder_cli.py` 即可

### 更改语言

默认的语言是英文

在 `settings.json` 找到下面一行：

```json
"language": "en",
```

修改 `"language"` 的值就可以更改程序运行时的语言

现在支持的语言有英文（值改成 `"en"`）和简体中文（值改成 `"cns"`）

### 多进程

采用多个进程进行编译。默认的进程数是5

在 `settings.json` 找到下面一行：

```json
"num_of_processes": 5,
```

修改 `"num_of_processes"` 的值就可以更改进程数

### 自定义编译命令

在 `settings.json` 中修改 `"compile_commands"`，`"compile_cases"` 和 `"default_command"` 的值就可以自定义编译命令。格式为：

```json
"compile_commands": {
        "命令1名称": [
            "xelatex -interaction=batchmode $FILE"  // 在执行这行命令时，$FILE 会被替换为不带扩展名的文件名，$FILE 会被替换为带扩展名的文件名
        ],
        "命令2名称": [
            "xelatex -interaction=batchmode $FILE",
            "xelatex -interaction=batchmode $FILE"
        ],
        ...
    },
"compile_cases": [
    {
        "match": "匹配条件1的正则表达式",
        "exec": [
            "命令1名称",
            "命令2名称",
            ...
        ]
    },
    {
        "match": "匹配条件2的正则表达式",
        "exec": [
            "命令3名称",
            "命令4名称",
            ...
        ]
    },
    ...
],
"default_command": [
    "命令5名称",
    "命令6名称",
    ...
]
```

程序执行时会从上到下读取 `"compile_cases"` 中每个 object，在 `.tex` 文件中搜索能匹配 `"match"` 的值的字符串，如果有这样的字符串则退出匹配，之后会执行对应的 `"exec"` 中的命令

如果 `"compile_cases"` 中所有的 object 都没有匹配，则执行 `"default_command"` 中的命令

### 自定义要编译或要删除的文件

在 `settings.json` 中找到 `"compile_format"`，把你想要编译的文件的扩展名加到 `"compile_format"` 的值里面，程序就可以读取编译这类文件

在 `settings.json` 中找到 `"remove_format"`，把能匹配到你想要删除的文件的正则表达式加到 `"remove_format"` 的值里面，清理临时文件时就会删除这个文件

## 示例

只要把 `settings.json` 设置好，这个程序可以实现很多功能

比如要使用 [Pandoc](https://pandoc.org/) 把当前目录下所有的 markdown、txt、html 文件转换为 pdf、docx、html 文件，可以把 `settings.json` 设置成下面这样：

```json
"compile_format": [
    "md",
    "txt",
    "html"
],
"compile_commands": {
    "docx": [
        "pandoc -f markdown -o '$FILE'.docx '$FILE_FULL'"
    ],
    "pdf": [
        "pandoc -f markdown -o '$FILE'.pdf '$FILE_FULL'"
    ],
    "html": [
        "pandoc -f markdown -o '$FILE'.html '$FILE_FULL'"
    ]
},
"compile_cases": [
    {
        "match": "#### to .docx ####",
        "exec": [
            "docx"
        ]
    },
    {
        "match": "#### to .pdf ####",
        "exec": [
            "pdf"
        ]
    },
    {
        "match": "#### to .html ####",
        "exec": [
            "html"
        ]
    }
],
"default_command": [
    "html"
],
"remove_format": []
```

要把某个文件转换为特定的格式，只需要在文件中加一行注释，内容为 `#### to .（要转换的格式的扩展名） ####`

## 许可证

本程序使用 Apache V2.0 许可证。详情见 http://www.apache.org/licenses/LICENSE-2.0

