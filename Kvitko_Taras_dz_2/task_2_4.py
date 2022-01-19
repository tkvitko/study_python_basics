def get_name(string: str) -> str:
    # Функция взятия имени в нужном формате из строки
    source_name = string.split()[-1]
    return source_name.title()


if __name__ == '__main__':

    my_list = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

    for item in my_list:
        name = get_name(item)
        print(f'Привет, {name}!')
