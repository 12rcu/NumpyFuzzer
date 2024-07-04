from typing import Any

import numpy as np


class FunctionHeader:
    func: Any
    parameter_arr: [type]
    static_parameters: [Any]
    returns: type

    def __init__(self, func, params: [type], static_parameters: [Any], returns: type) -> None:
        self.func = func
        self.parameter_arr = params
        self.static_parameters = static_parameters
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
    FunctionHeader(np.sum, params=[int, int], static_parameters=[None, np.int64], returns=np.int64),
    FunctionHeader(np.sum, params=[float, float], static_parameters=[None, np.float64], returns=np.float64),
    FunctionHeader(np.prod, params=[int, int], static_parameters=[None, np.int64], returns=np.int64),
    FunctionHeader(np.prod, params=[float, float], static_parameters=[None, np.float64], returns=np.float64),
    FunctionHeader(np.mean, params=[int, int], static_parameters=[None, np.float64], returns=np.float64),
    FunctionHeader(np.std, params=[int, int], static_parameters=[None, np.float64], returns=np.float64),
    FunctionHeader(np.var, params=[int, int], static_parameters=[None, np.float64], returns=np.float64),
    FunctionHeader(np.min, params=[int, int], static_parameters=[None, None], returns=np.int64),
    FunctionHeader(np.max, params=[int, int], static_parameters=[None, None], returns=np.int64),
]
