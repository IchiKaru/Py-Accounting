#pylint:disable=E0602
#A program that records user input labelling it as either Assets , Liabilities, or Equity.

import time
time.sleep(0.5)

#Basic Printing To the User
print('----------------------------------------------------------')
print('Welcome. This program is a work in progress and may have')
print('a lot of issues. For any problems, simply raise an issue')
print('at the github page where you got this program.')
print('----------------------------------------------------------')
print('')
print("The basic accounting equation is: Total Assets = Liabilities + Owner's Capital_Value - Withdrawals + Revenues - Expenses")
print('Fixed, intangible, and current assets are found under ASSETS. Expenses, revenues, and Withdrawals are under CAPITAL/EQUITY')
print('Keep this in mind when using the program')
print('')

time.sleep(1)
def variables():
#global assets list
    global Current_Assets
    Current_Assets=[]
    global Current_Assets_Value
    Current_Assets_Value=[]
    global Fixed_Assets
    Fixed_Assets=[]
    global Fixed_Assets_Value
    Fixed_Assets_Value=[]
    global Intangible_Assets
    Intangible_Assets=[]
    global Intangible_Assets_Value
    Intangible_Assets_Value=[]
    #global liability list
    global Current_Liabilities
    Current_Liabilities=[]
    global Current_Liabilities_Amount
    Current_Liabilities_Amount=[]
    #global Capital_Value (or equity depending on your region) List
    global Capital_Entry
    Capital_Entry=[]
    global Capital_Value
    Capital_Value=[]
    #extended global variables
    global Revenues
    Revenues=[]
    global Revenue_Quantity
    Revenue_Quantity=[]
    global Expenditures
    Expenditures=[]
    global Expenditure_Cost
    Expenditure_Cost=[]
    global Withdrawal
    Withdrawal=[]
    global Withdrawal_value
    Withdrawal_value=[]
    #global variables
    global user_choice

def start_program():
    print('What do you choose to Record?')
    time.sleep(1.5)
    user_choice = input("Enter 'Assets', 'Liabilities', or 'Capital':")
    print('-'*20)
    time.sleep(0.5)
    print('Follow all instructions carefully. If there are any irregularities, visit https://github.com/04raymond/Py-Accounting.')

    if user_choice == 'Assets':
        asset_type = input("What type of assets is it? 'F' for fixed, 'C' for current, 'I' for intangible:")
        if asset_type == 'C':
            current_asset_record()
        elif asset_type == 'F':
            fixed_asset_record()
        elif asset_type =='I':
            intangible_asset_record()
        else:
            print('Sorry, that is an invalid syntax.')
            time.sleep(0.5)
            start_program()
    elif user_choice == 'Capital':
        capital_type = input("'R' for revenue and 'E' for expenses. If none, enter [n]:")
        if capital_type == 'R':
            revenue_record()
        elif capital_type == 'E':
            expense_record()
        else:
            recording(user_choice)
    else:
        recording(user_choice)

#asks for specific information regarding the user_choice part
def choice_handle(user_choice):
	recording(user_choice)

def Withdrawal_record():
    n = int(input("How many Withdrawal entries incurred?: "))

    print("\n")
    for i in range(0, n):
        print("Enter the expenses incurred", i, )
        withdraw = input()
        Withdrawal.append(withdraw)
    print("You have entered ", Withdrawal)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the expense value for ", i, )
        withdrawn = eval(input())
        Withdrawal_value.append(withdrawn)
    print("You have entered ", Expenditure_Cost)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Withdrawal)
    print('You have entered the following asset value:',Withdrawal_value)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)    

def expense_record():
    n = int(input("How many expense entries incurred?: "))

    print("\n")
    for i in range(0, n):
        print("Enter the expenses incurred", i, )
        expense = input()
        Expenditures.append(expense)
    print("You have entered ", Expenditures)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the expense value for ", i, )
        expensevalue = eval(input())
        Expenditure_Cost.append(expensevalue)
    print("You have entered ", Expenditure_Cost)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Expenditures)
    print('You have entered the following asset value:',Expenditure_Cost)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)    
def revenue_record():
    n = int(input("How many revenue entries?: "))

    print("\n")
    for i in range(0, n):
        print("Enter the revenue/transaction name incurred", i, )
        revenue = input()
        Revenues.append(revenue)
    print("You have entered ", Revenues)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        revenuevalue = eval(input())
        Revenue_Quantity.append(revenuevalue)
    print("You have entered ", Revenue_Quantity)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Revenues)
    print('You have entered the following asset value:',Revenue_Quantity)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)
def intangible_asset_record():
    n = int(input("How many asset account titles?: "))

    print("\n")
    for i in range(0, n):
        print("Enter the asset", i, )
        asset = input()
        Intangible_Assets.append(asset)
    print("You have entered ", Intangible_Assets)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        Intangible_Assets_Value.append(assetvalue)
    print("You have entered ", Intangible_Assets_Value)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Intangible_Assets)
    print('You have entered the following asset value:',Intangible_Assets_Value)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)

def current_asset_record():
    n = int(input("How many asset account titles?: "))
    print("\n")
    for i in range(0, n):
        print("Enter the asset", i, )
        asset = input()
        Current_Assets.append(asset)
    print("You have entered ", Current_Assets)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        Current_Assets_Value.append(assetvalue)
    print("You have entered ", Current_Assets_Value)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Current_Assets)
    print('You have entered the following asset value:',Current_Assets_Value)
    time.sleep(1)
    #user confirmation
    user_confirmation = input('is the following information correct?[y,n]:')
    if user_confirmation == 'y':
        Retry_parameter()
    elif user_confirmation == 'n':
        time.sleep(0.5)
        recording(user_choice)
