#!/usr/bin/python3
"""
Description:
    The program looks over a given folder for asciidoc/markdown files, and check if every tasks inside files is complete.
    The program has to parse CLI args to process.
    Tasks are simply lines beginning with one of theses two patterns (with any number of whitespaces before):
    `- [ ]` is an incomplete task
    `- [x]` is an complete task

Given:
    - A `folder`, root directory where program looks at files 
    - An `extension`, pointing files we need to check (accepted: asciidoc, adoc, md)

Output:
    Display all files where incomplete tasks remains, foreach, print every incomplete task
"""

import os
import sys
import argparse


def get_files(folder, extension):
    """
    Get all files with given extension in given folder, and subfolders, recursively
    """
    files = []
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files


def get_tasks(file):
    """
    Get all tasks in given file
    """
    tasks = []
    with open(file, 'r') as f:
        for line in f:
            if line.strip().startswith('- [ ]'):
                tasks.append(line)
    return tasks


def check_tasks(tasks):
    """
    Check if all tasks are complete
    """
    return len(tasks) == 0


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description='Check incomplete tasks in asciidoc/markdown files')
    parser.add_argument('folder', help='Folder where program looks for files')
    parser.add_argument('extension', help='Extension of files to check')
    args = parser.parse_args()

    files = get_files(args.folder, args.extension)
    for file in files:
        tasks = get_tasks(file)
        if not check_tasks(tasks):
            print(file+":")
            for task in tasks:
                print(task.rstrip())
            print()


if __name__ == '__main__':
    main()
