# Python_In_Action
This is repository whose goal is to record equity and earning income. 
Currently a ice breaker for times when nothing is happening.

### Updates
Date: 05/06/2022
1. Cleaner and better code for reading.
2. Made specific variables global such as
  
`global assets list`
`global Current_A_list`
`Current_A_list=[]`
`global Current_A_Value_List`
`Current_A_Value_List=[]`
`global Fixed_A_list`
`Fixed_A_list=[]`
`global Fixed_A_Value_List`
`Fixed_A_Value_List=[]`
`global intangible_A_list`
`intangible_A_list=[]`
`global intangible_A_Value_List`
`intangible_A_Value_List=[]`
`global Current_L_list`
`Current_L_list=[]`
`global Current_L_Value_List`
`Current_L_Value_List=[]`
`global Current_C_list`
`Current_C_list=[]`
`global Current_C_Value_List`
`Current_C_Value_List=[]`
`global user_choice`

3. Splitted the code of the intangible, fixed, and current assets so that I can work on them independently. 
4. Finally prints all of the assets.

### Update
05/13/2022
1. Added more functionality.
2. Now checks whether the values you have entered follows the accounting equation.
3. New lists and variables namely `revenue_list`,`revenue_value_list`,`expense_list`,`expense_value_list`,`withdrawal`, and `withdrawal_value`.
4. Renamed `user_choices()` to `start_program()`
5. Copied and pasted the codes for expense, revenue, and withdrawals:
`    n = int(input("How many withdrawal entries incurred?: "))

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
        recording(user_choice)`
 It uses that format now.
 6. If the credit and debit side are not equal, it will notify the user and will also display the inequality.
