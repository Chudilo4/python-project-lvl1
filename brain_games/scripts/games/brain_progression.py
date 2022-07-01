# file <brain_progression.py>


from brain_games.scripts.hello import hello
from brain_games.scripts.progression import progression


def main():
    name = hello()
    progression(name)


if __name__ == '__main__':
    main()
