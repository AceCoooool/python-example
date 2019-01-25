import argparse


def spiral_matrix(n):
    t, r, c = 1, 0, 0
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    if n % 2 == 0:
        k = n // 2
    else:
        k = int((n / 2) + 1)
    for i in range(k):
        while c < n:
            matrix[r][c] = t
            t = t + 1
            c = c + 1
        r = r + 1
        c = c - 1
        while r < n:
            matrix[r][c] = t
            t = t + 1
            r = r + 1
        r = r - 1
        c = c - 1
        while c >= i:
            matrix[r][c] = t
            c = c - 1
            t = t + 1
        c = c + 1
        r = r - 1
        while r > i:
            matrix[r][c] = t
            t = t + 1
            r = r - 1
        r = r + 1
        n = n - 1
        c = c + 1
    return matrix


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Spiral Matrix')
    parser.add_argument('--num', type=int, default=5)

    config = parser.parse_args()
    matrix = spiral_matrix(config.num)
    for m in matrix:
        print(m)
