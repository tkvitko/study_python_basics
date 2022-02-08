import os
import shutil


def merge_folders(base_dir_name: str, merging_dir_name: str):
    """
    Функия для мержа папок в одну
    :param base_dir_name: имя  папки, внутри которой работаем
    :param merging_dir_name: имя папки, которую ищем и мержим
    :return: None
    """

    for root, folders, files in os.walk(top=base_dir_name):
        if root.endswith(merging_dir_name) and root != os.path.join(base_dir_name, merging_dir_name):
            sub_folder = folders[0]
            src = os.path.join(root, sub_folder)
            dst = os.path.join(base_dir_name, merging_dir_name, sub_folder)
            try:
                shutil.copytree(src=src,
                                dst=dst)
            except FileExistsError as e:
                print(f'{e.filename} already exists, spipping...')
            except Exception as e:
                print(f'{e.__class__.__name__} - {e} FATALITY')


if __name__ == '__main__':
    base_dir = 'my_project'
    folder_to_copy = 'templates'
    merge_folders(base_dir_name=base_dir,
                  merging_dir_name=folder_to_copy)
