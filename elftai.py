#!/usr/bin/python3

from argparse import ArgumentParser

from TitleManager import TitleManager

def main():
    parser = ArgumentParser(allow_abbrev=True)
    subp = parser.add_subparsers()
    
    list_parser = subp.add_parser('list', aliases=['l'], help='List information about one or all Titles')
    list_parser.add_argument('-e', '--entries', nargs='?', default=5, type=int, help='Number of latest items to print')
    list_parser.add_argument('names', nargs='*', help='Titles about which to print specific information. If none, print summary about all Titles.')
    list_parser.set_defaults(func=parse_list)

    args = parser.parse_args()
    args.func(args)

def parse_list(args):
    with TitleManager('test.csv', 'test_out.csv') as tm:
        if len(args.names) != 0:
            for name in args.names:
                if name != args.names[0]: print()
                # tm.printsummary
        else:
            tm.print_summary()

if __name__=='__main__':
    main()
