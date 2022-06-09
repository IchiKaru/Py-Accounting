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
print("The basic accounting equation is: Total Assets = Liabilities + Owner's Capital - Withdrawals + Revenues - Expenses")
print('Fixed, intangible, and current assets are found under ASSETS. Expenses, revenues, and withdrawals are under CAPITAL/EQUITY')
print('Keep this in mind when using the program')
print('')

time.sleep(1)
def variables():
#global assets list
    global Current_A_list
    Current_A_list=[]
    global Current_A_Value_List
    Current_A_Value_List=[]
    global Fixed_A_list
    Fixed_A_list=[]
    global Fixed_A_Value_List
    Fixed_A_Value_List=[]
    global intangible_A_list
    intangible_A_list=[]
    global intangible_A_Value_List
    intangible_A_Value_List=[]
    #global liability list
    global Current_L_list
    Current_L_list=[]
    global Current_L_Value_List
    Current_L_Value_List=[]
    #global Capital (or equity depending on your region) List
    global Current_C_list
    Current_C_list=[]
    global Current_C_Value_List
    Current_C_Value_List=[]
    #extended global variables
    global revenue_list
    revenue_list=[]
    global revenue_value_list
    revenue_value_list=[]
    global expense_list
    expense_list=[]
    global expense_value_list
    expense_value_list=[]
    global withdrawal
    withdrawal=[]
    global withdrawal_value
    withdrawal_value=[]
    #global variables
    global user_choice

def start_program():
    print('What do you choose to Record?')
    time.sleep(1.5)
    user_choice=input('a for assets, l for liabilities, and c for Capital:')
    print('-'*20)
    time.sleep(0.5)
    print('Follow all instructions carefully. If there are any irregularities, visit https://github.com/IjiRay/Py-Accounting.')

    if user_choice=='a':
        asset_type=input("'F' for fixed, 'C' for current, 'I' for intangible:")
        if asset_type=='C':
            current_asset_record()
        elif asset_type=='F':
            fixed_asset_record()
        elif asset_type=='I':
            intangible_asset_record()
        else:
            print('Sorry, that is an invalid syntax.')
            time.sleep(0.5)
            start_program()
    elif user_choice=='c':
        capital_type=input("'R' for revenue and 'E' for expenses. If none, enter [n]:")
        if capital_type=='R':
            revenue_record()
        elif capital_type=='E':
            expense_record()
        else:
            recording(user_choice)
    else:
        recording(user_choice)

#asks for specific information regarding the user_choice part
def choice_handle(user_choice):
	recording(user_choice)

def withdrawal_record():
    n = int(input("How many withdrawal entries incurred?: "))

    print("\n")
    for i in range(0, n):
        print("Enter the expenses incurred", i, )
        withdraw = input()
        withdrawal.append(withdraw)
    print("You have entered ", withdrawal)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the expense value for ", i, )
        withdrawn = eval(input())
        withdrawal_value.append(withdrawn)
    print("You have entered ", expense_value_list)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',withdrawal)
    print('You have entered the following asset value:',withdrawal_value)
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
        expense_list.append(expense)
    print("You have entered ", expense_list)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the expense value for ", i, )
        expensevalue = eval(input())
        expense_value_list.append(expensevalue)
    print("You have entered ", expense_value_list)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',expense_list)
    print('You have entered the following asset value:',expense_value_list)
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
        revenue_list.append(revenue)
    print("You have entered ", revenue_list)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        revenuevalue = eval(input())
        revenue_value_list.append(revenuevalue)
    print("You have entered ", revenue_value_list)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',revenue_list)
    print('You have entered the following asset value:',revenue_value_list)
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
        intangible_A_list.append(asset)
    print("You have entered ", intangible_A_list)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        intangible_A_Value_List.append(assetvalue)
    print("You have entered ", intangible_A_Value_List)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',intangible_A_list)
    print('You have entered the following asset value:',intangible_A_Value_List)
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
        Current_A_list.append(asset)
    print("You have entered ", Current_A_list)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        Current_A_Value_List.append(assetvalue)
    print("You have entered ", Current_A_Value_List)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Current_A_list)
    print('You have entered the following asset value:',Current_A_Value_List)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)
