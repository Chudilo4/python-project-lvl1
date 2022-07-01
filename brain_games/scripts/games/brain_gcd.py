# file <brain_gcd.py>


from brain_games.scripts.hello import hello
from brain_games.scripts.gcd import gcd


def main():
    name = hello()
    gcd(name)


if __name__ == '__main__':
    main()
