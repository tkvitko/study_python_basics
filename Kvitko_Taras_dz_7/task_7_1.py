import os


def create_project_starter(project_structure: dict):
    """
    Функция создает структуру папок в соответствии с переданным словарем
    """
    for folder, sub_folders in project_structure.items():
        for sub_folder in sub_folders:
            os.makedirs(os.path.join(folder, sub_folder), exist_ok=True)


if __name__ == '__main__':
    project_name = 'my_project'

    structure = {
        project_name: [
            'settings',
            'mainapp',
            'adminapp',
            'authapp'
        ]
    }

    create_project_starter(project_structure=structure)
