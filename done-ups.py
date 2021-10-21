#!/usr/bin/python3
"""
Description:
    The program looks over a given folder for an asciidoc/markdown file, and check every done tasks for a given day (default yesterday).
    The program has to parse CLI args to process.
    The target file is a concatenation of the given folder, the day, and the extension
    Tasks are simply lines beginning with one of theses two patterns (with any number of whitespaces before):
    `- [ ]` is an incomplete task
    `- [x]` is an complete task

Given:
    - A `folder`, root directory where program looks at files 
    - An `extension`, pointing files we need to check (accepted: asciidoc, adoc, md)
    - A `day` (ex: 2021/21/12), default yesterday

Output:
    Display the target file and print every complete task
"""

import os
import sys
import argparse
import datetime


def get_tasks(file):
    """
    Get all tasks in given file
    """
    tasks = []
    with open(file, 'r') as f:
        for line in f:
            if line.strip().startswith('- [x]'):
                tasks.append(line)
    return tasks


def get_yesterday():
    """
    Get a string that represent yesterday (ex: 2021/12/11)
    """
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    return yesterday.strftime("%Y/%m/%d")


def get_file(folder, day, extension):
    """
    Get the target file
    """
    return os.path.join(folder, day + '.' + extension)


def main():
    parser = argparse.ArgumentParser(
        description='Display tasks done for a given day')
    parser.add_argument('folder', help='Folder where to look for files')
    parser.add_argument(
        '-d', '--day', help='Day to check (default: yesterday)', default=get_yesterday())
    parser.add_argument(
        '-e', '--extension', help='File extension to look for (default: asciidoc)', default='md')
    args = parser.parse_args()

    file = get_file(args.folder, args.day, args.extension)
    if not os.path.isfile(file):
        print('File not found:', file)
        sys.exit(1)

    tasks = get_tasks(file)
    if len(tasks) == 0:
        print('No task found')
    else:
        print('Tasks done:')
        for task in tasks:
            print(task, end='')


if __name__ == '__main__':
    main()
