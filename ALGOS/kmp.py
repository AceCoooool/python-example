import argparse


def kmp(pattern, text):
    # 1) Construct the failure array
    failure = [0]
    i = 0
    for index, char in enumerate(pattern[1:]):
        if pattern[i] == char:
            i += 1
        else:
            i = 0
        failure.append(i)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return True
            i += 1
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif failure[j] > 0:
            j = failure[j] - 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KMP string match Algorithm')
    parser.add_argument('--pattern', type=str, default='Abc')
    parser.add_argument('--text', type=str, default='AcbacbAbc')

    config = parser.parse_args()
    if kmp(config.pattern, config.text):
        print("Match. Success !!!")
    else:
        print("Can not match. Failed !!!")
