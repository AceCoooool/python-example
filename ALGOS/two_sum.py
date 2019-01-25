import argparse


def two_sum(nums, target):
    chk_map = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            indices = [chk_map[compl], index]
            print(indices)
            return [indices]
        else:
            chk_map[val] = index
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Two Sum')
    parser.add_argument('--nums', type=str, default="1 2 3 4")
    parser.add_argument('--target', type=int, default=6)

    config = parser.parse_args()
    nums = [int(x) for x in config.nums.strip().split(' ')]
    res = two_sum(nums, config.target)
    if res is False:
        print("There not exists")
