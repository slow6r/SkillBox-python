a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

# Добавляем элементы списка b в основной список a и считаем количество 5
a.extend(b)
count_five = a.count(5)
print(f"Количество цифр 5 при первом объединении: {count_five}")

# Удаляем все элементы 5 из списка a
a = [x for x in a if x != 5]

# Добавляем элементы списка c и считаем количество 3
a.extend(c)
count_three = a.count(3)
print(f"Количество цифр 3 при втором объединении: {count_three}")

# Итоговый список
print("Итоговый список:", a)
