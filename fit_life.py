print("Добро пожаловать в фитнес-трекер FitLife!")

# Запрашиваем данные пользователя
user_name = input("Укажите Ваше имя ")
user_age = input("Укажите Ваш возраст ")
user_weight = input("Укажите Ваш вес в килограммах, например, 79.4 ")
user_height = input("Укажите, Ваш рост в метрах, например, 1.85 ")

# Информируем пользователя, что успешно записали данные для расчета
print("Ваши данные приняты - готовим расчет...")

# Записываем user_age как число. На текущем этапе не требуется
user_age = int(user_age)

# Делаем user_name с заглавной
user_name = user_name.title()

# Применяем плавающую точку к user_weight
float_user_weight = float(user_weight)

# Применяем плавающую точку к user_height
float_user_height = float(user_height)

# Рассчитываем ИМТ
bmi = float_user_weight / (float_user_height ** 2)

# Рассчитываем норму воды в день и переводим в литры
water_l = float_user_weight * 30 / 1000

# Выводим пользователю результат
print("_" * 50)
print(f"{user_name}, Ваш индекс массы тела равен {round(bmi, 1)}.")
print(
    f"Рекомендуемый ежедневный объем потребления воды "
    f"составляет {round(water_l, 1)} л.",
)
print("_" * 50)
print("Благодарим за использование сервиса FitLife. Будьте здоровы!")
