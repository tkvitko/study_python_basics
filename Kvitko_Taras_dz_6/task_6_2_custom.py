import sys


def get_data_from_file(filename: str, min_count_for_spamer=1000) -> list:
    """
    Функция поиска всех спамеров
    (ip-адресов, количество запросов с которых превышает лимит)
    """

    stats = {}
    spamers = {}

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            ip_address = line.split(' ')[0]
            if ip_address in stats.keys():
                stats[ip_address] += 1
            else:
                stats[ip_address] = 1

            # если это спамер, добавляем в словарь спамеров
            if stats[ip_address] > min_count_for_spamer:
                spamers[ip_address] = stats[ip_address]

    sorted_spamers = sorted(spamers.items(), key=lambda item: item[1], reverse=True)
    print(f'Программа заняла {sys.getsizeof(stats) + sys.getsizeof(spamers) + sys.getsizeof(sorted_spamers)} байт')
    return sorted_spamers


if __name__ == '__main__':
    file_name = 'nginx_logs.txt'
    spamers = get_data_from_file(file_name)
    print(spamers)
