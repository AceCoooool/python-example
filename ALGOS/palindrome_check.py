import argparse


def palindrome_check(phase):
    string = phase.strip().lower()
    if string == string[::-1]:
        print("\nWow!, The phrase is a Palindrome!")
    else:
        print("\nSorry, The given phrase is not a Palindrome.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Palindrome Check')
    parser.add_argument('--phase', type=str, default='AbbA')

    config = parser.parse_args()

    palindrome_check(config.phase)
