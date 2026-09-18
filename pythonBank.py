class pythonBank:
    def __init__(self, customer_name, current_balance, min_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.min_balance = min_balance
        self.account_number = account_number
        self.routing_number = routing_number

    def deposit(self):
        self.current_balance += self.min_balance
        self.min_balance = 0

    def withdraw(self):
        if self. current_balance > self.min_balance:
            self.current_balance -= self.min_balance
        else:
            print("You cannot withdraw money")


    def print_customer_information(self):
        print(self.customer_name)
        print(self.current_balance)
        print(self.min_balance)
        print(self.account_number)

    def get_routing_number(self):
        return self.routing_number






