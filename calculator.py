income= float(input("What is your income?"))
rent= float(input("How much is your rent?"))
food= float(input("How much money do you spend on groceries?"))
subscription_total=0
for i in range(1,5):
    subscription= float(input("How much is subscription" "?" + str(i)))
    subscription_total+=subscription
    
expenses= float(input("What expenses do you already have?"))
expenses+=subscription_total
total= str(income-expenses)

print(str("Your income is "+ str(income)))
print(str("Your expenses are "+ str(expenses)))
print(str("Your remaining income is "+ str(total)))
