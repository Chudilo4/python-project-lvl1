# file <foo_parity.py>


from random import randint
import prompt
from brain_games.scripts.loss import loss


def foo_parity(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count <= 2:
        number = randint(0, 100)
        prity = number % 2
        print(f'Question: {number}')
        answr = prompt.string('Your answer: ')
        c = ''
        if answr == 'yes' and prity == 0 or answr == 'no' and prity != 0:
            count += 1
            print('Correct!')
        else:
            if answr.lower() == 'yes':
                c = 'no'
            else:
                c = 'yes'
            loss(c, answr, name)
            break
    print(f'Congratulations, {name}!')
