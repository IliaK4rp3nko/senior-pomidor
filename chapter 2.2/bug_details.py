bug_report = {
    "ID": 1,
    "name": "Ошибка при входе в приложение",
    "status": "Ожидает проверки"
}
def change_status(bug_report: dict, new_status: str) -> dict:
    bug_report["status"] = new_status
    return bug_report

print(bug_report)
print(change_status(bug_report, "Готово"))