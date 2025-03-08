bugs = ("Ошибка 1 — High",
        "Ошибка 2 — Low",
        "Ошибка 3 — Medium",
        "Ошибка 4 — High",
        "Ошибка 5 — Low")

def bug_filter(bugs):
    def validation_for_input():
        while True:
            priority = input("Введите приоритет для поиска (High, Medium, Low): ")
            if priority in {"High", "Medium", "Low"}:
                return priority
            print("Введите корректный приоритет бага из предложенных.")

    status = validation_for_input()
    new_list = [bug for bug in bugs if status in bug]
    return new_list

filtered_bugs = bug_filter(bugs)
print("Найденные баги:", filtered_bugs)