# Данные исполнителя
fio_student = "Мунтяну Оксана Александровна"
group_code = "52501"

# Описание объекта строительства
project_name = 'ТРЦ "Галерея"'
floors = 5
height = 35
is_residential = False
construction_year = 2010

# Переводим булево значение в текст
object_type = "Жилой" if is_residential else "Нежилой"

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {fio_student}")
print(f"Группа: {group_code}")
print()
print(f"Объект: {project_name}")
print(f"Этажность: {floors} этажей")
print(f"Высота: {height} м")
print(f"Тип: {object_type}")
print(f"Год постройки: {construction_year}")

# Адрес объекта:
# г. Санкт-Петербург, Лиговский проспект, д. 30А
# Причина выбора:
# крупный торговый центр в центре города, важный объект городской инфраструктуры
