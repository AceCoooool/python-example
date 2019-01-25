import os
import argparse


def count_files(path, extensions):
    counter = 0
    for root, dirs, files in os.walk(path):  # Loop through all the directories in the given path
        for file in files:  # For all the files
            counter += file.endswith(extensions)  # Count the files
    return counter  # Return the count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script count')
    parser.add_argument('--folder', type=str, default='.')
    parser.add_argument('--ext', type=str, default='py')

    config = parser.parse_args()
    if config.ext[0] != '.':
        config.ext = '.' + config.ext

    count = count_files(config.folder, config.ext)
    print('Extension({}): there are {} {} files.'.format(config.ext, count, config.ext))
