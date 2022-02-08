import os


# Попытался написать собственный парсер yaml =)

def create_project_starter(config_file_name: str):
    """
    Функция для создания структуры папок и файлов в соответствии с файлом конфигурации.
    Файл должен иметь слудующую структуру:
    - каждая строка - отдельная папка или файл
    - файл отличается от папки наличием точки
    - количетво символов "пробел" перед названием папки или файла определяет его уровень вложенности
    - БУДЬТЕ ВНИМАТЕЛЬНЫ: не допускается ситуация, когда уровень вложенности текущего элемента больше
    уровня вложенности предыдущего элемента более, чем на 1

    :param config_file_name: имя yaml-файла с конфигурацией
    :return: None
    """

    with open(config_file_name) as f:
        path_items_list = []  # список для хранения элементов пути
        prev_level = -1  # стартовое значение предыдущей позиции

        while True:
            line = f.readline()
            if not line:
                break
            elif '.' in line:  # это файл
                line_type = 'file'
            else:  # это папка
                line_type = 'folder'

            line = line.replace('\n', '')
            level = line.count(' ')  # определяем глубину
            level_difference = level - prev_level  # разница в глубине относительно предыдущей записи

            for _ in range(1 - level_difference):
                path_items_list.pop()  # сокращаем список элементов на количество, рассчитанное по разнице в глубине
            path_items_list.append(line.strip())  # заносим в список текущий элемент
            prev_level = level  # обновляем уровень для следующей итерации

            if line_type == 'folder':
                # создание папки
                os.makedirs(os.path.join(*path_items_list), exist_ok=True)
            else:
                # создание файла
                if not os.path.exists(os.path.join(*path_items_list)):  # если файл еще не создан
                    with open(os.path.join(*path_items_list), 'w'):
                        pass


if __name__ == '__main__':
    config = 'config.yaml'
    create_project_starter(config_file_name=config)
