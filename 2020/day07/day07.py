def contains_gold(rule, test):
    ls = [rule]
    i = 0
    for r in test:
        if rule in r[0]:
            break
        i += 1
    if i < len(test):
        r = test[i]
        if rule in r[0]:
            if 'shinygold' in r[1]:
                ls = ls + ['shinygold']
                return ls
            elif 'noother' in r[1]:
                ls = ls + ['noother']
                return ls
            else:
                rr = r[1]
                rr = ''.join([i for i in rr if not i.isdigit()])
                rr = rr.split(',')
                for rrr in rr:
                    ls = ls + contains_gold(rrr, test)
    return ls


if __name__ == '__main__':
    with open("input07.txt") as f:
        test = f.read()
    ll = []
    test = test.splitlines()
    test = [l.replace(" ", "") for l in test]
    test = [l.replace(".", "") for l in test]
    test = [l.replace("bags", "") for l in test]
    test = [l.replace("bag", "") for l in test]
    test = [l.split("contain") for l in test]
    for rule in test:
        ll.append(contains_gold(rule[0], test))
    s = 0
    for l in ll:
        if 'shinygold' in l and l[0] != 'shinygold':
            s += 1
    print(s)
