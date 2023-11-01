from User import User
from Admin import Admin
from User import Bank


def main():
    while True:
        val = int(input("""
            Please select an option:
            1. Create account 
            2. Log in
            3. Admin
            4. Close 
            Option: """))

        if val == 1:
            name = input('Your name: ')
            email = input('Your email: ')
            address = input('Your address: ')
            type_val = int(input("""Your account type: 1. Savings
                    2. Current
                    Select account type: """))
            if type_val == 1:
                account_type = 'Savings'
            else:
                account_type = 'Current'

            account = User(name, email, address, account_type)

            if account != None:
                print(f"""Account created successfully
    Your {account_type} account number is #{account.account_number}
    You can login using your account number""")

        elif val == 2:
            num = int(input('Please enter your account number to login: #'))

            if Bank().users.get(num) == None:
                print('Account does not exist. Please create an account.')
            else:
                Bank().login(num)

                while True:
                    num2 = int(input("""
                    Please select an option:
                    1. Deposit 
                    2. Withdraw
                    3. Balance    
                    4. Transactions    
                    5. Loan    
                    6. Transfer    
                    7. Close 

                    Option: """))

                    if num2 == 1:
                        amount = int(input('Enter your deposit amount: '))
                        deposit = account.deposit(amount)
                        print(deposit)

                    if num2 == 2:
                        amount = int(input('Enter your withdraw amount: '))
                        withdraw = account.withdraw(amount)
                        print(withdraw)

                    if num2 == 3:
                        balance = account.check_balance()
                        print(balance)

                    if num2 == 4:
                        transactions = account.view_transactions()
                        print(transactions)

                    if num2 == 5:
                        amount = int(input('Enter your loan amount: '))
                        loan = account.take_loan(amount)
                        print(loan)

                    if num2 == 6:
                        amount = int(input('Enter your transfer amount: '))
                        acc1 = int(input('Enter your target account: #'))
                        transfer = account.transfer(amount, acc1)
                        print(transfer)

                    if num2 == 7:
                        break

        elif val == 3:
            num1 = int(
                input('To confirm you are an admin, enter your password (0000): '))
            if num1 == 0000:
                while True:
                    val2 = int(input("""
                Please select an option:
                1. Create an account 
                2. Delete an user
                3. Check all accounts    
                4. Check bank amount    
                5. Check bank loan    
                6. Loan status    
                7. Close 

                Option: """))

                    if val2 == 1:
                        name = input('Your name: ')
                        email = input('Your email: ')
                        address = input('Your address: ')
                        type_val = int(input("""Your account type: 1. Savings
                   2. Current
                   Select account type: """))
                        if type_val == 1:
                            account_type = 'Savings'
                        else:
                            account_type = 'Current'

                        account = User(name, email, address, account_type)

                        if account != None:
                            print(f"""Account created successfully
                Your {account_type} account number is {account.account_number}
                You can login using your account number""")

                    elif val2 == 2:
                        acc2 = int(input('Enter account number to delete: '))
                        print(Admin().delete_account(acc2))

                    elif val2 == 3:
                        print(Admin().check_user())

                    elif val2 == 4:
                        print(Admin().bank_amount())

                    elif val2 == 5:
                        print(Admin().loan_amount())

                    elif val2 == 6:
                        sts = Admin().loan()
                        if sts:
                            val3 = int(input("""Loan status is turned on
Press 0 to turn it off
"""))
                        else:
                            val3 = int(input("""Loan status is turned off
Press 1 to turn it on
"""))
                        Admin().loan_action(val3)

                    elif val2 == 7:
                        break

            else:
                print('You are not an admin')

        elif val == 4:
            break


if __name__ == '__main__':
    main()
