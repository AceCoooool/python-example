import os
import argparse


def file_merge(folder, out_file, ext):
    files = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(ext)]
    with open(out_file, 'w') as f:
        for file in files:
            with open(file, 'r') as rf:
                print('File {} readed.'.format(file))
                f.write(rf.read() + '\n')
    print('\n File {} wrote.'.format(out_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File merge')
    parser.add_argument('--folder', type=str, default='../data/txt')
    parser.add_argument('--out_file', type=str, default='../data/results.txt')
    parser.add_argument('--ext', type=str, default='txt')

    config = parser.parse_args()

    with open(config.out_file, 'w+'):
        pass
    if config.ext[0] != '.':
        config.ext = '.' + config.ext

    file_merge(config.folder, config.out_file, config.ext)
