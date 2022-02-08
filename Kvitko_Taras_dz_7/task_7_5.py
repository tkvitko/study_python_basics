import json
import os


def show_stats(base_dir: str):
    """
    Функция сбора статистики размеров файлов по папке.
    Записывает результат в файл <имя_папки>_summary.json
    """

    thresholds = {10 ** x: [0, set()] for x in range(1, 6)}
    thresholds[0] = [0, set()]

    for item in os.walk(top=base_dir):
        files = item[2]
        if files:
            folder = item[0]
            for file in files:
                size = os.stat(os.path.join(folder, file)).st_size
                extension = file.split('.')[-1]

                for key in sorted(thresholds.keys()):
                    if size > key:
                        continue
                    else:
                        thresholds[key][0] += 1
                        thresholds[key][1].add(extension)
                        break

    for k, v in thresholds.items():
        v[1] = list(v[1])
        thresholds[k] = tuple(v)

    result = {threshold: count for threshold, count in sorted(thresholds.items()) if count[0]}

    with open(f'{base_dir}_summary.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)


if __name__ == '__main__':
    base_dir = 'my'
    show_stats(base_dir=base_dir)
