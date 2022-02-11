import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    re_mail = re.compile(r'[a-zA-Zа-яА-Я0-9_\-]+@[a-zA-Zа-яА-Я0-9_\-]+\.[a-zA-Zа-яА-Я0-9_\-]+')
    if re.compile(re_mail).match(email):
        values = email.split('@')
        return {'username': values[0],
                'domain': values[1]}
    else:
        raise ValueError(f'Wrong email: {email}')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
