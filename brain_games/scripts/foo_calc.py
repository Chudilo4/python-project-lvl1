# file <foo_calc.py>


from random import choice


def foo_calc(rn, rn2):
    sym = ('+', '-', '*')
    rn3 = choice(sym)
    if rn3 == '+':
        print(f'Question: {rn}{rn3}{rn2}')
        return rn + rn2
    elif rn3 == '-':
        print(f'Question: {rn}{rn3}{rn2}')
        return rn - rn2
    else:
        print(f'Question: {rn}{rn3}{rn2}')
        return rn * rn2
