import os


def show_stats(base_dir: str) -> dict:
    """
    Функция сбора статистики размеров файлов по папке.
    Возвращает словарь с непустыми значениями
    """

    thresholds = {10 ** x : 0 for x in range(1, 6)}
    thresholds[0] = 0

    for item in os.walk(top=base_dir):
        files = item[2]
        if files:
            folder = item[0]
            for file in files:
                size = os.stat(os.path.join(folder, file)).st_size

                for key in sorted(thresholds.keys()):
                    if size > key:
                        continue
                    else:
                        thresholds[key] += 1
                        break

    return {threshold: count for threshold, count in sorted(thresholds.items()) if count}


if __name__ == '__main__':
    base_dir = 'some_data'
    print(show_stats(base_dir=base_dir))