def fixed_asset_record():
    n = int(input("How many asset account titles?: "))
    

    print("\n")
    for i in range(0, n):
        print("Enter the asset", i, )
        asset = input()
        Fixed_A_list.append(asset)
    print("You have entered ", Fixed_A_list)
    time.sleep(0.5)
    print("\n")
    for i in range(0, n):
        print("Enter the asset value for ", i, )
        assetvalue = eval(input())
        Fixed_A_Value_List.append(assetvalue)
    print("You have entered ", Fixed_A_Value_List)
    time.sleep(0.5)
    #shows what user have entered
    print('You have entered the following account title(s):',Fixed_A_list)
    print('You have entered the following asset value:',Fixed_A_Value_List)
    time.sleep(1)
    #user confirmation
    user_confirmation=input('is the following information correct?:')
    if user_confirmation=='y':
        Retry_parameter()
    elif user_confirmation=='n':
        time.sleep(0.5)
        recording(user_choice)

def recording(user_choice):
    if user_choice=='l':
        n = int(input("How many liability account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the liability", i, )
            liability = input()
            Current_L_list.append(liability)
        print("You have entered ", Current_L_list)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the asset value for ", i, )
            liabilityvalue = eval(input())  
            Current_L_Value_List.append(liabilityvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',Current_L_list)
        print('You have entered the following liability values(s)',Current_L_Value_List)
        time.sleep(1)
        #user confirmation
        user_confirmation=input('is the following information correct?[y,n]:')
        if user_confirmation=='y':
            Retry_parameter()
        elif user_confirmation=='n':
            time.sleep(0.5)
            recording(user_choice)
    elif user_choice=='c':
        n = int(input("How many Capital account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the Capital Account Title", i, )
            capital = input()
            Current_C_list.append(capital)
        print("You have entered ", Current_C_list)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the Capital value for ", i, )
            capitalvalue = eval(input())
            Current_C_Value_List.append(capitalvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',Current_C_list)
        print('You have entered the following capital values(s)',Current_C_Value_List)
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
        print('Current Assets:', Current_A_list)
        print('Total Current Asset Value', sum(Current_A_Value_List))
        print('-'*20)
        print('Fixed Assets:', Fixed_A_list)
        print('Total Fixed Asset Value:', sum(Fixed_A_Value_List))
        print('-'*20)
        print('Intangible Assets:', Current_A_list)
        print('Total Intangible Asset Value:', sum(intangible_A_Value_List))
        print('-'*20)
        print('Liabilities:', Current_L_list)
        print('Total Liabilities:', sum(Current_L_Value_List))
        print('-'*20)
        print('Capital:', Current_C_list)
        print('Total Capital:', sum(Current_C_Value_List))
	print('-'*20)
	
variables()
start_program()

check=input('Would you like to check for imbalances in both credit side and debit side? [y,n]:')
if check=='y':
    if sum(Current_A_Value_List)+sum(Fixed_A_Value_List)+sum(intangible_A_Value_List)==sum(Current_L_Value_List)+sum(Current_C_Value_List)+sum(revenue_value_list)-sum(expense_value_list)-sum(withdrawal_value):
        time.sleep(0.5)
        print('OK')
    else:
        time.sleep(0.5)
        print('The inputted values are not equal.')
        if sum(Current_A_Value_List)+sum(Fixed_A_Value_List)+sum(intangible_A_Value_List)>sum(Current_L_Value_List)+sum(Current_C_Value_List)+sum(revenue_value_list)-sum(expense_value_list)-sum(withdrawal_value):
            print('The debit side is higher then the credit side.')
            time.sleep(1)
            print('The debit side is', sum(Current_A_Value_List)+sum(Fixed_A_Value_List)+sum(intangible_A_Value_List),'and the credit side is', sum(Current_L_Value_List)+sum(Current_C_Value_List)+sum(revenue_value_list)-sum(expense_value_list)-sum(withdrawal_value))
            seeif=input('Would you like to fix the errors? [y,n]:')
            if seeif=='y':
                start_program()
            elif seeif=='n':
                print('ok.')
        if sum(Current_A_Value_List)+sum(Fixed_A_Value_List)+sum(intangible_A_Value_List)<sum(Current_L_Value_List)+sum(Current_C_Value_List)+sum(revenue_value_list)-sum(expense_value_list)-sum(withdrawal_value):
            print('The credit side is higher than the debit side.')
            time.sleep(1)
            print('The debit side is', sum(Current_A_Value_List)+sum(Fixed_A_Value_List)+sum(intangible_A_Value_List),'and the credit side is', sum(Current_L_Value_List)+sum(Current_C_Value_List)+sum(revenue_value_list)-sum(expense_value_list)-sum(withdrawal_value))
            seeif=input('Would you like to fix the errors? [y,n]:')
            if seeif=='y':
                start_program()
            elif seeif=='n':
                print('ok.')
else:
    print("Your recorded values are now gone. Sorry, this is a work in progress.") 
	
