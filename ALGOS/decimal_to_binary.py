import argparse


def decimal2binary(num, decimal_acc=7):
    whole = []
    fractional = ['.']  # 保存小数部分

    decimal = round(num % 1, decimal_acc)
    w_num = int(num)

    i = 0
    # Loop to find binary of decimal part
    while decimal != 1 and i < decimal_acc:
        decimal = decimal * 2
        fractional.append(int(decimal // 1))
        decimal = round(decimal % 1, decimal_acc)
        if decimal == 0:
            break  # Removes trailing zeros.
        i = i + 1

    # Loop to find binary of whole number part.
    while w_num != 0:
        whole.append(w_num % 2)
        w_num = w_num // 2
    whole.reverse()

    return whole + fractional


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decimal to binary')
    parser.add_argument('--num', type=float, default=10.2)
    parser.add_argument('--acc', type=int, default=7)

    config = parser.parse_args()

    res = decimal2binary(config.num, config.acc)
    print('The', config.num, 'binary form is: ', *res)
