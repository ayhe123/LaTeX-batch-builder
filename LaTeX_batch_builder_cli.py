"""
LaTeX_batch_builder_cli.py
LaTeX-batch-builder command line interface

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

import sys
import os
from multiprocessing import Pool, freeze_support
from itertools import zip_longest
from compile_tools import find_files, remove_file_list, compile_cmd
from read_settings import read_settings


def compile_process(file_name, commands, dir_name, cmd_table):
    """Process that get and compile LaTeX file"""
    os.chdir(dir_name)
    print(f'compiling {file_name}.tex')
    variable = {r'\$FILE': file_name}
    compile_cmd(commands, variable, cmd_table)


def main_ui(process_pool, settings, lang_file):
    """User interface"""
    reply = '-1'
    while reply not in ('0', '1', '2', '4'):
        current_dir = os.path.abspath('')
        files = find_files(settings['compile_cases'],
                           settings['default_command'])
        print('-'*50)
        if files:
            print(lang_file['pwd'])
            print('-'*50)
            for file_name, commands in files:
                print(f'{file_name}.tex\t{commands}')
        else:
            print(lang_file['empty_dir'])
        print('-'*50)
        print(lang_file['choices'])
        reply = input(lang_file['prompt'])
        if reply in ('0', '2'):
            new_files = [(x, y, current_dir, settings['compile_commands'])
                         for x, y in files]
            process_pool.starmap(compile_process, new_files)
        if reply in ('1', '2'):
            remove_files = remove_file_list(settings['remove_format'])
            if remove_files:
                print(lang_file['cleaning_1'])
                print('-'*50)
                for files_line in zip_longest(remove_files[::3],
                                              remove_files[1::3],
                                              remove_files[2::3],
                                              fillvalue=''):
                    print('\t'.join([s.ljust(15) for s in files_line]))
                print('-'*50)
                reply_clean = '0'
                while reply_clean not in ('y', 'n'):
                    reply_clean = input(lang_file['cleaning_2'])
                if reply_clean == 'y':
                    for files in remove_files:
                        os.remove(files)
            else:
                print(lang_file['cleaning_3'])
        if reply == '3':
            print(lang_file['chdir_1'], current_dir)
            reply_dir = input(lang_file['chdir_2'])
            try:
                os.chdir(reply_dir)
            except FileNotFoundError:
                print(lang_file['chdir_3'])


if __name__ == '__main__':
    freeze_support()  # for Windows executable
    result = read_settings()
    if not result:
        sys.exit()
    with Pool(result[0]['num_of_processes']) as pool:
        main_ui(pool, *result)
