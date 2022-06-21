#this file in side bank package
#call module
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc1= Account()
cus1_acc1.open_account(cus1.name,'Saving','752-963-4522',500)

print('**** Open bank account detail ****')
print(cus1.cus_info())
print(cus1_acc1.display_balance())
#print(cus1.cus_info())