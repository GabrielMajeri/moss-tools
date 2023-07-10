#!/usr/bin/env python3

import argparse
from pathlib import Path
from sys import stderr

from zipfile import ZipFile

try:
    from unrar.rarfile import RarFile
    unrar_available = True
except ModuleNotFoundError:
    print("module `unrar` is not installed, .rar archives will not be extracted", file=stderr)
    unrar_available = False

parser = argparse.ArgumentParser(
    prog='extract',
    description='Recursively extract all .zip/.rar archives found in a directory and its children'
)

parser.add_argument('base_directory')

parser.add_argument('--remove', dest='remove_after_extraction', action='store_true', help="remove the source archive after extraction is complete")

args = parser.parse_args()

path = Path(args.base_directory)

if not path.is_dir():
    raise Exception("given path is not a directory")

def extract_all(extension):
    for file in path.glob(f'**/*.{extension}'):
        if not file.is_file():
            print(f"cannot read file '{file}', skipping it", file=stderr)
            continue

        print(f"extracting file '{file}'")
        output_dir = file.with_suffix('')

        if file.suffix == '.zip':
            with ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
        elif file.suffix == '.rar':
            if not unrar_available:
                raise Exception("cannot extract RAR archives without the `unrar` module")

            # UnRAR library doesn't support path objects as inputs
            with RarFile(str(file), 'r') as rar_ref:
                rar_ref.extractall(str(output_dir))
        else:
            raise NotImplementedError(f"unsupported file extension for extraction: '{file.suffix}'")

        if args.remove_after_extraction:
            file.unlink()
            print(f"deleted '{file}' after extraction")

SUPPORTED_ARCHIVE_FILE_EXTENSIONS = (
    'zip',
)

if unrar_available:
    SUPPORTED_ARCHIVE_FILE_EXTENSIONS += ('rar',)

for extension in SUPPORTED_ARCHIVE_FILE_EXTENSIONS:
    extract_all(extension)
