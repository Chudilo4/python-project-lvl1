# file <foo_prime.py>


def foo_prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            if count > 1:
                return 'yes'
            else:
                return 'no'
