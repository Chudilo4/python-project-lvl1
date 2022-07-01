# file <foo_gcd.py>


def foo_gcd(n1, n2):
    n3 = n1 % n2
    if n3 == 0:
        return n2
    n4 = n2 % n3
    if n4 == 0:
        return n3
    else:
        return foo_gcd(n3, n4)
