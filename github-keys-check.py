#!/usr/bin/python3
import urllib.request
import argparse
import pwd
import grp
import sys


def key_for_user(user):
    url = 'https://github.com/%s.keys' % user
    with urllib.request.urlopen(url) as f:
        return f.read().decode('utf-8')


def validate_user(username, min_uid, in_group):
    """
    Validates that a given username is:

        1. A valid, existing user
        2. Is a member of the group in_group
        3. Has uid > min_uid
    """
    user = pwd.getpwnam(username)
    if in_group is None or username in grp.getgrnam(in_group).gr_mem:
        return user.pw_uid > min_uid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument(
        '--min-uid', type=int, default=999,
        help='uid must be > this to be allowed ssh access. \
              Helps keep system users non-sshable'
    )
    parser.add_argument(
        '--in-group', default=None,
        help='Only users in this group can login via github keys'
    )
    args = parser.parse_args()
    if validate_user(args.username, args.min_uid, args.in_group):
        print(key_for_user(args.username))
    else:
        print("Not a valid user")
        sys.exit(1)
