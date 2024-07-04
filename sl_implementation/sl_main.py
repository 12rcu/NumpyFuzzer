#!/usr/bin/env python3
"""
Module Docstring
"""
import numpy as np
from fuzzingbook.GrammarFuzzer import *

import ValuePoolFuzzer as v
import GrammarFuzzer as g

import ValuePoolRunner as vr
import GrammarRunner as gr

__author__ = "Sebastian Lommen"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    TRIALS = 22
    print("---------------My ValuePoolFuzzer:----------------")
    exp_runner = vr.ValuePoolRunner(np.exp, [any])
    log10_runner = vr.ValuePoolRunner(np.log10, [any])
    vp_fuzzer = v.ValuePoolFuzzer()
    vp_fuzzer.runs(exp_runner, TRIALS, print_successful=False)
    vp_fuzzer.runs(log10_runner, TRIALS, print_successful=False)

    print("---------------My GrammarFuzzer:----------------")
    g_runner = gr.GrammarRunner()
    g_fuzzer = g.GrammarFuzzer(g.UFUNC_GRAMMAR)
    g_fuzzer.runs(g_runner, trials=TRIALS*2, print_successful=False)

    '''
    print("---------------Fuzzing Book GrammarFuzzer:----------------")
    fpg_fuzzer = GrammarFuzzer(g.UFUNC_GRAMMAR)
    print(fpg_fuzzer.runs(g_runner, TRIALS))
    '''

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
