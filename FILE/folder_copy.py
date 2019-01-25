import shutil
import argparse


def folder_copy(src_folder, dst_folder):
    shutil.copytree(src_folder, dst_folder)
    print("Finish Copy.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder Copy')
    parser.add_argument('--src_folder', type=str, default='../data/txt')
    parser.add_argument('--dst_folder', type=str, default='../data/txt2')

    config = parser.parse_args()

    folder_copy(config.src_folder, config.dst_folder)
