import random


def get_jokes(count=2, can_repeat=True) -> list:
    """
    Возвращает список шуток в количестве count
    :param count: количество шуток
    :param can_repeat: может ли одно и то же слово повторяться в разных шутках
    :return: список шуток
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []

    if not can_repeat:
        # На случай, если попросили слишком много шуток при условии, что повторять слова нельзя
        min_len = min(len(nouns), len(adverbs), len(adjectives))
        if count > min_len:
            count = min_len

    for i in range(count):
        if can_repeat:
            words_list = list(map(random.choice, [nouns, adverbs, adjectives]))
        else:
            words_list = list(map(lambda x: x.pop(random.randrange(len(x))), [nouns, adverbs, adjectives]))
        list_out.append(' '.join(words_list))

    return list_out


print(get_jokes(can_repeat=False,
                count=10))
print(get_jokes(can_repeat=True,
                count=2))
