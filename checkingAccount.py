from pythonBank import pythonBank

class checkingAccount(pythonBank):
    def __init__(self, customer_name, current_balance, min_balance, account_number, routing_number, transfer_limit):

        pythonBank.__init__(self, customer_name, current_balance, min_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
        self.transfer_count = 0



    def transfer(self, amount):

        if self.transfer_count >= self.transfer_limit:
            print("Transfer limit reached")

        elif amount > self.current_balance:
            print("Not enough money")

        else:
            self.current_balance -= amount
            self.transfer_count += 1
            print("Transfer successful")
            print("Amount Transferred:", amount)
            print("Current Balance:", self.current_balance)
            