import sys
import os


def get_data_from_file(filename: str) -> (str, int):
    """Функция поиска спамера"""

    stats = {}
    max_count = 0
    spammer_ip = None

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

                # обновляем инфо о максимуме
                if stats[ip_address] > max_count:
                    max_count = stats[ip_address]
                    spammer_ip = ip_address

    print(f'Статистика заняла {sys.getsizeof(stats)} байт')
    return spammer_ip, max_count


if __name__ == '__main__':
    file_name = os.path.join('data', 'nginx_logs.txt')
    spammer_ip_, max_count_ = get_data_from_file(filename=file_name)
    print(spammer_ip_, max_count_)
