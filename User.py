class Bank:
    loan_given = 0
    bank_balance = 0
    users = {}
    loan_status = True
    current = None

    def login(self, acc):
        Bank.current = acc


class BankAccount:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type


class User(BankAccount):
    account_number = 10000

    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)

        self.balance = 0
        self.transactions = []
        self.loan_taken = 0

        self.account_number = User.account_number
        User.account_number += 1

        Bank.users[self.account_number] = self

    def __repr__(self):
        return f'{self.account_number, self.name, self.email, self.balance, self.address, self.account_type, self.transactions, self.loan_taken}'

    def deposit(self, amount):
        Bank.users[Bank.current].balance += amount
        Bank.bank_balance += amount

        Bank.users[Bank.current].transactions.append(f'Deposit: +{amount}')
        return f'Deposit: +{amount}'

    def withdraw(self, amount):
        if amount > Bank.users[Bank.current].balance:
            return "Withdrawal amount exceeded"
        else:
            Bank.users[Bank.current].balance -= amount

            Bank.bank_balance -= amount

            Bank.users[Bank.current].transactions.append(
                f'Withdrawal: -{amount}')
            return f'Withdrawn: -{amount}'

    def check_balance(self):
        return f'Available Balance: {Bank.users[Bank.current].balance}'

    def view_transactions(self):
        return Bank.users[Bank.current].transactions

    def take_loan(self, loan_amount):
        if not Bank.loan_status:
            return 'Loan status is turned off. You can not take any loan.'
        else:
            if Bank.users[Bank.current].loan_taken < 2:
                Bank.users[Bank.current].balance += loan_amount
                Bank.users[Bank.current].loan_taken += 1

                Bank.bank_balance -= loan_amount
                Bank.loan_given += loan_amount

                Bank.users[Bank.current].transactions.append(
                    f'Loan Taken: +{loan_amount}')
                return f'Loan Taken: {loan_amount}'
            else:
                return "You have already taken the maximum number of loans"

    def transfer(self, amount, target_account):
        if Bank.users.get(target_account) == None:
            return 'Account does not exist'
        else:
            if Bank.users[Bank.current].balance >= amount:
                Bank.users[Bank.current].balance -= amount
                Bank.users[target_account].balance += amount

                Bank.users[Bank.current].transactions.append(
                    f'transfered {amount} to: #{target_account}')
                Bank.users[target_account].transactions.append(
                    f'received {amount} from: #{Bank.current}')

                return f'Transferred {amount} to Account #{target_account}'
            else:
                return "Insufficient funds for transfer"
