def palindrome(s):
    s = ''.join(s.split()).lower()
    if s == s[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'
