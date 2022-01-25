def thesaurus(*args) -> dict:
    names_list = set(args)
    dict_out = dict()

    for name in names_list:
        if name[0] in dict_out.keys():
            dict_out[name[0]].append(name)
        else:
            dict_out[name[0]] = [name]

    # Сортировка словаря по ключам через создание второго словаря:
    sorted_dict = dict()
    for key in sorted(dict_out.keys()):
        sorted_dict[key] = dict_out[key]
    return sorted_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Иван"))
