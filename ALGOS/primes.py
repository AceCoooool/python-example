import argparse


def find_primes(num):
    res_list = []
    for i in range(2, num + 1):
        if res_list != [] and any(i % l == 0 for l in res_list):
            continue
        res_list.append(i)
    return res_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find primes')
    parser.add_argument('--num', type=int, default=10)

    config = parser.parse_args()
    res = find_primes(config.num)
    print("The primes in range [2, {}] is:\n {}".format(config.num, res))
