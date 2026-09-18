from pythonBank import pythonBank
from savingsAccount import savingsAccount
from checkingAccount import checkingAccount


#Instances
#savings
Jack = savingsAccount("Jack", 100000, 1000, "SA39049", "RT293820", 0.05)
print("Jack's Account")
Jack.print_customer_information()

Jack.interest()

print()

Jan = savingsAccount("Jan", 12830, 1000, "SA39569", "RT394820", 0.02)
print("Jan's Account")
Jan.print_customer_information()

Jan.interest()

print(Jan.interest_rate)


#checking
Gary = checkingAccount("Gary", 50000, 1500, 'C4930', 'RT37384', 2 )
print("Gary's Account")
Gary.print_customer_information()

Gary.transfer(500)

print()

Bryce = checkingAccount("Bryce", 100000, 2000, "C93840", "RT3947203", 5)
print("Bryce's Account")
Bryce.print_customer_information()

Bryce.transfer(180000)
print()


