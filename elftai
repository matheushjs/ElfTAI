#!/usr/bin/python3

import sys
import termcolor as tc
from argparse import ArgumentParser

from modules_elf import TitleManager

def main():
    parser = ArgumentParser(description="ElfTAI (Title/Alias/Items) - Program for organizing data with specific characteristics.", allow_abbrev=True)
    subp = parser.add_subparsers()
    
    list_parser = subp.add_parser('list', help='List information about one or all Titles')
    list_parser.add_argument('-e', '--entries', nargs='?', default=5, type=int, help='Number of latest items to print')
    list_parser.add_argument('name', nargs="*", help='Titles about which to print specific information. If none is given, print summary about all Titles.')
    list_parser.set_defaults(func=parse_list)

    find_parser = subp.add_parser('find', aliases=['search'], help='Display Titles that contain the given item')
    find_parser.add_argument('item', nargs=1, help='IDs to find')
    find_parser.set_defaults(func=parse_find)

    add_parser = subp.add_parser('add', help='Add a Title, alias or item')
    add_parser.add_argument('-t', '--title', type=str, help="Title to create or to which add the given alias/item")
    add_parser.add_argument('-a', '--alias', type=str, help="Alias to add to the given Title")
    add_parser.add_argument('-i', '--item', type=str, help="Item to add to the given Title")
    add_parser.set_defaults(func=parse_add)

    rm_parser = subp.add_parser('rm', help='Remove a Title, alias or item')
    rm_parser.add_argument('-t', '--title', type=str, help="Title to remove")
    rm_parser.add_argument('-a', '--alias', type=str, help="Alias to remove")
    rm_parser.add_argument('-i', '--item', type=str, help="Item to remove")
    rm_parser.set_defaults(func=parse_rm)

    comm_parser = subp.add_parser('comment', help='Change comment associated to a Title')
    comm_parser.add_argument('-t', '--title', type=str, help="Title of which to change comment")
    comm_parser.add_argument('string', nargs=1, type=str, help="Comment to associate to the Title")
    comm_parser.set_defaults(func=parse_comm)

    # TODO: operation 'name' for editing Title's title
    # TODO: operation 'comment' for editing/appending/adding comments

    args = parser.parse_args()
    with TitleManager('database.csv', 'backup_database.csv') as tm:
        try:
            args.func(args, tm)
        except:
            print("Wrong command line operation. Try running '{} -h'".format(sys.argv[0]))

def parse_list(args, tm):
    if len(args.name) != 0:
        for name in args.name:
            if name != args.name[0]: print()
            ok = tm.print_full(name.strip(), args.entries)
            if not ok:
                print("Could not find Title by name/alias '{}'".format(name.strip()))
    else:
        tm.print_summary()

def parse_find(args, tm):
    tm.find_item(args.item[0])

def parse_add(args, tm):
    if not args.title:
        print("You need to specify a Title upon which to operate. Use the -t directive.")
        return

    if args.alias and args.item:
        print("For simplicity purposes, you cannot add alias and items together.\nUse 2 separate commands, please.")
        return

    if args.alias:
        retval = tm.add_node(args.title, args.alias)
        if retval is True:
            print("Created Title '{}', with alias '{}'".format(args.title, args.alias))
        else:
            tm.add_alias(args.title, args.alias)
            print("Added alias '{}' to Title identified by '{}'.".format(args.alias, args.title))

    elif args.item:
        retval = tm.add_node(args.title)
        if retval is True:
            tm.add_item(args.title, args.item)
            print("Created Title '{}', with item '{}'".format(args.title, args.item))
        else:
            retval = tm.add_item(args.title, args.item)
            if retval is True:
                print("Added item '{}' to Title identified by '{}'".format(args.item, args.title))
            else:
                print("Item already exists in Title identified by '{}'".format(args.item, args.title))
    else:
        retval = tm.add_node(args.title)
        if retval is True:
            print("Created Title '{}'".format(args.title))
        else:
            print("Title already exists! Nothing has been done.")

def parse_rm(args, tm):
    if args.alias:
        if args.item:
            print("Ignoring the given item. Delete it on a separate execution, please.")
        if args.title:
            print("Title is not needed when deleting an alias, hence will be ignored.")

        retval = tm.rm_alias(args.alias)
        if len(retval) != 0:
            print("Could not remove alias '{}'. Confirm if it exists.".format(args.alias))
        else:
            print("Removed alias '{}'".format(args.alias))

    elif args.item:
        if not args.title:
            print("Items can only be removed from a single Title. Specify a Title with -t")
            return

        retval = tm.rm_item(args.title, args.item)
        if retval is True:
            print("Removed item '{}' from Title identified by '{}'".format(args.item, args.title))
        else:
            #TODO: Add a function to check if the node exists or not. Can be done using EXCEPTIONS.
            print("Could not remove item '{}' from Title identified by '{}'.".format(args.item, args.title))
            print("Either the Title doesn't exist, or the Title found doesn't have the given item.")

    elif args.title:
        inp = input(tc.colored("Confirm removal of Title identified by '{}' [Y/n]: ".format(args.title), "red", attrs=['bold']))
        if inp.lower().strip() == 'y':
            retval = tm.rm_node(args.title)
            if retval is True:
                print("Removed")
            else:
                print("Title doesn't exist. Nothing has been done.")
        else:
            print("Canceled")

    else:
        print("Please, provide one of the following:\n1) A title with -t\n2) An alias with -a\n3) An item with -i and a title/alias with -t")

def parse_comm(args, tm):
    if not args.title:
        print("You must provide a title using argument directive -t")
        return
    
    retval = tm.set_comment(args.title, args.string[0])
    if retval is None:
        print("Could not find Node identified by title '{}'".format(args.title))
    else:
        print("Replaced old comment '{}'".format(retval))

if __name__=='__main__':
    main()
