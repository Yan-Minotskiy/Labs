def brackets_check(s):
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                print('NO')
                return False
    if meetings == 0:
        print('YES')
    else:
        print('NO')
    return meetings == 0
