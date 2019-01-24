import shutil
import time
import os
import argparse


def move_files(src_dir, dst_dir, days):
    src_dir = os.path.abspath(src_dir)
    dst_dir = os.path.abspath(dst_dir)
    now = time.time()
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for f in os.listdir(src_dir):
        f = os.path.join(src_dir, f)
        if os.stat(f).st_mtime < now - days * 86400:  # Work out how old they are, if they are older than 240 days old
            if os.path.isfile(f):  # Check it's a file
                shutil.move(f, dst_dir)  # Move the files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File remove')
    parser.add_argument('--src_dir', type=str, default='./test')
    parser.add_argument('--dst_dir', type=str, default='./test')
    parser.add_argument('--days', type=int, default=1)

    config = parser.parse_args()
    move_files(config.src_dir, config.dst_dir, config.days)
