# file <brain_calc.py>


from brain_games.scripts.hello import hello
from brain_games.scripts.question import question


def main():
    name = hello()
    print(name)
    question('brain_calc', name)


if __name__ == '__main__':
    main()
