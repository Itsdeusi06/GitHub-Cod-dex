class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
   
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("Sorry, you don't have enough funds.")
            return 0

    def display_balance(self):
        print(self.balance)


customer = BankAccount("John", "Doe", "12345", "Savings", "54321", 500)
customer.deposit(250)  # This should print: "You've deposited $250. Your new balance is $750."
customer.withdraw(100) # This should print: "You've withdrawn $100. Your new balance is $650."
customer.display_balance()  # This should print: "Your current balance is $650."