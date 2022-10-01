def num_translate_adv(number_word: str) -> str:
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if number_word[0].isupper():
        return numbers.get(number_word.lower()).title()
    else:
        return numbers.get(number_word.lower())


print(num_translate_adv('One'))
print(num_translate_adv('two'))
