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
            print(f"{accounts.fname} {accounts.mname} {accounts.lname}\'s account balance is {accounts.balance}'")

    def transferFunds(self, your_account, recipient_account, amount):
        for accounts in self.accounts:
            if accounts.fname == your_account:
                accounts.balance -= amount
                if accounts.balance < 0:
                    accounts.balance -= 35
        for accounts in self.accounts:
            if accounts.fname == recipient_account:
                accounts.balance += amount

    def withdrawFunds(self, account_to_withdraw, withdraw_amount):
        for accounts in self.accounts:
            if accounts.fname == account_to_withdraw:
                accounts.balance -= withdraw_amount
                if accounts.balance < 0:
                    accounts.balance -= 35
    
def main():
    Big_Boy_Banking = Bank("Big Boy Banking LLC", "69420 Road St.")
    action = 1

    while action != 6:
        print("""@@@@%/*****************************************************************************************/&@@@
@**************************************************************************************************/
***********************/%//(#***********************************************************************
*********************&        .******************************,,*************************************
******************,%@%.      ,.(*******                ****      ***********************************
***************& &             (********      ,***      ,**     ,***********************************
**************(   @@@&&@@@@#&(.@*******       ***       ******.********,.,**,,,,********************
**************(  @@#@@@@@@@#/#&(******.              ***       ****     **     .********************
*************& ,, %@@  ./@&,&#@&(*****      ***      ****     .**     .**.     *********************
************** &@&*@@@@&@@&@@(@@#****      .****      **      **      ***     **********************
**************&%(@@@@@@@@%*(@@%(****       ****       *      **,     ***     ,**********************
****************(%%%(/@@@@&&%%****..       ..        **       **            .***********************
************%%@@@@@@. %@@@@..@***************************.,***********,     ************************
*********#@@@%@@@@@@@  (*#/@  @@/(*******               ,*****     **     ,*************************
******%#@@@@@(/(&@@@@ * ##%@   @@%(*******      ***,      *****,      .*****************************
****#%@@@@((*%%,@. ,/ @%#@#@#/%@@&(******       ***       ******************************************
****/##&%/*% @*&#@ (&  *#   &@#@@#,*****.      ,,       ****      .    ***.      ***     ***********
***********&     @(,@@* *@@  ##&@#,*****      **      ****      ***.    .**,     **     .***********
***********/&(/@(    //  ,@(***//******      .***,      *      ****      *,     ***     ************
*************& .%@@@@@@(*(************       ****       *     ,***      **     ***     *************
***********& &%*,@, *  ,*/***********,      ***,       **,    ***     .**.            ,*************
**********@   @@,  @@. &***********,..............,*********.      ,*******   .*,     **************
********/  ,##.  @@%#***************************************************    ,**,    .***************
*********# *  /*********************************************************,        .***,**************
***********((**,,***********************************************************************************
*********************************************************BANKING****LLC*****************************
@***************************************************************************************************
@@#***********************************************************************************************&@\n""")
        print("WELCOME TO BIG BOY BANKING LLC ONLINE:")
        print(f"""What would you like to do at your friendly neighborhood {Big_Boy_Banking.name}?""")
        print("1. Create an account. ")
        print(f"2. Show a list of all {Big_Boy_Banking.name} account holders. ")
        print("3. Transfer funds. ")
        print("4. Withdraw funds. ")
        print("6. Exit Big Boy Banking. ")

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
            your_account = input("What is the first name for your account? ")
            recipient_account = input("Who do you want to transfer money to? ")
            amount = int(input("How much would you like to transfer? "))
            Big_Boy_Banking.transferFunds(your_account, recipient_account, amount)

        elif (action == 4):
            account_to_withdraw = input("What is the first name for your account? ")
            withdraw_amount = int(input("How much would you like to withdraw from your account? "))
            Big_Boy_Banking.withdrawFunds(account_to_withdraw, withdraw_amount)
            print(f"You withdrew ${withdraw_amount} from {account_to_withdraw}. ")

        if (action == 6):
            print("See you soon! We'll miss you dearly while you're away... Please comeback soon to Big Boy Banking LLC. Where your moneys safety is our top priority!")
            break
        

main()