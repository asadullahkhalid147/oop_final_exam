class Admin:
    def __init__(self,email,password):
        self.email=email
        self.password=password


    def total_balance(self,users):
        total_balance=sum(user.balance for user in users)
        return total_balance


    def total_loan(self,users):
        total_loan=sum(user.loan for user in users)
        return total_loan




    def loan_feature(self,ready):
        global give_loan
        give_loan=ready

        if give_loan:
            print("loan feature on.")
        else:
            print("loan feature  off.")