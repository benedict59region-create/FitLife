# Норма воды в милилитрах на один килограмм веса
WATER_ML_PER_KG = 30

# Объем милилитров в одном литре
WATER_ML_PER_L = 1000

print("Добро пожаловать в фитнес-трекер FitLife!")

# Запрашиваем данные пользователя
user_name = input("Укажите Ваше имя ")

while True:
    user_age = input("Укажите Ваш возраст ")
    try:
        user_age = int(user_age)
        if 1 <= user_age <= 120:
            break
        else:
            print(
                 f"Введенное значение вне допустимого диапазона."
                 f" Введите значение от 1 до 120",
                 )
    except ValueError:
            print("Введите целое число, например, 25")

while True:
    user_weight = input("Укажите Ваш вес в килограммах, например, 79.4 ")
    try:
        user_weight = float(user_weight)
        if 5.0 <= user_weight <= 250.0:
            break
        else:
            print(
                 f"Введенное значение вне допустимого диапазона."
                 f" Введите значение от 5.0 до 250.0",
                 )
    except ValueError:
            print("Введите корректное число, например, 79.4")

while True:
    user_height = input("Укажите Ваш рост в метрах, например, 1.85 ")
    try:
        user_height = float(user_height)
        if 0.5 <= user_height <= 2.5:
            break
        else:
            print(
                 f"Введенное значение вне допустимого диапазона."
                 f" Введите значение от 0.5 до 2.5",
                 )
    except ValueError:
            print("Введите корректное число, например, 1.85")

# Информируем пользователя, что успешно записали данные для расчета
print("Ваши данные приняты - готовим расчет...")

# Делаем user_name с заглавной
user_name = user_name.title()

# Рассчитываем ИМТ
bmi = user_weight / (user_height ** 2)

# Рассчитываем норму воды в день и переводим в литры
water_l = user_weight * WATER_ML_PER_KG / WATER_ML_PER_L

# Выводим пользователю результат
print("_" * 50)
print(f"{user_name}, Ваш индекс массы тела равен {round(bmi, 1)}.")
print(
    f"Рекомендуемый ежедневный объем потребления воды "
    f"составляет {round(water_l, 1)} л.",
)
print("_" * 50)
print("Благодарим за использование сервиса FitLife. Будьте здоровы!")
