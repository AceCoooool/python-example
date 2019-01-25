import argparse


def merge_sort(array):
    mid = (len(array) - 1) // 2
    if len(array) > 2:
        a = merge_sort(array[0:mid])
        b = merge_sort(array[mid:len(array)])
    elif len(array) == 2:
        a = [array[0]]
        b = [array[1]]
    else:
        return array

    i, j = 0, 0
    new = []
    while i != len(a) or j != len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                new += [a[i]]
                i += 1
            else:
                new += [b[j]]
                j += 1
        elif i == len(a) and j != len(b):
            new += [b[j]]
            j += 1
        elif j == len(b) and i != len(a):
            new += [a[i]]
            i += 1
        else:
            break
    return new


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge sort')
    parser.add_argument('--array', type=str, default='5, 2, 3, 1')

    config = parser.parse_args()

    array = [float(a) for a in config.array.split(',')]
    print('array (before sort): ', array)
    array = merge_sort(array)
    print('array (after sort): ', array)
