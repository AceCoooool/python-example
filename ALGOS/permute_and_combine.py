import argparse


def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n = n - 1

    return fact


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return permutation(n, r) / factorial(r)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Permutation and Combination')
    parser.add_argument('--n', type=int, default=6)
    parser.add_argument('--r', type=int, default=3)
    parser.add_argument('--c', type=bool, default=False)

    config = parser.parse_args()
    if config.c:
        print('Combination Computation\n')
        res = combination(config.n, config.r)
        print('Combination of {}C{} = {}'.format(config.n, config.r, res))
    else:
        print('Permutation Computation\n')
        res = permutation(config.n, config.r)
        print('Permutation of {}P{} = {}'.format(config.n, config.r, res))
