"""
cli_languages.py
Language files for LaTeX-batch-builder command line interface

Copyright 2022 ayhe123

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

list_of_languages = ['en', 'cns']
languages = [
    {  # en
        "pwd": ".tex files in current directory(commands in brackets will be executed when compiling this file):",
        "empty_dir": "No .tex files in current directory",
        "choices": "Please choose:\n0: Compile all files\n1: Remove temporary files\n2: Compile and remove temporary files\n3: Change directory\n4: Exit",
        "prompt": "Input a number between 0 and 4 > ",
        "chdir_1": "Current directory:",
        "chdir_2": "Enter directory > ",
        "chdir_3": "No such directory!",
        "cleaning_1": "These files are about to remove:",
        "cleaning_2": "Continue?[y/n] > ",
        "cleaning_3": "No files to be removed"
    },
    {  # cns
        "pwd": "当前目录下的 .tex 文件有(括号里的命令将在编译这个文件时执行):",
        "empty_dir": "当前目录下没有 .tex 文件",
        "choices": "请选择:\n0: 编译所有文件\n1: 清理临时文件\n2: 编译且清理临时文件\n3: 切换目录\n4: 退出",
        "prompt": "输入 0-4 间的数字 > ",
        "chdir_1": "当前目录:",
        "chdir_2": "输入要前往的目录 > ",
        "chdir_3": "没有这个目录!",
        "cleaning_1": "这些文件将被删除:",
        "cleaning_2": "是否继续?[y/n] > ",
        "cleaning_3": "没有要删除的文件"
    }
]
