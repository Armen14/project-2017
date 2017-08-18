#!/usr/bin/python
# -*- coding:utf-8 -*-

import os


def get_directory(dir):
    dirs = []
    files = []

    for dir_name, dir_names, file_names in os.walk(dir):
        dirs.append(dir_name)
        for sub_dir_name in dir_names:
            dirs.append(os.path.join(dir_name, sub_dir_name))
        for file_name in file_names:
            files.append(os.path.join(dir_name, file_name))
            format_filter = filter(lambda x: x.endswith('.pdf'), files)

    return dirs, format_filter

if __name__ == '__main__':
    print get_directory('C:/book')
