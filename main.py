#!/usr/bin/env python3
"""
Module Docstring
"""

import ValuePool as v

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    fuzzer = v.ValuePoolFuzzer(int)
    print(fuzzer.fuzz())
    print(fuzzer.fuzz())
    print(fuzzer.fuzz())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
