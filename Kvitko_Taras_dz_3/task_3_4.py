def thesaurus_adv(*args):
    pairs_list = args
    result = {}

    for pair in pairs_list:
        pair_list = pair.split(' ')
        if len(pair_list) != 2:
            return 'Wrong element in list'
        else:
            name = pair_list[0].title()  # поддержка имен и фамилий с маленькой буквы
            surname = pair_list[1].title()

            if surname[0] in result.keys():
                if name[0] in result[surname[0]]:
                    result[surname[0]][name[0]].append(pair)
                else:
                    result[surname[0]][name[0]] = [pair]
            else:
                result[surname[0]] = {name[0]: [pair]}

    return result


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
