import numpy as np
import numpy.char
from numpy import strings
from numpy.char import *
from fuzzingbook.MutationFuzzer import *
from fuzzingbook import Fuzzer
from fuzzingbook.Fuzzer import *


# Fuzzing book uses three methods: insert, delete and flip random character

def run():
    numbers = [np.str_("1"), np.str_("12"), np.str_("123"), np.str_("1234"), np.str_("12345"), np.str_("100000"),
               np.str_("100000000"), np.str_("1000000000000000")]
    mutation_fuzzer = MutationFuzzer(seed=numbers)
    runner = FunctionRunner(is_digit_test)

    for i in range(1000000000000):
        input_string = mutation_fuzzer.fuzz()
        bytes = input_string.encode()

        reference_check = input_string.isdigit()
        result, outcome = runner.run(input_string)
        if reference_check != (True if outcome == "PASS" else False):
            print(str(i) + ": " + str(input_string) + ": " + str(outcome) + ". Reference says: " + str(reference_check))
            print("Bytes: " + str(bytes))


def is_digit_test(input_string):
    if strings.isdigit(input_string):
        return True
    else:
        raise Exception()


if __name__ == "__main__":
    run()
