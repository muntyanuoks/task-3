# Исходный прайс материалов
price_table = {
    "Брус": 780.0,
    "Доска": 540.0,
    "ОСБ": 1250.0,
    "Утеплитель": 980.0,
    "Саморезы": 220.0,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_table}")

# Добавляем две новые позиции
price_table["Лак"] = 430.0
price_table["Фанерный лист"] = 1600.0

print()
print("После добавления двух материалов:")
print(price_table)

# Изменяем цену утеплителя на 10%
price_table["Утеплитель"] = price_table["Утеплитель"] * 1.10

# Подготавливаем словарь с форматированием
display_prices = {name: f"{price:.2f}" for name, price in price_table.items()}

print()
print("После изменения цены утеплителя на 10%:")
print(display_prices)

# Удаляем одну позицию из прайса
removed_value = price_table.pop("Саморезы")
display_prices = {name: f"{price:.2f}" for name, price in price_table.items()}

print()
print(f"Удалённый материал: Саморезы ({removed_value:.2f} руб.)")
print(f"Итоговый словарь: {display_prices}")

# Вычисляем среднюю цену
average_value = sum(price_table.values()) / len(price_table)

print(f"Средняя цена материалов: {average_value:.2f} руб.")