def fixed_asset_record():
    n = int(input("How many asset account titles?: "))
    

    print("\n")
    for i in range(0, n):
        print("Enter the asset", i, )
        asset = input()
        Fixed_Assets.append(asset)
    print("You have entered ", Fixed_Assets)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        Fixed_Assets_Value.append(assetvalue)
    print("You have entered ", Fixed_Assets_Value)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Fixed_Assets)
    print('You have entered the following asset value:',Fixed_Assets_Value)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)

def recording(user_choice):
    if user_choice=='Liabilities':
        n = int(input("How many liability account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the liability", i, )
            liability = input()
            Current_Liabilities.append(liability)
        print("You have entered ", Current_Liabilities)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the asset value for ", i, )
            liabilityvalue = eval(input())  
            Current_Liabilities_Amount.append(liabilityvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',Current_Liabilities)
        print('You have entered the following liability values(s)',Current_Liabilities_Amount)
        time.sleep(1)
        #user confirmation
        user_confirmation=input('is the following information correct?[y,n]:')
        if user_confirmation=='y':
            Retry_parameter()
        elif user_confirmation=='n':
            time.sleep(0.5)
            recording(user_choice)
    elif user_choice=='Capital_Value':
        n = int(input("How many Capital_Value account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the Capital_Value Account Title", i, )
            capital = input()
            Capital_Entry.append(capital)
        print("You have entered ", Capital_Entry)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the Capital_Value value for ", i, )
            capitalvalue = eval(input())
            Capital_Value.append(capitalvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',Capital_Entry)
        print('You have entered the following capital values(s)',Capital_Value)
        time.sleep(0.5)
        #user confirmation
        user_confirmation=input('is the following information correct?[y,n]:')
        if user_confirmation=='y':
            Retry_parameter()
        elif user_confirmation=='n':
            time.sleep(0.5)
            recording(user_choice)
    else:
        print("Only 'l' or 'c' . Try again")
        time.sleep(0.5)
        start_program()

def Retry_parameter():
    time.sleep(0.5)
    again=input('Would you like to record again? [y,n]: ')
    if again=='y':
        start_program()
    elif again=='n':
        print('The values you have recorded are now stored on RAM. To avoid loss, do not quit the application.')
        print('Capital_Value:', Capital_Entry)
        print('Total Capital_Value:', sum(Capital_Value))
        print('-'*20)
        for a, b in zip(Current_Assets, Current_Assets_Value):
            print(a, b)  
        print('-'*20)
        for a, b in zip(Fixed_Assets, Fixed_Assets_Value):
            print(a, b)
        print('-'*20)
        for a, b in zip(Intangible_Assets, Intangible_Assets_Value):
            print(a, b)
        print('-'*20)
        for a, b in zip(Current_Liabilities, Current_Liabilities_Amount):
            print(a, b)
        print('-'*20)
        for a, b in zip(Capital_Entry, Capital_Value):
            print(a, b)
        print('-'*20)

variables()
start_program()

check=input('Would you like to check for imbalances in both credit side and debit side? [y,n]:')
if check=='y':
    if sum(Current_Assets_Value)+sum(Fixed_Assets_Value)+sum(Intangible_Assets_Value)==sum(Current_Liabilities_Amount)+sum(Capital_Value)+sum(Revenue_Quantity)-sum(Expenditure_Cost)-sum(Withdrawal_value):
        time.sleep(0.5)
        print('OK')
    else:
        time.sleep(0.5)
        print('The inputted values are not equal.')
        if sum(Current_Assets_Value)+sum(Fixed_Assets_Value)+sum(Intangible_Assets_Value)>sum(Current_Liabilities_Amount)+sum(Capital_Value)+sum(Revenue_Quantity)-sum(Expenditure_Cost)-sum(Withdrawal_value):
            print('The debit side is higher then the credit side.')
            time.sleep(1)
            print('The debit side is', sum(Current_Assets_Value)+sum(Fixed_Assets_Value)+sum(Intangible_Assets_Value),'and the credit side is', sum(Current_Liabilities_Amount)+sum(Capital_Value)+sum(Revenue_Quantity)-sum(Expenditure_Cost)-sum(Withdrawal_value))
            seeif=input('Would you like to fix the errors? [y,n]:')
            if seeif=='y':
                start_program()
            elif seeif=='n':
                print('ok.')
        if sum(Current_Assets_Value)+sum(Fixed_Assets_Value)+sum(Intangible_Assets_Value)<sum(Current_Liabilities_Amount)+sum(Capital_Value)+sum(Revenue_Quantity)-sum(Expenditure_Cost)-sum(Withdrawal_value):
            print('The credit side is higher than the debit side.')
            time.sleep(1)
            print('The debit side is', sum(Current_Assets_Value)+sum(Fixed_Assets_Value)+sum(Intangible_Assets_Value),'and the credit side is', sum(Current_Liabilities_Amount)+sum(Capital_Value)+sum(Revenue_Quantity)-sum(Expenditure_Cost)-sum(Withdrawal_value))
            seeif=input('Would you like to fix the errors? [y,n]:')
            if seeif=='y':
                start_program()
            elif seeif=='n':
                print('ok.')
else:
    print("Your recorded values are now gone. Sorry, this is a work in progress. Hahaha!") 
	
