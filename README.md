# github-ssh-auth #

Allow `sshd` to use your github ssh keys for authentiacatin you.

## What? ##

Allows you to do ssh login based on public key stored in github.

## Why? ##

I maintain multiple servers with accounts for multiple people. Account
management is a major PITA. I want the following to be true:

1. No password logins
2. People shouldn't have to provide me their keys manually to get setup
3. People shouldn't need *me* to manualy change their keys simply because
   they had lost their previous keys and can not log in
4. I don't want to run ansible/puppet/chef/whatever to maintain user 
   accounts - too complicated for what I want

This enables me to provide all of that, with the only constraint being that
the shell username and the github account name match.

## How? ##

1. Install `python3`
2. Copy the `github-keys-check.py` file into `/usr/local/bin/`
3. Add the following lines to your `sshd` config (usually at `/etc/ssh/sshd_config`):
    ```
    AuthorizedKeysCommand       /usr/local/bin/github-keys-check.py
    AuthorizedKeysCommandUser   nobody
    ```
4. Restart ssh (with `service ssh restart` or similar)
5. Create a useraccount - should match the name of the user on github

This allows the user to authenticate with this ssh daemon by using their github ssh keys.

## Drawbacks ##

1. If GitHub is down, so is your ssh
2. If a user's GitHub account is compromised, so is your ssh
3. If GitHub is compromised, so is your server
4. Requires people to have a github account to be able to ssh into your server
5. GitHub can potentially figure out who the users of a particular IP address are
6. Security is right now somewhat coarse - only min-uid based username validation.
   While this disallows obviously terrible things like the github user 'root' being
   able to ssh into any machine, it isn't good enough.
