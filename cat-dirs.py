#!/usr/bin/env python3

import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    prog='cat-dirs',
    description='Concatenate source files from subdirectories into a single text file for each subdir'
)

parser.add_argument('base_directory')

args = parser.parse_args()

path = Path(args.base_directory)

if not path.is_dir():
    raise Exception("given path is not a directory")

SOURCE_FILE_EXTENSIONS = (
    'h',
    'hpp',
    'h++',
    'hh',
    'c',
    'cpp',
    'cxx',
    'c++',
)

for dir in path.glob('*/'):
    if not dir.is_dir():
        continue

    dst_file_name = f'{dir.name}.cpp'
    dst_file_path = path.joinpath(dst_file_name)

    with open(dst_file_path, 'w') as fout:
        for extension in SOURCE_FILE_EXTENSIONS:
            for src_file in dir.rglob(f'*.{extension}'):
                with open(src_file, 'r') as fin:
                    contents = fin.read()
                    fout.write(f'// === {src_file.name}:\n\n')
                    fout.write(contents)
                    fout.write('\n\n')
