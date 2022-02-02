import sys


def get_data_from_file(filename: str) -> (str, int):
    """Функция поиска спамера"""

    stats = {}
    max_count = 0
    spamer_ip = None

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            ip_address = line.split(' ')[0]
            if ip_address in stats.keys():
                stats[ip_address] += 1
            else:
                stats[ip_address] = 1

            # обновляем инфо о максимуме
            if stats[ip_address] > max_count:
                max_count = stats[ip_address]
                spamer_ip = ip_address

    print(f'Статистика заняла {sys.getsizeof(stats)} байт')
    return spamer_ip, max_count


if __name__ == '__main__':
    file_name = 'nginx_logs.txt'
    spamer_ip, max_count = get_data_from_file(filename=file_name)
    print(spamer_ip, max_count)
