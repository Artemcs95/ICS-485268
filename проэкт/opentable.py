from prettytable import PrettyTable
from table import dt

x = PrettyTable()

x.field_names = ["Код товару", "Назва товару", "Місяць", "Середня ринкова ціна за місяць", "Роздрібна ціна, грн.", "Рівень зміни цін"]
for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )


def opentable():
    print('\nАналіз зміни рівня ринкових цін')
    print(x)
