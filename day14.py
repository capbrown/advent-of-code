import re


def chemistry(recipes, need, need_n, n_ore, made):
    print(')))', need_n, ',', recipes[need][0], need, '=>', end=' ')
    for val in recipes[need][1]:
        print('(', recipes[need][1][val], val, ')', end=' ')
    print()
    print(made)
    next_needs = list(recipes[need][1].keys())
    nnn = need_n // recipes[need][0]

    for n in next_needs:
        if n == 'ORE':
            made[need] = recipes[need][0] - need_n
            if made[need] < 0:
                made[need] = 0
            n_ore += recipes[need][1][n]
            return n_ore, recipes[need][0]

        if need in made.keys():
            now_need = recipes[need][1][n] - made[need]
        else:
            now_need = recipes[need][1][n]
        if n in made.keys():
            if made[n] > 0:
                now_need -= made[n]
                made[n] -= now_need
                if made[n] < 0:
                    made[n] = 0

        if now_need > 0:
            for NNN in range(nnn):
                n_ore, now_need = chemistry(recipes, n, now_need, n_ore, made)

    return n_ore, now_need


lineList = [line.rstrip('\n') for line in open('inputs/day14.txt')]
reactions = []
for string in lineList:
    reactions.append(tuple([c for c in re.sub('[,]', '', string).split(' => ')]))

reactions = [tuple((tuple(a[0].split(' ')), tuple(a[1].split(' ')))) for a in reactions]
recipes = {}
for reaction in reactions:
    r = reactions.index(reaction)
    r_in = reaction[0]
    r_out = reaction[1]
    r_input_2 = {}
    while len(r_in) > 2:
        r_input_2[r_in[1]] = int(r_in[0])
        r_in = r_in[2:]
    r_input_2[r_in[1]] = int(r_in[0])
    recipes[r_out[1]] = (int(r_out[0]), r_input_2)

print(chemistry(recipes, 'FUEL', 1, 0, {}))
