# file <brain_calc.py>


from brain_games.scripts.hello import hello
from brain_games.scripts.question import question


def main():
    name = hello()
    question(name)


if __name__ == '__main__':
    main()
