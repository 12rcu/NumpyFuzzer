import numpy
from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np
from random import randrange


class ValuePool:
    pool = []
    index = 0

    def __init__(self) -> None:
        """Constructor"""
        pass

    def getNextValue(self):
        ret = self.pool[self.index]
        self.index = self.index + 1
        if len(self.pool) == self.index:
            self.index = randrange(len(self.pool))
        return ret


class IntValuePool(ValuePool):
    pool = [0, 1, -1, 10, 100, 100_000_000_000_000, 16, 32, 512, -10, -100, -17, -33]


class FloatValuePool(ValuePool):
    pool = [0.0, -1.0, 1.0, float("inf"), float("-inf"), numpy.inf, numpy.euler_gamma, numpy.pi, numpy.e]


class ArrayValuePool(ValuePool):
    pool = [
        np.array([]),
        np.array([1, 2, 3]),
        np.array([-1, 1, 0]),
        np.array([0]),
        np.array([100_000, -100_000]),
        np.zeros((10, 10))
    ]


class ValuePoolFuzzer(Fuzzer):

    def __init__(self, t: type, values: Any = None) -> None:
        super().__init__()
        if values is not None:
            self.valuePool = ValuePool()
            self.valuePool.pool = values
        elif t == int:
            self.valuePool = IntValuePool()
        elif t == float:
            self.valuePool = FloatValuePool()
        else:
            raise NotImplemented()

    def fuzz(self):
        """Return fuzz input"""
        return self.valuePool.getNextValue()

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for i in range(trials)]


class ValuePoolArgWrapper(Fuzzer):
    pools: [ValuePoolFuzzer] = []
    current_params: [] = []
    index = 0

    def __init__(self, args: [type]):
        super().__init__()
        for argType in args:
            pool = ValuePoolFuzzer(argType)
            self.pools.append(pool)
            self.current_params.append(pool.fuzz())

        assert len(self.pools) == len(self.current_params)

    def execFuzz(self) -> bool:
        """bump index"""
        self.index = self.index + 1

        tmp_index = 1
        for accessIndex in range(len(self.pools)):
            if self.index % tmp_index:
                self.current_params[accessIndex] = self.pools[accessIndex].fuzz()
            tmp_index += len(self.pools[accessIndex].valuePool.pool)

        if tmp_index < self.index:
            return False  # all parameters were exhaustively fuzzed
        else:
            return True

    def fuzz(self):
        self.execFuzz()
        """Returns an array of with types specified in the constructor """
        return self.current_params
