# file <foo_prime.py>


def foo_prime(n):
    if n % 1 == 0 and n % n == 0 and n != 1:
        return 'yes'
    else:
        return 'no'
