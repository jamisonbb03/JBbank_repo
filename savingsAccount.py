from pythonBank import pythonBank

class savingsAccount(pythonBank):
    def __init__(self, customer_name, current_balance, min_balance, account_number, routing_number, interest_rate):
        pythonBank.__init__(self, customer_name, current_balance, min_balance, account_number, routing_number)


        self.interest_rate = interest_rate

    def interest(self):
            self.current_balance += self.current_balance * self.interest_rate