# Advent of Code Day 19

import re


if __name__ == '__main__':

    with open('input19.txt') as f:
        lines = f.read().splitlines()

    all = {}
    for line in lines:
        line = line.replace("\"", "")
        index, data = line.split(':')
        all[index] = [int(n) if n.isnumeric() else n for n in data.split()]

    for a in all:
        rule_data = all[a]
        if len(rule_data) > 1:
            for i, rule in enumerate(rule_data):
                if isinstance(rule, int):
                    got = all[str(rule)]
                    if len(got) > 1:
                        rule_data[i] = got
                    else:
                        rule_data[i] = got[0]
    rules = []
    for a in all:
        a = str(all[a]).replace('\'', "").replace(" ", "").replace('[', '(').replace(']', ')').replace(',', '')[1:-1]
        print(a)
        rules.append(a)
    print(rules)

    input_strs = """ababbb
bababa
abbbab
aaabbb
aaaabbb""".splitlines()
    for test_str in input_strs:
        test_results = []
        for pat in rules:
            pattern = re.compile(pat)
            test_results.append(pattern.match(test_str))
        print(any(test_results))
