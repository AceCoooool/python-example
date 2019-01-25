import os
import argparse


def check_env(env_file):
    for env_check in open(env_file, 'r'):
        env_check = env_check.strip()
        print('[{}]'.format(env_check))
        newenv = os.getenv(env_check)

        if newenv is None:  # If it doesn't exist
            print(env_check, 'is not set')  # Print it is not set
        else:  # Else if it does exist
            print('Current Setting for {}={}\n'.format(env_check, newenv))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check environment')
    parser.add_argument('--env_file', type=str, default='../data/env.conf')

    config = parser.parse_args()

    check_env(config.env_file)
