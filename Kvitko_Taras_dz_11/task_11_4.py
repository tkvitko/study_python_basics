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
    print(storage)
    print(storage.units_list)
    print(office)
    print(office_2)

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

    print(storage)
    print(office)
    print(office_2)
    storage.add(1)
