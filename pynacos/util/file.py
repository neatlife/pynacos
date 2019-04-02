# coding=utf-8

import errno
import os
import shutil


def read(path):
    with open(path, 'r') as file:
        data = file.read()
        return data


def delete_all(path):
    shutil.rmtree(path)


def delete(path):
    os.remove(path)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def write(path, content):
    with open(path, "w") as text_file:
        text_file.write(content)
