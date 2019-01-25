# Note: only support linux
import os
from time import strftime
import argparse


def file_zip(folder, ext, remove=False):
    folder = os.path.abspath(folder)
    if ext[0] != '.':
        ext = '.' + ext
    files = [file for file in os.listdir(folder) if file.endswith(ext)]
    zipname = strftime("%Y-%m-%d") + '.zip'
    os.chdir(folder)
    os.system('zip ' + zipname + " " + ' '.join(files))
    if remove:
        for file in files:
            os.remove(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File zip')
    parser.add_argument('--folder', type=str, default='../data/txt')
    parser.add_argument('--ext', type=str, default='txt')
    parser.add_argument('--remove', type=bool, default=False)

    config = parser.parse_args()
    file_zip(config.folder, config.ext, config.remove)