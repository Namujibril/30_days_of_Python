# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        self.total_income = self.calculate_total_income()
        self.total_expense = self.calculate_total_expense()
        self.account_info = self.calculate_account_info()
        self.add_income = self.add_income()
        self.add_expense = self.add_expense()
        self.account_balance = self.calculate_account_balance()

    def calculate_total_income(self):
        return sum(self.incomes)

    def calculate_total_expense(self):
        return sum(self.expenses)

    def calculate_account_info(self):
        return f'Account info: {self.firstname} {self.lastname}'

    def add_income(self):
        return self.incomes

    def add_expense(self):
        return self.expenses

    def calculate_account_balance(self):
        return self.total_income - self.total_expense 
    