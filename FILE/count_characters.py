import pprint
import collections
import argparse


def count_characters(file):
    with open(file, 'r') as f:
        count = collections.Counter(f.read().upper())
    value = pprint.pformat(count)
    print(value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Characters count')
    parser.add_argument('--file', type=str, default='../data/words.txt')

    config = parser.parse_args()

    count_characters(config.file)
