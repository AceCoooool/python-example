import os
import argparse


def create_dir(root):
    if not os.path.exists(root):
        os.makedirs(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Root to create file')
    parser.add_argument('--root', type=str, default='./test/file')

    config = parser.parse_args()
    create_dir(config.root)
