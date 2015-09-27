#!/usr/bin/python3
import urllib.request
import argparse


def key_for_user(user):
    url = 'https://github.com/%s.keys' % user
    with urllib.request.urlopen(url) as f:
        return f.read().decode('utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    args = parser.parse_args()
    print(key_for_user(args.username))
