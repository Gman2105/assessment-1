hundred_dollor_bill = 100 #This is the variable called hundred dollar bill which is assigned to a value of 100
fifty_dollar_bill = 50 #This is the variable called fifty dollar bill which is assigned to a value of 50
twenty_dollar_bill  = 20 # This is a twenty dollar bill whcih is assigned to avalue of 20 
ten_dollar_bill = 10 # This is a ten dollar bill, whcih is assigned to a value of 10 
five_dollar_bill = 5 # This is a five dollar bill whcih is assigned to a value of 5 
one_dollar_bill = 1 # This is a one dollar bill which is assigned to a value of 1 
quarter = 0.25 #This is a warter coin whcih is assigned to a value of 0.25
dime = 0.10 # This is a dime coin which value is assigned to a value of 0.10
nickel = 0.05 # This is a nickle coin which value is assigned to 0.05
penny = 0.01 # This is a penny coin which value is assigned to 0.01 

item_cost = float(input("Enter the total price: $ ")) # This variable is called item _cost. It allows the user to input the total price of the product purchased, so the program can calculate the change.
moneygiven = float(input("Enter how much money given: $ ")) # This variable is called moneygiven. It allows the user to input the ammount of money given to the cashier, so that the program can calculate the change.
moneyback = moneygiven - item_cost # This line of code allows the program to calculate the change of the ammount given and recieved. 

hundreddmb = int(moneyback / hundred_dollor_bill) # This line of code assigns to the variable fifty dmb. Which stands for fifty dollar money back.
hundrednewbalance = moneyback - hundreddmb * hundred_dollor_bill 

fiftydmb = int(hundrednewbalance / fifty_dollar_bill) # This line of code assigns to the variable fifty dmb. Which stands for fifty dollar money back.
fiftydnewbalance = hundrednewbalance - fiftydmb * fifty_dollar_bill  

twentydmb = int(fiftydnewbalance / twenty_dollar_bill) # This line of code assigns to the variable fifty dmb. Which stands for fifty dollar money back.
twentydnewbalance = fiftydnewbalance-twentydmb*twenty_dollar_bill  

tendmb = int(twentydnewbalance / ten_dollar_bill) # This line of code has the ten dollar money back variable. This allows the twenty new balance divided by the ten dollars bill variable.
tendnewbalance = twentydnewbalance-tendmb*ten_dollar_bill  

fivedmb = int(tendnewbalance / five_dollar_bill) # This line of code is the five dollar back balance, which is the integer of the ten new balance divided by the five dollar bill variable value. 
fivednewbalance = tendnewbalance-fivedmb*five_dollar_bill  

onedmb = int(fivednewbalance / one_dollar_bill) #This is one dollar back balance, this allows the program to calculate the balance of one dollar. 
onednewbalance = fivednewbalance-onedmb*one_dollar_bill  

print (hundreddmb, "$ 100 Bill") # This line of code prints out the ammount of hundred dollar we need.
print (fiftydmb,"$ 50 Bill") # This line of code prints out the ammount of fifty dollar we need. 
print (twentydmb,"$ 20 Bill") # This line of code prints out the ammount of ten dollar we need. 
print (tendmb,"$ 10 Bill") # This line of code prints out the ammount of ten dollar we need. 
print (fivedmb,"$ 5 Bill") # # This line of code prints out the ammount of five dollar we need. 
print (onedmb,"$ 1 Bill") # This line of code prints out the ammount of one dollar we need. 

moneybacknew = moneyback-int(moneyback) # This is the new variable which is money back new and which calculates the decimals of the money

quarter_money_back = int(moneybacknew / quarter) # This variable allows the program to calculate, the ammount of quarters needed. 
partialtotal = moneybacknew - quarter_money_back * quarter # This variable is the first partial total and calculate the partial ammount of money remaining. 

dimes_money_back = int(partialtotal / dime) # This variable calculates the dime money back, by dividing the integer of the partial total by dime
dpartialtotal = partialtotal - dimes_money_back * dime # This line of code contains the partial total - the ammount of dimes needed. 

nickel_money_back = int(dpartialtotal / nickel) # This line of code calculate the integer of the dime partial total and divide it by the value of a nickle 
npartialtotal = dpartialtotal - nickel_money_back * nickel # This line of code contains the clauclations of the n partial total 

penny_money_back = int(npartialtotal / penny) + int(round((0.99),1))  # This line of code calculates the integer of the nickle partial total and divides it by the value of penny 
penny_partial_total = npartialtotal - penny_money_back * penny # This line of code calculate the penny partial total 

print(quarter_money_back, 'quarters' ) # This line of code prints out how much of quarter money is needed. 
print(dimes_money_back,'dime') # This line of code prints out how much of dime money is needed. 
print(nickel_money_back,'nickels') # # This line of code prints out how much of nickel money is needed. 
print(penny_money_back, 'pennys') # This line of code prints out how much of penny money is needed.