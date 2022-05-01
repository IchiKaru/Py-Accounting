
#A program that records user input labelling it as either Assets , Liabilities, or Equity.

import time
time.sleep(3)
#asks the user what to record
user_choices()


def user_choices():
    print('What do you choose to Record?')
    time.sleep(1.5)
    user_choice=input('a for assets, l for liabilities, and c for Capital:')
    choice_handle(time, user_choice)
    
#asks for specific information regarding the user_choice part
def choice_handle(time, user_choice):
    A1_title_list=[]
    A1_Value_List=[]
    L1_title_list=[]
    L1_Value_List=[]
    C1_title_list=[]
    C1_Value_List=[]
    print('When recording, do not use spaces, rather, use underscores')
    time.sleep(0.7)
    print('Examples: notes payable should be notes_payable')
    time.sleep(0.7)
    print('As musch as possible, capitalize the first letter.')
    if user_choice=='a':
        print('When adding records, always first write on paper to avoid loss.')
        time.sleep(2)
        print('If you do not have a paper, you may aslo restart the program.')
        time.sleep(2)

        n = int(input("How many asset account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the asset", i, )
            asset = input()
            A1_title_list.append(asset)
        print("You have entered ", A1_title_list)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the asset value for ", i, )
            assetvalue = input()
            A1_Value_List.append(assetvalue)
        print("You have entered ", A1_title_list)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',A1_title_list)
        print('You have entered the following asset value:',A1_Value_List)
        time.sleep(1)
        y=1
        n=0
        time.sleep(0.5)
        #user confirmation
        user_confirmation=input('is the following information correct?:')
        if user_confirmation==n:
            Retry()
        elif user_confirmation==y:
            time.sleep(0.5)
            choice_handle(time, user_choice)
    elif user_choice=='l':
        print('When adding records, always first write on paper to avoid loss.')
        time.sleep(2.2)
        print('If you do not have a paper, you may aslo restart the program.')
        n = int(input("How many liability account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the liability", i, )
            liability = input()
            L1_title_list.append(liability)
        print("You have entered ", L1_title_list)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the asset value for ", i, )
            liabilityvalue = input()
            L1_Value_List.append(liabilityvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',L1_title_list)
        print('You have entered the following liability values(s)',L1_Value_List)
        time.sleep(1)
        y=1
        n=0
        time.sleep(0.5)
        #user confirmation
        user_confirmation=input('is the following information correct?[y,n]:')
        if user_confirmation==n:
            Retry()
        elif user_confirmation==y:
            time.sleep(0.5)
            choice_handle(time, user_choice)
    elif user_choice=='c':
        print('When adding records, always first write on paper to avoid loss.')
        time.sleep(2.2)
        print('If you do not have a paper, you may aslo restart the program.')
        n = int(input("How many Capital account titles?: "))

        print("\n")
        for i in range(0, n):
            print("Enter the Capital Account Title", i, )
            capital = input()
            C1_title_list.append(capital)
        print("You have entered ", C1_title_list)
        time.sleep(0.5)
        print("\n")
        for i in range(0, n):
            print("Enter the Capital value for ", i, )
            capitalvalue = input()
            C1_Value_List.append(capitalvalue)
        time.sleep(0.5)
        #shows what user have entered
        print('You have entered the following account title(s):',C1_title_list)
        print('You have entered the following capital values(s)',C1_Value_List)
        time.sleep(1)
        y=1
        n=0
        time.sleep(0.5)
        #user confirmation
        user_confirmation=input('is the following information correct?[y,n]:')
        if user_confirmation==n:
            Retry()
        elif user_confirmation==y:
            time.sleep(0.5)
            choice_handle(time, user_choice)
    else:
        print('ony a or b or c. Try again')
        time.sleep(0.3)
        user_choices()

#user confirmation
def Retry():
    time.sleep(2)
    again=input('Would you like to record again? [y,n]: ')
    if again=='y':
    	user_choices()
    if again=='n':
    	print('ok.')
    	