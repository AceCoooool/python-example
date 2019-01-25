import os
import argparse

fsizedicr = {'Bytes': 1,
             'Kilobytes': float(1) / 1024,
             'Megabytes': float(1) / (1024 * 1024),
             'Gigabytes': float(1) / (1024 * 1024 * 1024)}


def folder_size(folder):
    dir_size = 0
    for (path, dirs, files) in os.walk(folder):
        for file in files:  # Get all the files
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)  # Add the size of each file in the root dir to get the total size.
    fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]  # List of units
    if dir_size == 0:
        print("File Empty")  # Sanity check to eliminate corner-case of empty file.
    else:
        for units in sorted(fsizeList)[::-1]:  # Reverse sort list of units so smallest magnitude units print first.
            print("Folder Size: " + units)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder size')
    parser.add_argument('--folder', type=str, default='../data')

    config = parser.parse_args()
    folder_size(config.folder)