# Helper scripts for Moss

## Description

This repository contains a set of Python scripts I've found useful for preprocessing student's submissions before running them through [Moss](https://theory.stanford.edu/~aiken/moss/).

## Scripts

- `cat-dirs.py`: goes through each subdirectory in a directory, concatenating all source files in that subdirectory (and its child directories, recursively) into a single source file.
  Useful if each of your students' programs is in a different, named subdirectory.

- `replace-spaces-in-filenames.py`: goes through all files in a directory and replaces spaces in the filenames with underscores (`_`).
  Useful since the Moss upload script doesn't seem to work very well with files with spaces in their name.

The scripts are set up for processing C++ source code, but can be easily adapted to work with any other programming language (just change the list of file extensions).

## License

These scripts are MIT licensed, see the [`LICENSE`](LICENSE.txt) file for details.
