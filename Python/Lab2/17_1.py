transliteration_base = {'а': 'a',
                        'б': 'b',
                        'в': 'v',
                        'г': 'g',
                        'д': 'd',
                        'е': 'e',
                        'ё': 'e',
                        'ж': 'zh',
                        'з': 'z',
                        'и': 'i',
                        'й': 'i',
                        'к': 'k',
                        'л': 'l',
                        'м': 'm',
                        'н': 'n',
                        'о': 'o',
                        'п': 'p',
                        'р': 'r',
                        'с': 's',
                        'т': 't',
                        'у': 'u',
                        'ф': 'f',
                        'х': 'kh',
                        'ц': 'tc',
                        'ч': 'ch',
                        'ш': 'sh',
                        'щ': 'shch',
                        'ы': 'y',
                        'э': 'e',
                        'ю': 'iu',
                        'я': 'ia'
                        }
s = input()
ns = ''
for c in s:
    if c.lower() in transliteration_base:
        if c == c.upper():
            ns += transliteration_base[c.lower()].title()
        else:
            ns += transliteration_base[c]
    else:
        ns += c
print(ns)
