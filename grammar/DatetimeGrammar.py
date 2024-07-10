from fuzzingbook.Grammars import *

DATETIME_GRAMMAR: Grammar = {
    "<start>": ["<function>"],
    "<function>":
            ["<date> - <date>", "<date> - <timespan>", "<timespan> / <timespan>", "np.busday_offset(<date>, <number>)", "np.is_busday(<date>)", "np.busday_count(<date>, <date>)"],
    "<date>": ["np.datetime64('<formated_date>')"],
    "<timespan>": ["np.timedelta64(<formated_timespan>)"],
    "<formated_date>": ["<year>-<monthday>"],
    "<formated_timespan>": ["'NAT'", "<number>, '<interval>'"],
    "<year>": [str(i) for i in range(-1, 3000)],
    "<monthday>": ["<month28>-<days28>", "<month30>-<days30>", "<month31>-<days31>"],
    "<month28>": ["02"],
    "<month30>": ["04", "06", "07", "09", "11"],
    "<month31>": ["01", "03", "05", "08", "10", "12"],
    "<days28>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 28)],
    "<days30>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 30)],
    "<days31>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 31)],
    "<number>": [str(i) for i in range(-100, 100)],
    "<interval>": ["D", "M", "Y", "h", "m", "s"],
}