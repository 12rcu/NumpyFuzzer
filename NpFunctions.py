from typing import Any

import numpy as np


class FunctionHeader:
    func: Any
    params: [type]
    returns: type

    def __init__(self, func, params: [type], returns: type) -> None:
        self.func = func
        self.params = params
        self.returns = returns


numpy_functions = [
    np.sum, np.prod, np.mean, np.std, np.var,
    np.min, np.max, np.argmin, np.argmax, np.sort
]

assertFunctions = {
    np.sum: [[int, int], lambda x, y: x + y],
    np.prod: [[int, int], lambda x, y: x * y],
    np.min: [[int, int], lambda x, y: x if x < y else y],
    np.max: [[int, int], lambda x, y: x if x > y else y]
}

functionHeaders = [
    FunctionHeader(np.sum, [int, int], np.int64),
    FunctionHeader(np.prod, [int, int], int),
    FunctionHeader(np.mean,[int, int], float),
    FunctionHeader(np.std, [int, int], int),
    FunctionHeader(np.var, [int, int], int),
    FunctionHeader(np.min, [int, int], int),
    FunctionHeader(np.max, [int, int], int),
]