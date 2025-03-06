# Задача "Основы"
def basic_info():
    name = input("Введите ваше имя: ")
    profession = input("Введите вашу профессию: ")
    years_experience = input("Сколько лет вы работаете в QA? ")
    question = input("Дай определение термину Переменная: ").lower()

    keyword1 = "ссылка"
    keyword2 = "объект"

    if keyword1 in question and keyword2 in question:
        print(
            f"Привет, {name}! Вы работаете как {profession} уже {years_experience} лет, "
            "и за это время вы не забыли, что такое переменная!"
        )
    else:
        print(
            f"Привет, {name}! Вы работаете как {profession} уже {years_experience} лет, "
            "но вам стоит повторить, что такое переменная."
        )

basic_info()