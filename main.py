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
    np.sum([float("-inf"), float("inf")])
    #np.sum([0, -100, -np.inf, np.inf, -33, 1, 1.0, 3.141592653589793, 32, -33, -33, -100])
    TestValuePool.generate()
    print("Is valid grammar: ")
    print(IpGrammar.ipGrammar())
    print("Random ip: ")
    print(IpGrammar.generateIp())
    TestGenerator.testGenerator()


if __name__ == "__main__":
    main()
