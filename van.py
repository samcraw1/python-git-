#!/usr/bin/env python3

import argparse
from ast import arg


from van_init import init
from van_add import add
from van_commit import commit
from van_log import log
from van_status import status
from van_checkout import checkout
from git_diff import diff

parser = argparse.ArgumentParser(prog="van")
parser.description = "VAN Version Control"


subparsers = parser.add_subparsers(dest="command")

#van init
subparsers.add_parser("init", help="Initialize a new VAN repository")
#van checkout
subparsers.add_parser("checkout", help="Checkout the latest commit")

#van status
subparsers.add_parser("status", help="Show the status of the working directory")

#van diff
diff_subparsers = subparsers.add_parser("diff")
diff_subparsers.add_argument("filename")

#van add
add_subparsers = subparsers.add_parser("add")
add_subparsers.add_argument("filename")


# van commit -m "message"

commit_parser = subparsers.add_parser("commit")
commit_parser.add_argument("-m", "--message", required=True)


#van log
subparsers.add_parser("log")

args = parser.parse_args()

if args.command == "init":
    init()

elif args.command == "commit":
    commit(args.message) 

elif args.command == "add":
    add(args.filename)

elif args.command == "log":
    log()

elif args.command == "status":
    status()

elif args.command == "diff":
    diff(args.filename)
elif args.command == "checkout":
    checkout()

else: 
    parser.print_help()