import os
import argparse


def script_list(root, log_file):
    root = os.path.abspath(root)
    with open(log_file, 'w') as log:
        for dirpath, dirname, filenames in os.walk(root):
            for filename in filenames:
                log.write(os.path.join(dirpath, filename) + '\n')
    print("\nYour logfile ", log_file, "has been created")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script listing')
    parser.add_argument('--folder', type=str, default='../data/txt')
    parser.add_argument('--log_file', type=str, default='../data/log/script_list.log')

    config = parser.parse_args()
    with open(config.log_file, 'w+') as f: pass

    script_list(config.folder, config.log_file)
