import os
import requests
from bs4 import BeautifulSoup
import argparse


def get_links(url, ext):
    # create response object
    r = requests.get(url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'html5lib')

    # find all links on web-page
    links = soup.findAll('a')

    # filter the link sending with .mp4
    ext_links = [url + link['href'] for link in links if link['href'].endswith(ext)]

    return set(ext_links)


def download_series(url, ext, out_file):
    links = get_links(url, ext)

    for link in links:

        '''iterate through all links in video_links
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = os.path.join(out_file, link.split('/')[-1])

        print("Downloading the file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All files are downloaded!")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download script')
    parser.add_argument('--url', type=str, default="http://www-personal.umich.edu/~csev/books/py4inf/media/")
    parser.add_argument('--ext', type=str, default='.sh')
    parser.add_argument('--out_file', type=str, default='../data/output')

    config = parser.parse_args()
    if not os.path.exists(config.out_file):
        os.mkdir(config.out_file)

    download_series(config.url, config.ext, config.out_file)
