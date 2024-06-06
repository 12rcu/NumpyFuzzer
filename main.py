#!/usr/bin/env python3
"""
Module Docstring
"""

from grammar import IpGrammar
from valuepool import TestValuePool
from generator import TestGenerator
import numpy as np


def main():
    np.sum([100000000000000, 1])
    TestValuePool.generate()
    print("Is valid grammar: ")
    print(IpGrammar.ipGrammar())
    print("Random ip: ")
    print(IpGrammar.generateIp())
    TestGenerator.testGenerator()


if __name__ == "__main__":
    main()
