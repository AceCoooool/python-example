import math
import argparse


def factors(num):
    b = 1
    print('The factors of {} :'.format(num))
    while b <= math.sqrt(num):
        if num % b == 0:
            print("A factor of the number is ", b)
            print("A factor of the number is ", num // b)
        b += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Factors')
    parser.add_argument('--num', type=int, default=10)

    config = parser.parse_args()
    factors(config.num)
