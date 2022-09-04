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

import os
import argparse
import pathlib
from multiprocessing import Pool, freeze_support
from itertools import zip_longest
from compile_tools import find_files, remove_file_list, compile_cmd
from read_settings import read_settings
from cli_languages import languages, list_of_languages
from settings import default_settings, export_settings


def reply_yn(message):
    """Display messge, ask for reply until user input 'y' or 'n' """
    reply = '0'
    while reply not in ('y', 'n'):
        reply = input(message)
    if reply == 'y':
        return True
    return False


def compile_process(file_name, file_fullname, commands, dir_name, cmd_table):
    """Process that get and compile LaTeX file"""
    os.chdir(dir_name)
    print(f'compiling {file_fullname}')
    variable = {r'\$FILE_FULL': file_fullname,
                r'\$FILE': file_name}
    compile_cmd(commands, variable, cmd_table)


def main_no_ui(process_pool, settings, args):
    """Proceed without user interface"""
    if args['compile']:
        files = find_files(settings['compile_cases'],
                           settings['default_command'],
                           settings['compile_format'])
        new_files = [(name, fullname, cmd, os.path.abspath(''), settings['compile_commands'])
                     for name, fullname, cmd in files]
        process_pool.starmap(compile_process, new_files)
    if args['remove']:
        for files in remove_file_list(settings['remove_format']):
            os.remove(files)


def main_ui(process_pool, settings, lang_file):
    """User interface"""
    reply = '-1'
    while reply not in ('0', '1', '2', '4'):
        current_dir = os.path.abspath('')
        files = find_files(settings['compile_cases'],
                           settings['default_command'],
                           settings['compile_format'])
        print('-'*50)
        if files:
            print(lang_file['pwd'])
            print('-'*50)
            for _, file_fullname, commands in files:
                print(f"{file_fullname}\t({', '.join(commands)})")
        else:
            print(lang_file['empty_dir'])
        print('-'*50)
        print(lang_file['choices'])
        reply = input(lang_file['prompt'])
        if reply in ('0', '2'):
            new_files = [(name, fullname, cmd, current_dir, settings['compile_commands'])
                         for name, fullname, cmd in files]
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
                if reply_yn(lang_file['cleaning_2']):
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
    parser = argparse.ArgumentParser(
        description="A tool which compiles several LaTeX files simultaneously and deletes temporary files.")
    parser.add_argument(
        "-q", "--quiet", action='store_true',
        help="Don't display user interface and use arguments")
    parser.add_argument(
        "-c", "--compile", action='store_true', help="Compile LaTeX files")
    parser.add_argument(
        "-r", "--remove", action='store_true', help="Remove temporary files")
    parser.add_argument(
        "-d", "--directory", type=pathlib.Path, help="Working directory")
    args = parser.parse_args().__dict__

    if args['directory']:
        os.chdir(args['directory'])
    settings = read_settings()
    if not settings:
        print('Using default settings')
        settings = default_settings
        if not args['quiet'] and reply_yn('Export default settings?[y/n] > '):
            export_settings()

    if args['quiet']:
        with Pool(settings['num_of_processes']) as pool:
            main_no_ui(pool, settings, args)
    else:
        lang_type = list_of_languages.index(settings['language'])
        with Pool(settings['num_of_processes']) as pool:
            main_ui(pool, settings, languages[lang_type])
