# file <prime.py>


import prompt
from random import randint
from brain_games.scripts.foo_prime import foo_prime
from brain_games.scripts.loss import loss


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    an_tr = 'no'
    count = 0
    while count <= 2:
        n = randint(1, 3572)
        an_tr = foo_prime(n)
        print(f'Question: {n}')
        an_us = prompt.string('Your answer: ')
        print(an_tr)
        if an_us == 'yes' and an_tr == 'yes' or an_us == 'no' and an_tr == 'no':
            print('Correct!')
            count += 1
        else:
            loss(not an_us, an_us, name)
            break
        print(f'Congratulations, {name}!')
