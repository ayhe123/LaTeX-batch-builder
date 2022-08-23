"""
read_settings.py
Reading settings files for LaTeX-batch-builder

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


def read_json(filename):
    """Read json files, get content"""
    try:
        with open(filename, encoding='utf-8') as fp:
            content = json.load(fp)
    except FileNotFoundError:
        print(f'{filename} not found!')
    except json.decoder.JSONDecodeError:
        print(f'{filename} corrupted!')
    else:
        return content
    return False


def check_file(filename, content, check_list):
    """Check content in json files"""
    for key in check_list:
        if key not in content.keys():
            print(f'Item in {filename} is missing!')
            return False
    return True


def read_settings():
    """Read settings.json, check files, get settings"""
    settings = read_json('LaTeX_batch_builder.json')
    if not settings:
        return False
    if not check_file('LaTeX_batch_builder.json', settings, ['language',
                                                  'num_of_processes',
                                                  'compile_commands',
                                                  'compile_cases',
                                                  'default_command',
                                                  'remove_format']):
        return False
    return settings
