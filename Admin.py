from User import Bank


class Admin:
    def __init__(self) -> None:
        pass

    def loan_amount(self):
        return Bank.loan_given

    def bank_amount(self):
        return Bank.bank_balance

    def check_user(self):
        return Bank.users

    def loan_action(self, status):
        if status == 0:
            Bank.loan_status = False
        else:
            Bank.loan_status = True
        return Bank.loan_status

    def loan(self):
        return Bank.loan_status

    def delete_account(self, account_number):
        for user in Bank.users:
            if user == account_number:
                del Bank.users[user]
                return f"Account #{account_number} has been deleted."
        return "Account not found."
