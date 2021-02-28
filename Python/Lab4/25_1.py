import string
import random


def generate_password(count):
    li = list((string.digits + string.ascii_letters))
    li.pop(li.index('l'))
    li.pop(li.index('I'))
    li.pop(li.index('1'))
    li.pop(li.index('o'))
    li.pop(li.index('O'))
    li.pop(li.index('0'))
    s = ''
    for i in range(count):
        s += random.choice(li)
    return s


def main(m, n):
    li = []
    for i in range(m):
        li.append(generate_password(n))
    return li
