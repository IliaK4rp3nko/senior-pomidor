import pytest

class BankAccount:
    def __init__(self, owner: str, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount): # Добавляет сумму к балансу, если сумма положительная, иначе выбрасывает ValueError
        if amount < 0:
            raise ValueError("Введите корректную сумму.")
        else:
            self.__balance += amount
            return self.__balance
    
    def withdraw(self, amount): # Снимает сумму с баланса, если на счету достаточно средств, иначе выбрасывает ValueError
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете. Введите другую сумму.")
        else:
            self.__balance -= amount
            return self.__balance
    
    def get_balance(self): # Отдает баланс по счету
        return self.__balance


class SavingsAccount(BankAccount): # Класс для начисления процентной ставки
    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate  # Вычесляем процент
        self.deposit(interest)  # Добавляем к баллансу процент
        return self.get_balance()


class CheckingAccount(BankAccount):
    def withdraw(self, amount):  
        self._BankAccount__balance -= amount  # Получаем доступ к приватному атриуду
        # балланса родительского класса и списываем сумму с него
        return self.get_balance()


bank_account = SavingsAccount("Ilia", 0)
bank_account.deposit(500)
bank_account.withdraw(100)
bank_account.apply_interest()

def test_positive_balance():
    assert bank_account.get_balance() > 0
