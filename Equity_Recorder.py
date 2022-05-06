#pylint:disable=E0602
#A program that records user input labelling it as either Assets , Liabilities, or Equity.

import time
def global_things():
    time.sleep(0.5)
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
    #global Capital List
    global Current_C_list
    Current_C_list=[]
    global Current_C_Value_List
    Current_C_Value_List=[]
    #global variables
    global user_choice

def user_choices():
    print('What do you choose to Record?')
    time.sleep(1.5)
    user_choice=input('a for assets, l for liabilities, and c for Capital:')
    if user_choice=='a':
        asset_type=input("'F' for fixed, 'C' for current, 'I' for intangible")
        if asset_type=='C':
            current_asset_record()
        elif asset_type=='F':
            fixed_asset_record()
        elif asset_type=='I':
            intangible_asset_record()
        else:
            print('Sorry, that is an invalid syntax.')
            time.sleep(0.5)
            user_choices()
    else:
        recording(user_choice)

#asks for specific information regarding the user_choice part
def choice_handle(user_choice):
	recording(user_choice)

def intangible_asset_record():
    print('When recording, do not use spaces, rather, use underscores')
    time.sleep(0.5)
    print('Examples: notes payable should be notes_payable')
    time.sleep(0.5)
    print('As much as possible, capitalize the first letter.')
    time.sleep(0.5)
    print('When adding records, always first write on paper to avoid loss.')
    time.sleep(0.5)
    print('If you do not have a paper, you may also restart the program.')
    time.sleep(0.5)

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
        assetvalue = input()
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
    print('When recording, do not use spaces, rather, use underscores')
    time.sleep(0.5)
    print('Examples: notes payable should be notes_payable')
    time.sleep(0.5)
    print('As much as possible, capitalize the first letter.')
    time.sleep(0.5)
    print('When adding records, always first write on paper to avoid loss.')
    time.sleep(0.5)
    print('If you do not have a paper, you may also restart the program.')
    time.sleep(0.5)
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
        assetvalue = input()
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
    print('When recording, do not use spaces, rather, use underscores')
    time.sleep(0.5)
    print('Examples: notes payable should be notes_payable')
    time.sleep(0.5)
    print('As much as possible, capitalize the first letter.')
    time.sleep(0.5)
    print('When adding records, always first write on paper to avoid loss.')
    time.sleep(0.5)
    print('If you do not have a paper, you may also restart the program.')
    time.sleep(0.5)
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
        assetvalue = input()
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
            liabilityvalue = input()
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
            capitalvalue = input()
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
        print('ony a or b or c. Try again')
        time.sleep(0.5)
        user_choices()

def Retry_parameter():
    time.sleep(0.5)
    again=input('Would you like to record again? [y,n]: ')
    if again=='y':
        user_choices()
    elif again=='n':
        print('Your values have been saved')
        print('Current Assets:', Current_A_list)
        print('Value', Current_A_Value_List)
        print('Fixed Assets:', Fixed_A_list)
        print('Value', Fixed_A_Value_List)
        print('Intangible Assets:', Current_A_list)
        print('Value', intangible_A_Value_List)
        print('Liabilities:', Current_L_list)
        print('Value', Current_L_Value_List)
        print('Capital:', Current_C_list)
        print('Value', Current_C_Value_List)


global_things()
user_choices()   

	