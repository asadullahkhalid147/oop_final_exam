from user import User
from admin import Admin

give_loan= True
users= []

admins = [Admin('khalid','000')]

def create_account():
    email = input('email: ')



    password = input('password:')
    user = User(email,password)

    users.append(user)
    print('account created.')

def user_menu(user):
    while True:
        print(' \n user menu:')
        print('1.deposit')

        print('2.withdraw ')
        print('3.transfer')
        print('4. check balance ')
        print('5.take loan ')

        print('6.transaction history')
        print('7.logout')
        key = input(' enter:')


        if key=='1':
            amount= int(input('enter:'))
            user.deposit(amount)
            print(f'{amount} deposited.')


        elif key=='2':
            amount = int(input('enter:'))
            user.withdraw(amount)


        elif key=='3':
            transfer_email= input('email:')
            recipient= next((u for u in users if u.email==transfer_email), None)
            
            if recipient:
                amount = int(input('amount: '))
                user.transfer(recipient, amount)
                print(f'{amount} transferred.')
            else:
                print('not found.')
        elif key=='4':
            balance = user.check_balance()
            print(f'balance:{balance}')


        elif key =='5':
            user.take_loan()

        elif key=='6':
            history= user.check_transaction_history()
            print('transaction jistory:')
            for transaction in history:
                print(transaction)


        elif key== '7':
            break
        else:
            print("try again.")


def admin_menu(admin):
    while True:
        print('\n admin menu: ')
        print("1 total balance")

        print('2.total laon')

        print('3.on off loan feature')
        print('4.logout')

        key = input('enter:')

        if key =='1':
            balance = admin.total_balance(users)

            print(f'balance:{balance}')


        elif key== '2':
            loan = admin.total_loan(users)

            print(f'loan:{loan}')

        elif key == '3':
            ready = input(" write yes or no: ").lower()== 'yes'

            admin.loan_feature(ready)


        elif key== '4':
            break
        else:
            print('invalid')


def main():
    while True:
        print('\n Banking Management System: ')
        print('1.Create account')

        print('2. User login')
        print('3. Admin login')
        print('4. Exit')

        key= input(' enter choice: ')

        if key=='1':
            create_account()


        elif key=='2':
            email=input('email: ')
            password=input('password: ')
            user=next((u for u in users if u.email==email and u.password==password),None)
            if user:
                user_menu(user)
            else:
                print(' invalid .')


        elif key =='3':
            email= input(' email: ')
            password=input('password: ')
            admin =next((a for a in admins if a.email==email and a.password==password),None)
            if admin:
                admin_menu(admin)
            else:
                print(' invalid .')


        elif key=='4':
            print('the end')
            break
        else:
            print('invalid.')


if __name__== '__main__':
    main()
