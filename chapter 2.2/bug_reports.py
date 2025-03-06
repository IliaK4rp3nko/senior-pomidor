bugs = ("Ошибка 1 — High",
        "Ошибка 2 — Low",
        "Ошибка 3 — Medium",
        "Ошибка 4 — High",
        "Ошибка 5 — Low",)

def add_bug(bugs, bug):
    bugs.append(bug)
    return bugs

def delete_bug(bugs):
    for bug in bugs:
        if "Low" in bug:
            bugs.remove(bug)
        return bugs

def sorting_bugs(bugs):
    priority_order = ["high","medium","low"]
    sorted_bugs = []
    for priority in priority_order:
        for bug in bugs:
            if bug == priority:
                sorted_bugs.append(bug)
    return priority_order

