from equipment import Storage, Office
from equipment import Printer, Scanner, Copier
from equipment import NotEnoughEquipment

if __name__ == '__main__':
    office = Office('Офис 1')
    office_2 = Office('Офис 2')
    storage = Storage('Склад')

    printer_1 = Printer(model='Canon', is_colorful=True)
    printer_2 = Printer(model='Canon', is_colorful=False)
    printer_3 = Printer(model='Philips', is_colorful=True)
    copier = Copier(model='Sony', speed=1)
    scanner = Scanner(model='HP', resolution=(1280, 720))

    storage.add(printer_1)
    storage.add(printer_2)
    storage.add(printer_3)
    storage.add(scanner)
    print(f'Кратко о складе: {storage}')
    print(f'Список оборудования на складе: {storage.units_list}')
    print(f'Кратко об офисе: {office}')
    print(f'Кратко об офисе: {office_2}')
    print(f"Результат поиска: {storage.search_unit('Scanner', ('resolution', (1280, 720)))}")

    print('Результат итерирования по оборудованию склада')
    for unit in storage.iter_units():
        print(unit)

    print('4 попытки перемещений')
    try:
        storage.transit(office, printer_1)
    except NotEnoughEquipment as e:
        print(f'Перемещение невозможно: {e}')
    try:
        storage.transit(office, printer_3)
    except NotEnoughEquipment as e:
        print(f'Перемещение невозможно: {e}')
    try:
        storage.transit(office_2, scanner)
    except NotEnoughEquipment as e:
        print(f'Перемещение невозможно: {e}')
    try:
        storage.transit(office, copier)
    except NotEnoughEquipment as e:
        print(f'Перемещение невозможно: {e}')

    print(f'Кратко о складе: {storage}')
    print(f'Кратко об офисе: {office}')
    print(f'Кратко об офисе: {office_2}')
    print('Попытка добавить на склад не оборудование:')
    storage.add(1)
