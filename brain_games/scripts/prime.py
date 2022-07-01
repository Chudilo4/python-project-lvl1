# file <prime.py>


import prompt
from random import randint
from brain_games.scripts.loss import loss


def prime(name):
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
            break
    print(f'Congratulations, {name}!')
