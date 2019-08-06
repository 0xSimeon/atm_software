'''
Created on Jul 29, 2019

@author: Simicode
'''
def func1():
    print("Welcome to Fidelity Bank. Create an account with us, Today.")
    name = input('What is your name: ')
    pin = (input("Enter your PIN: "))
    if len(pin) > 4 :
        print("Incorrect Pin")
    if pin =
        
func1()
'''choice = 1
print("Press 1 to try again")
if choice == 1:
    func1()

exit()'''
        
print('You need to make an initial deposit to activate your account')
deposit = int(input('How much do you want to deposit? :'))
account_balance = str(deposit)
print('Your account balance is N'+ account_balance)

print('1.To Transfer \n.2.To Withdraw \n3.Deposit \n4.To recharge \n5.To check balance')
choice= int(input('What would you like to do?:  '))
if choice ==1:
    de_bank = input('enter the destination bank: ')
    acct_num = int(input('Type account number: '))
    if  acct_num > 10 or acct_num < 10:
        print("Invalid account number")
    t_amount = int(input('How much do you want to transfer? (account bal: '))
    if t_amount > account_balance:
        print('insufficient balance')
               
elif choice==2:                    
    account_type = input('Savings or Current')
    with_amt = int(input('Enter the withdrawal amount: '))
    if with_amt > account_balance:
        print('insufficient balance, please try again.')
elif choice==3:
    depo_amt = int(input('Enter the amount you want to deposit: '))
    if depo_amt <=499:
        print('The minimum deposit amount is N500')
elif choice==4:
    airtime_amt = int(input("Enter the amount of airtime you want to buy: "))
    if airtime_amt <50: 
        print('The minimum airtime purchase is N50')
elif choice ==5:
    print('Your account balance is : ',account_balance)
else:
    print("Incorrect bank details")