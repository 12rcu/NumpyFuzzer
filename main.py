#!/usr/bin/env python3
"""
Module Docstring
"""
import numpy as np

import ValuePool as v

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

numpy_functions = [
    np.sum, np.prod, np.mean, np.std, np.var,
    np.min, np.max, np.argmin, np.argmax, np.sort
]

functions2 = {
    np.sum: [int, int]

}


def generate():
    for (func, types) in functions2.items():
        pools = []

        for type in types:
            pools.append(v.ValuePoolFuzzer(type))

        arguments = []
        for pool in pools:
            arguments.append(pool.fuzz())

        result = func(*arguments)
        print(result)


def main():
    generate()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
