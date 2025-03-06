
# Задача "Переменные"
def user_profile():
    name = "ilia"
    proffesion = "MQA"
    tool = "proxyman"
    name = input("Введите ваше имя: ")
    profession = input("Введите вашу профессию: ")
    tool = input("Введите ваш любимый инструмент для тестирования: ")
    if not tool:
        print("Инструмент не указан. Попробуйте снова!")
    else:
        print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")

user_profile()