# file <brain_prime.py>


from brain_games.scripts.hello import hello
from brain_games.scripts.prime import prime


def main():
    name = hello()
    prime(name)


if __name__ == '__main__':
    main()
