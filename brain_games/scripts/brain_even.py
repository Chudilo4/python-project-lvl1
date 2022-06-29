# file <brain_even.py>

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer = ''
    count = 0
    wrong_answer = ''
    while count <= 2:
        r_n = randint(1, 100)
        print(f'Question: {r_n}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == 'yes':
            wrong_answer = 'no'
        if answer.lower() == 'no':
            wrong_answer = 'yes'
        if r_n % 2 == 0 and answer == 'yes' or r_n % 2 != 0 and answer == 'no':
            count += 1
            print('Correct!')
        elif r_n % 2 == 0 and answer != 'yes' or r_n % 2 != 0 and answer != 'no':
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{wrong_answer}'.''')
            print(f'''Let's try again, {name}!''')
            break
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
