# LaTeX-batch-builder

****

IMPORTANT: I need someone to help me with packaging and testing on Windows. See [this issue](https://github.com/ayhe123/LaTeX-batch-builder/issues/1) for details.

****

[中文文档](README_cns.md)

A tool which compiles several LaTeX files simultaneously and deletes temporary files.

This program compiles all LaTeX files in the working directory by executing different commands according to the content of the file. You can customize the commands the program executes.

## Usage

### Requirement

One of the mainstream LaTeX distributions (TeX Live, MacTeX, etc.) is required. Make sure that `xelatex` is available at terminal:

```bash
xelatex --version
```

### Packed executables

Packed executables (packed using `pyinstaller`) can be downloaded [here](https://github.com/ayhe123/LaTeX-batch-builder/releases). You can use it without Python.

If you are using MacOS, you should enter the directory of the program in the terminal and run it instead of double-click the program, otherwise an exception with message `settings.json not found!` will be raised.

Don't remove `settngs.json` in the program's directory.

### Run Source Code

All you need is Python 3 (This program is tested under Python 3.8). No additional Python package is needed.

Clone this repository and you can use it directly by running `LaTeX_batch_builder_cli.py`.

### Change Language

Default language is English.

To change the language of the program, find the following line in `settings.json` and modify its value:

```json
"language": "en",
```

English (by setting value as `"en"`) and simplified Chinese (by setting value as `"cns"`) is supported so far.

### Multiprocessing

This program uses multiprocessing to build LaTeX files. Default number of processes is 5.

To change the number of processes, find the following line in `settings.json` and modify its value:

```json
"num_of_processes": 5,
```

### Customize Compile Commands

Modify values of `"compile_commands"`, `"compile_cases"` and `"default_command"` in `settings.json` with following format to customize compile commands:

```json
"compile_commands": {
        "name of command1": [
            "xelatex -interaction=batchmode $FILE"  // $FILE will be replaced by .tex file name
        ],
        "name of command2": [
            "xelatex -interaction=batchmode $FILE",
            "xelatex -interaction=batchmode $FILE"
        ],
        ...
    },
"compile_cases": [
    {
        "match": "regular expression to match case 1",
        "exec": [
            "name of command1",
            "name of command2",
            ...
        ]
    },
    {
        "match": "regular expression to match case 2",
        "exec": [
            "name of command3",
            "name of command4",
            ...
        ]
    },
    ...
],
"default_command": [
    "name of command5",
    "name of command6",
    ...
]
```

The program will read objects in values of `"compile_cases"` in order, searching for strings which matches with regular expression given by value of `"match"`.

If such string exists, then the program cease to matching and commands in the corresponding `"exec"` will be executed.

If nothing in `"compile_cases"` is matched, then commands in `"default_command"` will be executed.

### Customize Files to Delete

Modify values of `"remove_format"` in `settings.json`, add regular expression which match the files you want to remove to its values, then the file will be removed when "Remove temporary files" is executed.

## License

Licensed under the Apache License, Version 2.0. For more details, visit http://www.apache.org/licenses/LICENSE-2.0
