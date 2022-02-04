import os
import sys


def get_data_from_file(filename: str, min_count_for_spammer=1000) -> list:
    """
    Функция поиска всех спамеров
    (ip-адресов, количество запросов с которых превышает лимит)
    """

    stats = {}
    spammers = {}

    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line = line.strip()
                ip_address = line.split(' ')[0]
                if ip_address in stats.keys():
                    stats[ip_address] += 1
                else:
                    stats[ip_address] = 1

                # если это спамер, добавляем в словарь спамеров
                if stats[ip_address] > min_count_for_spammer:
                    spammers[ip_address] = stats[ip_address]

    sorted_spammers = sorted(spammers.items(), key=lambda item: item[1], reverse=True)
    print(f'Программа заняла {sys.getsizeof(stats) + sys.getsizeof(spammers) + sys.getsizeof(sorted_spammers)} байт')
    return sorted_spammers


if __name__ == '__main__':
    file_name = os.path.join('data', 'nginx_logs.txt')
    spammers_ = get_data_from_file(file_name)
    print(spammers_)
