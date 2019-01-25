import os
import shutil
import argparse

# 注: 你也可以自己增添更多的分类
EXT_VIDEO_LIST = ['FLV', 'WMV', 'MOV', 'MP4', 'MPEG', '3GP', 'MKV', 'AVI']
EXT_IMAGE_LIST = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
EXT_DOCUMENT_LIST = ['DOC', 'DOCX', 'PPT', 'PPTX', 'PAGES', 'PDF', 'ODT', 'ODP', 'XLSX',
                     'XLS', 'ODS', 'TXT', 'IN', 'OUT', 'MD']
EXT_MUSIC_LIST = ['MP3', 'WAV', 'WMA', 'MKA', 'AAC', 'MID', 'RA', 'RAM', 'RM', 'OGG']
EXT_CODE_LIST = ['CPP', 'RB', 'PY', 'HTML', 'CSS', 'JS']
EXT_EXECUTABLE_LIST = ['LNK', 'DEB', 'EXE', 'SH', 'BUNDLE']
EXT_COMPRESSED_LIST = ['RAR', 'JAR', 'ZIP', 'TAR', 'MAR', 'ISO', 'LZ', '7ZIP', 'TGZ', 'GZ', 'BZ2']

TYPES_LIST = ['Video', 'Images', 'Documents', 'Music', 'Codes', 'Executables', 'Compressed']


def organize(root, dirs, name):
    if not os.path.exists(name):
        os.mkdir(name)
    src = '{}/{}'.format(root, dirs)
    dest = '{}/{}'.format(root, name)

    os.chdir(dest)
    shutil.move(src, '{}/{}'.format(dest, dirs))
    print(os.getcwd())
    os.chdir(root)


def file_organize(root, others=False):
    root = os.path.abspath(root)
    os.chdir(root)
    for dirs in os.listdir(root):
        flag = True
        for name, extension_list in zip(TYPES_LIST, [EXT_VIDEO_LIST, EXT_IMAGE_LIST, EXT_DOCUMENT_LIST, EXT_MUSIC_LIST,
                                                     EXT_CODE_LIST, EXT_EXECUTABLE_LIST, EXT_COMPRESSED_LIST]):
            if dirs.split('.')[-1].upper() in extension_list:
                organize(root, dirs, name)
                flag = False
        if flag and others and os.path.isfile(dirs):
            organize(root, dirs, 'Folders')
    print('Done Arranging Files and Folder in your specified directory')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Organization')
    parser.add_argument('--root', type=str, default='../data/file')
    parser.add_argument('--others', type=bool, default=False)

    config = parser.parse_args()

    file_organize(config.root, config.others)
