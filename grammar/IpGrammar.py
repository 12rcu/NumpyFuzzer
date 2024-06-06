from fuzzingbook.GrammarFuzzer import *

IP_GRAMMAR: Grammar = {
    "<start>": ["<Num>.<Num>.<Num>.<Num>"],
    "<Num>": ["<3Digits>", "<2Digits>", "<Digit>"],
    "<3Digits>": ["2<2DigitsR>", "1<Digit><Digit>"],
    "<2Digits>": ["<DigitP><Digit>"],
    "<2DigitsR>": ["55", "5<DigitR>", "<DigitR><Digit>"],
    "<Digit>": ["0", "<DigitP>"],
    "<DigitP>": ["1", "2", "3", "4", "5 ", "6", "7", "8", "9"],
    "<DigitR>": ["0", "1", "2", "3", "4"]
}


def ipGrammar():
    return is_valid_grammar(IP_GRAMMAR)


def generateIp():
    return GrammarFuzzer(IP_GRAMMAR).fuzz()
