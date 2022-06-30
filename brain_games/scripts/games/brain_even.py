# file <brain_even.py>

from brain_games.scripts.hello import hello
from brain_games.scripts.foo_parity import foo_parity


def main():
    name = hello()
    foo_parity(name)


if __name__ == '__main__':
    main()
