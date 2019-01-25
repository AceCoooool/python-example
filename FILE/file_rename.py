import os
import argparse


def batch_rename(work_dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    """
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    for filename in os.listdir(work_dir):
        # Get the file extension
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext

            # Write the files
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('--work_dir', type=str, default='../data/txt',
                        help='the directory where to change extension')
    parser.add_argument('--old_ext', type=str, default='txt', help='old extension')
    parser.add_argument('--new_ext', type=str, default='cpp', help='new extension')
    config = parser.parse_args()

    batch_rename(config.work_dir, config.old_ext, config.new_ext)
