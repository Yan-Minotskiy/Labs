translatedText = None


def translate(text):
    vowel_liters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    punctuation_marks = ['.', ',', '!', '?', '-', ':', ]
    s = ''
    for i in range(len(text)):
        if text[i].lower() not in vowel_liters and punctuation_marks:
            s = s + text[i]
    global translatedText
    translatedText = s
