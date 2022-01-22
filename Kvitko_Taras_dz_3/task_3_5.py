import random


def get_jokes(jokes_count=2, can_repeat=True) -> list:
    """
    Функция генерации шуток
    :param jokes_count: количество шуток
    :param can_repeat: может ли одно и то же слово повторяться в разных шутках
    :return: список шуток
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes_list = []
    for i in range(jokes_count):
        if can_repeat:
            words_list = list(map(random.choice, [nouns, adverbs, adjectives]))
        else:
            words_list = list(map(lambda x: x.pop(random.randrange(len(x))), [nouns, adverbs, adjectives]))
        jokes_list.append(' '.join(words_list))

    return jokes_list


print(get_jokes(can_repeat=False,
                jokes_count=4))
