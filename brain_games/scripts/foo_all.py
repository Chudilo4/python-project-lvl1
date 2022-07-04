# file <foo_all.py>


import prompt
from random import randint, choice


def prime():
    name = hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count <= 2:
        an_tr = 'yes'
        n = randint(1, 3572)
        for i in range(2, n):
            if n % i == 0:
                an_tr = "no"
        print(f'Question: {n}')
        an_us = prompt.string('Your answer: ')
        if an_us == 'yes' and an_tr == 'yes' or an_us == 'no' and an_tr == 'no':
            print('Correct!')
            count += 1
        else:
            loss(an_tr, an_us, name)
            return 0
    print(f'Congratulations, {name}!')


def parity():
    name = hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count <= 2:
        number = randint(0, 100)
        prity = number % 2
        print(f'Question: {number}')
        an_us = prompt.string('Your answer: ')
        an_tr = ''
        if an_us == 'yes' and prity == 0 or an_us == 'no' and prity != 0:
            count += 1
            print('Correct!')
        else:
            if an_us.lower() == 'yes':
                an_tr = 'no'
                loss(an_tr, an_us, name)
                return 0
            else:
                an_tr = 'yes'
                loss(an_tr, an_us, name)
                return 0
    print(f'Congratulations, {name}!')


def progression():
    name = hello()
    print('What number is missing in the progression?')
    count = 0
    while count <= 2:
        txt = ''
        start = randint(0, 100)
        diff = randint(1, 10)
        rang = randint(5, 10)
        tiff = randint(0, rang)
        an_tr = start + (diff * tiff)
        count2 = start
        for i in range(0, rang + 1):
            if i == tiff:
                txt += '.. '
                count2 += diff
            else:
                txt += f'{str(count2)} '
                count2 += diff
        print(f'Question: {txt[:len(txt)-1:]}')
        an_us = prompt.string('Your answer: ')
        if int(an_us) == an_tr:
            print('Correct!')
            count += 1
        else:
            loss(an_tr, an_us, name)
            return 0
    print(f'Congratulations, {name}!')


def gcd():
    name = hello()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    an_tr = 0
    while count <= 2:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        print(f'Question: {n1} {n2}')
        an_tr = foo_gcd(max(n1, n2), min(n1, n2))
        an_us = prompt.string('Your answer: ')
        if int(an_us) == an_tr:
            print('Correct!')
            count += 1
        else:
            loss(an_tr, an_us, name)
            return 0
    print(f'Congratulations, {name}!')


def question():
    name = hello()
    count = 0
    an_tr = 0
    an_us = 0
    while count <= 2:
        r_n = randint(0, 100)
        r_n2 = randint(0, 100)
        an_tr = foo_calc(r_n, r_n2)
        an_us = prompt.string('Your answer: ')
        if int(an_us) == an_tr:
            print('Correct')
            count += 1
        else:
            loss(an_tr, an_us, name)
            return 0
    print(f'Congratulations, {name}!')


def foo_gcd(n1, n2):
    n3 = n1 % n2
    if n3 == 0:
        return n2
    n4 = n2 % n3
    if n4 == 0:
        return n3
    else:
        return foo_gcd(n3, n4)


def foo_calc(rn, rn2):
    sym = ('+', '-', '*')
    rn3 = choice(sym)
    if rn3 == '+':
        print(f'Question: {rn} {rn3} {rn2}')
        return rn + rn2
    elif rn3 == '-':
        print(f'Question: {rn} {rn3} {rn2}')
        return rn - rn2
    else:
        print(f'Question: {rn} {rn3} {rn2}')
        return rn * rn2


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def loss(an_tr, an_us, name):
    print(f'\'{an_us}\' is wrong answer ;(. Correct answer was \'{an_tr}\'.')
    print(f'Let\'s try again, {name}!')
