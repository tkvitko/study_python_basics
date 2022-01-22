def thesaurus(*args) -> dict:
    names_list = args
    result = {}

    for name in names_list:
        if name[0] in result.keys():
            result[name[0]].append(name)
        else:
            result[name[0]] = [name, ]

    return result


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
