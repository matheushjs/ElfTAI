#!/usr/bin/python3

import sys
from argparse import ArgumentParser

from TitleManager import TitleManager

def main():
    parser = ArgumentParser(allow_abbrev=True)
    subp = parser.add_subparsers()
    
    list_parser = subp.add_parser('list', aliases=['l'], help='List information about one or all Titles')
    list_parser.add_argument('-e', '--entries', nargs='?', default=5, type=int, help='Number of latest items to print')
    list_parser.add_argument('name', nargs='*', help='Titles about which to print specific information. If none is given, print summary about all Titles.')
    list_parser.set_defaults(func=parse_list)

    args = parser.parse_args()
    with TitleManager('test.csv', 'test_out.csv') as tm:
        try:
            args.func(args, tm)
        except:
            print("Wrong command line operation. Try running '{} -h'".format(sys.argv[0]))

def parse_list(args, tm):
    if len(args.name) != 0:
        for name in args.name:
            if name != args.name[0]: print()
            ok = tm.print_full(name.strip())
            if not ok:
                print("Could not find Title by name/alias '{}'".format(name.strip()))
    else:
        tm.print_summary()

if __name__=='__main__':
    main()
