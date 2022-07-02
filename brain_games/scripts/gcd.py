# file <gcd.py>


from random import randint
import prompt
from brain_games.scripts.loss import loss
from brain_games.scripts.foo_gcd import foo_gcd


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    count = 0
    tr_an = 0
    while count <= 2:
        n1 = randint(0, 100)
        n2 = randint(0, 100)
        print(f'Question: {n1} {n2}')
        tr_an = foo_gcd(max(n1, n2), min(n1, n2))
        us_an = prompt.string('Your answer: ')
        if int(us_an) == tr_an:
            print('Correct!')
            count += 1
        else:
            loss(tr_an, us_an, name)
            return 0
    print(f'Congratulations, {name}!')
