class AccountHolder:

    def __init__(self, fname, mname, lname, account_type, balance):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.account_type = account_type
        self.balance = balance
        self.status = open

class Bank:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def openAccount(self, fname, mname, lname, account_type, balance):
        temp = AccountHolder(fname, mname, lname, account_type, balance)
        if balance >= 100:
            self.accounts.append(temp)
            print(f"Congratulations! Account created for {fname} {mname} {lname} with a balance of {balance}. Thank you for trusting us with your hard earned money. Here at {self.name}, we strive for greatness!")
        else:
            print("Account not created due to insufficient funds. Must have an initial balance of $100.")

    def showMembers(self):
        for accounts in self.accounts:
            print(f"{accounts.fname} {accounts.mname} {accounts.lname}")

    def transferFunds(self, account, amount):
    
def main():
    Big_Boy_Banking = Bank("Big Boy Banking LLC", "69420 Road St.")
    action = 1

    while action != 6:
        print(f"""What would you like to do at your friendly neighborhood {Big_Boy_Banking.name}?""")
        print("1. Create an account")
        print(f"2. Show a list of all {Big_Boy_Banking.name} account holders. ")
        print{f"3. Transfer funds. "}
        print("6. Exit Big Boy Banking.")

        action = int(input(">>>"))

        if (action == 1):

            fname = input("What is your first name? ")
            mname = input("What is your middle name? ")
            lname = input("What is your last name? ")
            account_type = input("What would you like to open? Checking or Savings? ")
            deposit = int(input("How much would you like to deposit? "))
            Big_Boy_Banking.openAccount(fname, mname, lname, account_type, deposit)

        elif (action == 2):
            Big_Boy_Banking.showMembers()

        elif (action == 3):
            Big_Boy_Banking.transferFunds()

        if (action == 6):
            print("See you soon. We'll miss you dearly while you're away...")
            break
        

main()