warehouse = {
    "Брус": {"quantity": 160, "price": 790.00, "min_quantity": 80},
    "Доска": {"quantity": 240, "price": 560.00, "min_quantity": 120},
    "ОСБ": {"quantity": 9, "price": 1270.00, "min_quantity": 15},
    "Лак": {"quantity": 27, "price": 440.00, "min_quantity": 20},
    "Фанерный лист": {"quantity": 18, "price": 1580.00, "min_quantity": 22},
}

# Выводим шапку таблицы склада
print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)
print()
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 70)

# Переменные для итогов
total_sum = 0
critical_positions = []
top_material = ""
top_cost = 0

# Проходим по всем материалам на складе
for stock_name, stock_data in warehouse.items():
    qty_value = stock_data["quantity"]
    price_value = stock_data["price"]
    minimum_qty = stock_data["min_quantity"]
    stock_cost = qty_value * price_value

    total_sum += stock_cost

    # Ищем самый дорогой материал по общей стоимости
    if stock_cost > top_cost:
        top_cost = stock_cost
        top_material = stock_name

    status_mark = ""
    # Проверяем, не стал ли остаток критическим
    if qty_value < minimum_qty:
        status_mark = "  CRITICAL"
        critical_positions.append(f"{stock_name}: {qty_value} < {minimum_qty}")

    print(
        f"{stock_name} | {qty_value} | {price_value:.2f} | "
        f"{minimum_qty} | {stock_cost:.2f}{status_mark}"
    )

print("=" * 70)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_sum:.2f} руб")
print(
    f"Самый дорогой: {top_material} "
    f"({top_cost:.2f} руб)"
)
print()
print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_positions)}):")

if critical_positions:
    for stock_name in critical_positions:
        print(f"- {stock_name}")
else:
    print("Нет критических остатков")

print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")

# Задаём, что будем выдавать со склада
material_to_issue = "Доска"
amount_to_issue = 60

if material_to_issue in warehouse:
    current_stock = warehouse[material_to_issue]["quantity"]

    if current_stock >= amount_to_issue:
        warehouse[material_to_issue]["quantity"] -= amount_to_issue
        print(f"Выдано {amount_to_issue} единиц: '{material_to_issue}'")
        print(
            f"Остаток: {current_stock} -> "
            f"{warehouse[material_to_issue]['quantity']}"
        )
    else:
        print("Недостаточно материала на складе")
else:
    print("Материал не найден")
