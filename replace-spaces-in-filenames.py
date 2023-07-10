#!/usr/bin/env python3

import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    prog='replace-spaces-in-filenames',
    description='Replace spaces in file names'
)

parser.add_argument('directory')

args = parser.parse_args()

path = Path(args.directory)

if not path.is_dir():
    raise Exception("given path is not a directory")

for file in path.glob('*'):
    if ' ' in file.name:
        new_name = file.name.replace(' ', '_')
        file.rename(file.parent.joinpath(new_name))
