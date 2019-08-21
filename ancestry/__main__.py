#!/usr/bin/env python
"""
    __main__.py
    ~~~~~~~~~~~

    ancestry command line interface

    :author: Peter & Heinrich Grabmayr
    :copyright: Copyright (c) 2019
"""
from ancestry import __version__


def _test(message):
    """Run test module.
    Args:
        file (str): the file name of the test module to run.
                If file='', all available test modules are run.
    """
    print('testing the command line')
    if message:
        print('hear, hear: ', message)


def main():
    """Main function called when ancestry is called from the command line.
    Here, commands are parsed and respective funcitons are called.

    Command Line Parameters:
    ------------------------
        ancestry
            test
            find
                threshvals, imgfilename
            combine
            measure
    """
    import argparse
    print('welcome to ancestry ', __version__)

    # Define parsers for all possible command line arguments
    # Main parser
    parser = argparse.ArgumentParser('ancestry')
    subparsers = parser.add_subparsers(dest='command')

    # test parser
    test_parser = subparsers.add_parser('test', help='do a simple test')
    test_parser.add_argument(
                '-m', '--message', type=str, default='',
                help='message to print')

    # Parse the given arguments
    args = parser.parse_args()
    if args.command:
        if args.command == 'test':
            _test(args.message)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
