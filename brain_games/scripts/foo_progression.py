# file <foo_progression.py>


from random import randint


def foo_progression():
    n_start = randint(0, 100)
    n_diff = randint(1, 10)
    count = n_start
    diaposon = randint(4, 9)
    tiff = randint(0, diaposon)
    txt = ''
    for i in range(0, diaposon + 2):
        count += n_diff
        if i == tiff:
            txt += '.. '
            n = count
        else:
            txt += f'{str(count)} '
    print(f'Question: {txt[:len(txt)-1:]}')
    return n
