# Входной номер дня недели
day_index = int(input("Введите номер дня недели: "))

# Подбираем название дня
if day_index == 1:
    day_label = "Понедельник"
elif day_index == 2:
    day_label = "Вторник"
elif day_index == 3:
    day_label = "Среда"
elif day_index == 4:
    day_label = "Четверг"
elif day_index == 5:
    day_label = "Пятница"
elif day_index == 6:
    day_label = "Суббота"
elif day_index == 7:
    day_label = "Воскресенье"
else:
    day_label = "Некорректный номер дня"

# Проверяем, рабочий это день или выходной
if 1 <= day_index <= 5:
    status_text = "Рабочий день"
    mode_value = "8:00 - начало смены"
elif day_index == 6 or day_index == 7:
    status_text = "Выходной"
    mode_value = "Отдых"
else:
    status_text = "Не определён"
    mode_value = "Проверьте номер дня"

print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {day_index}")
print(f"День недели: {day_label}")
print(f"Статус: {status_text}")
print(f"Режим: {mode_value}")
