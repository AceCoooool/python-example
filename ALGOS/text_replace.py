import argparse


def text_replace(text, origin_del, replace_del):
    text = text.split(origin_del)
    text = replace_del.join(text)
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text replace')
    parser.add_argument('--text', type=str, default='A man in here')
    parser.add_argument('--origin_del', type=str, default=' ')
    parser.add_argument('--replace_del', type=str, default='-')

    config = parser.parse_args()

    res = text_replace(config.text, config.origin_del, config.replace_del)
    print("text before replace: \n", config.text)
    print("text after replace: \n", res)
