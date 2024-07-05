import numpy as np
import numpy.char
from numpy import strings
from numpy.char import *
from fuzzingbook.MutationFuzzer import *
from fuzzingbook import Fuzzer
from fuzzingbook.Fuzzer import *
from datetime import datetime
from dateutil import parser

# Fuzzing book uses three methods: insert, delete and flip random character

def run():
    numbers = [np.str_("1"), np.str_("12"), np.str_("123"), np.str_("1234"), np.str_("12345"), np.str_("100000"),
               np.str_("100000000"), np.str_("1000000000000000")]
    mutation_fuzzer = MutationFuzzer(seed=numbers)
    runner = FunctionRunner(is_digit_test)

    for i in range(1000000000000):
        input_string = mutation_fuzzer.fuzz()

        reference_check = input_string.isdigit()
        result, outcome = runner.run(input_string)
        if reference_check != (True if outcome == "PASS" else False):
            print(str(i) + ": " + str(input_string) + ": " + str(outcome) + ". Reference says: " + str(reference_check) + ". Bytes: " + str(input_string.encode()))

def run_date():
    dates = ['2023-01-01', '2016-12-31 23:59:60.450', '1970-01-01 00:00:00', '0001-01-01 00:00:00', '9999-12-31 23:59:59', '1970-01-01 00:00:00']
    mutation_fuzzer = MutationFuzzer(seed=dates)
    runner = FunctionRunner(is_date_test)

    for i in range(1000000000):
        input_string = mutation_fuzzer.fuzz()

        result, outcome = runner.run(input_string)

        if outcome != "PASS":
            np_date = np.datetime64(input_string)
            print(str(i) + ": " + str(input_string) + ": " + str(np_date) + ". Reference says: " + str(datetime.strptime(input_string, '%m/%d/%y %H:%M:%S')))


def is_date_test(input_string):
    exception = False
    np_date = None
    py_date = None

    try:
        np_date = np.datetime64(input_string)
    except Exception:
        exception = True

    try:
        py_date = datetime.strptime(input_string, '%m/%d/%y %H:%M:%S')
    except Exception:
        return exception

    return np_date.astype('datetime64[s]') == np.datetime64(py_date)

def is_digit_test(input_string):
    if np.all(strings.isdigit(input_string)):
        return True
    else:
        raise Exception()


if __name__ == "__main__":
    run_date()

# Not passing: 9/12/33 23:59:59
