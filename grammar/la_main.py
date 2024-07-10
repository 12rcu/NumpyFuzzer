import sl_implementation.GrammarFuzzer as gf
import sl_implementation.GrammarRunner as gr

import DatetimeGrammar


def main():
    # TRIALS = 100

    print("---------------Datetime GrammarFuzzer:----------------")
    runner = gr.GrammarRunner()
    fuzzer = gf.GrammarFuzzer(DatetimeGrammar.DATETIME_GRAMMAR)
    # fuzzer.runs(runner, trials=TRIALS * 2, print_successful=False)
    fuzzer.runs(runner, timeout_in_sec=60 * 5, print_successful=False)


if __name__ == "__main__":
    main()
