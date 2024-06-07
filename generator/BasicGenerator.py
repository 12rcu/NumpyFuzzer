from NpFunctions import FunctionHeader
from valuepool.ValuePool import *
from threading import Event


class BasicGenerator:
    type_dir: {
        type: set
    } = {}

    def __init__(self):
        pass

    def add_result(self, t: type, entry: Any):
        """
        Inserts an entry into the type_dir
        :param t: the type to add the entry to
        :param entry: the entry to insert
        """
        if self.type_dir.__contains__(t):
            self.type_dir[t].add(entry)
        else:
            self.type_dir[t] = {entry}

    def generate(self, func: FunctionHeader, interrupt: Event):
        """
        executes the function with value pools and saves the result in dictionary
        :param func: the np function that takes only primary types as input to generate more complex input
        :param interrupt: an interrupt event that stops the generation
        """
        wrapper = ValuePoolArgWrapper(func.params)
        while wrapper.execFuzz() or not interrupt.is_set():
            func_result = func.func(wrapper.currentParams)  # todo refactor this call as
            # numpy takes an actual array instead of passing them in like
            # generator.generate(func, *interrupt)
            self.add_result(func.returns, func_result)

    def generate_pool(self, t: type) -> ValuePoolFuzzer:
        """
        Creates a ValuePoolFuzzer with the specified type and adds values from the generate() function
        :param t: the type the ValuePool has
        :return: the ValuePool fuzzer
        """
        assert self.type_dir.__contains__(t)
        return ValuePoolFuzzer(t, self.type_dir[t])
