# file <progression.py>


import prompt
from brain_games.scripts.loss import loss
from brain_games.scripts.foo_progression import foo_progression


def progression(name):
    print('What number is missing in the progression?')
    pr_true = 0
    count = 0
    while count <= 2:
        pr_true = foo_progression()
        an_us = prompt.string('Your answer: ')
        if int(an_us) == pr_true:
            print('Correct')
            count += 1
        else:
            loss(pr_true, an_us, name)
            break
        print(f'Congratulations, {name}!')
