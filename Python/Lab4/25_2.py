import string
import random


def generate_password(count):
    dli = list(string.digits)
    dli.pop(dli.index('0'))
    dli.pop(dli.index('1'))
    uli = list(string.ascii_uppercase)
    uli.pop(uli.index('I'))
    uli.pop(uli.index('O'))
    lli = list(string.ascii_uppercase)
    lli.pop(uli.index('l'))
    lli.pop(uli.index('o'))
    s = [random.choice(dli), random.choice(uli), random.choice(lli)]
    li = dli + uli + lli
    for i in range(count):
        s.append(random.choice(li))
    random.shuffle(s)
    return ''.join(s)


def main(m, n):
    li = []
    for i in range(m):
        li.append(generate_password(n))
    return li
