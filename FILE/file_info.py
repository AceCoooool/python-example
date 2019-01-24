import os
import stat  # index constants for os.stat()
import time
import argparse


def file_info(file):
    count = 0
    with open(file, 'r') as f:
        for _ in f:
            count += 1
    with open(file, 'r') as f:
        inp = f.read()
        t_char = len(inp)
    file_stats = os.stat(file)
    print("This is os.stat", file_stats)

    # create a dictionary to hold file info
    file_info = {
        'fname': file,
        'fsize': file_stats[stat.ST_SIZE],
        'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME])),
        'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_ATIME])),
        'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_CTIME])),
        'no_of_lines': count,
        't_char': t_char
    }

    print("\nfile name =", file_info['fname'])
    print("file size =", file_info['fsize'], "bytes")
    print("last modified =", file_info['f_lm'])
    print("last accessed =", file_info['f_la'])
    print("creation time =", file_info['f_ct'])
    print("Total number of lines are =", file_info['no_of_lines'])
    print("Total number of characters are =", file_info['t_char'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Information')
    parser.add_argument('--file', type=str, default='../LICENSE')

    config = parser.parse_args()
    file_info(config.file)
