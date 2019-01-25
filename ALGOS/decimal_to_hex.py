import argparse


def decimal2hex(num):
    return hex(int(num))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decimal to hex')
    parser.add_argument('--num', type=int, default=10)

    config = parser.parse_args()

    res = decimal2hex(config.num)
    print('The', config.num, 'hex form is: ', res)
