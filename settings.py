"""
settings.py
Settings files for LaTeX-batch-builder

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

import json


def export_settings():
    """Export default settings"""
    with open('LaTeX_batch_builder.json', 'w', encoding='utf-8') as fp:
        json.dump(default_settings, fp)


default_settings = {
    "language": "en",
    "num_of_processes": 5,
    "compile_format": [
        "tex"
    ],
    "compile_commands": {
        "xelatex": [
            "xelatex -interaction=batchmode '$FILE'"
        ],
        "xelatex*2": [
            "xelatex -interaction=batchmode '$FILE'",
            "xelatex -interaction=batchmode '$FILE'"
        ],
        "pdflatex": [
            "pdflatex -interaction=batchmode '$FILE'"
        ],
        "pdflatex*2": [
            "pdflatex -interaction=batchmode '$FILE'",
            "pdflatex -interaction=batchmode '$FILE'"
        ],
        "biber": [
            "biber -q '$FILE'"
        ],
        "bibtex": [
            "bibtex -terse '$FILE'"
        ],
        "makeindex": [
            "makeindex '$FILE'"
        ]
    },
    "compile_cases": [
        {
            "match": "\\\\printbibliography",
            "exec": [
                "xelatex",
                "biber",
                "xelatex*2"
            ]
        },
        {
            "match": "\\\\bibliography",
            "exec": [
                "xelatex",
                "bibtex",
                "xelatex*2"
            ]
        },
        {
            "match": "\\\\printindex",
            "exec": [
                "xelatex",
                "makeindex",
                "xelatex*2"
            ]
        }
    ],
    "default_command": [
        "xelatex*2"
    ],
    "remove_format": [
        "__latexindent_temp\\.tex",
        ".*\\.aux",
        ".*\\.bbl",
        ".*\\.blg",
        ".*\\.log",
        ".*\\.out",
        ".*\\.toc",
        ".*\\.bcf",
        ".*\\.xml",
        ".*\\.synctex",
        ".*\\.nlo",
        ".*\\.nls",
        ".*\\.bak",
        ".*\\.ind",
        ".*\\.idx",
        ".*\\.ilg",
        ".*\\.lof",
        ".*\\.lot",
        ".*\\.ent-x",
        ".*\\.tmp",
        ".*\\.ltx",
        ".*\\.los",
        ".*\\.lol",
        ".*\\.loc",
        ".*\\.listing",
        ".*\\.gz",
        ".*\\.userbak",
        ".*\\.nav",
        ".*\\.snm",
        ".*\\.vrb",
        ".*\\.synctex\\(busy\\)",
        ".*\\.nav",
        ".*\\.snm",
        ".*\\.vrb",
        ".*\\.fls",
        ".*\\.xdv",
        ".*\\.fdb_latexmk"
    ]
}
