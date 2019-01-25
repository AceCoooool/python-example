from urllib import request
import argparse


def check_internet_connectivity(url):
    try:
        request.urlopen(url, timeout=2)
        print("Working connection")

    except request.URLError as E:
        print("Connection error:%s" % E.reason)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Internet Connect')
    parser.add_argument('--url', type=str, default="http://baidu.com")

    config = parser.parse_args()
    check_internet_connectivity(url=config.url)
