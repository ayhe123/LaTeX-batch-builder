"""
compile_tools.py
Some functions used to compile LaTeX files

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

import os
import re


def find_files(cases: list, default_cmd: list):
    """
    Find .tex files and choose command according to file content.

    Parameters
    ----------

    cases: A list of dicts with form {'match':['command1','command2',...]}
    When a .tex file is found, the program will search through the file
    for strings which match with regular expression 'match'. If sonething
    is matched, then it will return ['command1','command2',...].

    default_cmd: A list of commands
    If nothing in cases is matched, then the program will return this.

    Returns
    -------

    A list of (file_name, commands), where file_name is the .tex file
    without ".tex", and commands is a list of corresponding commands.
    """
    files = os.listdir()
    result = []
    for file_fullname in files:
        file_name = '.'.join(file_fullname.split('.')[0:-1])
        file_type = file_fullname.split('.')[-1]
        if file_type == 'tex':
            commands = default_cmd
            with open(file_fullname, encoding='utf-8') as fp:
                context = fp.read()
                for case in cases:
                    if re.findall(case['match'], context):
                        commands = case['exec']
                        break
            result.append((file_name, commands))
    return result


def compile_cmd(commands: list, variables: dict, command_table: list):
    """
    Find commands in command_table, substitute variables (things like $FILE)
    with file name in commands, then execute these commands to compile file
    """
    for cmd_key in commands:
        for cmd_val in command_table[cmd_key]:
            for key, val in variables.items():
                cmd_val = re.sub(key, val, cmd_val)
            os.system(cmd_val)


def remove_file(file_patterns: list):
    """Delete files"""
    for pattern in file_patterns:
        for file in os.listdir():
            if re.findall(pattern, file):
                os.remove(file)
