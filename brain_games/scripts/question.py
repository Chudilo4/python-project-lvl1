# file <question.py>


from random import randint
import prompt
from brain_games.scripts.loss import loss
from brain_games.scripts.foo_calc import foo_calc


def question(name):
    count = 0
    answr_true = 0
    answr_user = 0
    while count <= 2:
        r_n = randint(0, 100)
        r_n2 = randint(0, 100)
        answr_true = foo_calc(r_n, r_n2)
        answr_user = prompt.string('Your answer: ')
        if int(answr_user) == answr_true:
            print('Correct')
            count += 1
        else:
            loss(answr_true, answr_user, name)
            break
        print(f'Congratulations, {name}!')
