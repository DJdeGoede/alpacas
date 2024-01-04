#!/usr/bin/env python3


def main ():
    print('Yo')
    parent_name = '.'.join(__name__.split('.')[:-1])
    print(__name__)


def myfunc():
    print('Welcome!')


def secondfunc():
    print('Only run me when specified')


if __name__ == '__main__':
    main()
