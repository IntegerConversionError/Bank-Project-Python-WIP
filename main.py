#    W O R K   I N   P R O G R E S S 
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

databaseName = "database.txt"



#used to create database text file if it doesn't exist
def initDatabase():
   f = open(databaseName, "a+")
   f.close()
 
 
def updateBalance(name, newBalance, database):
   for i in range(len(database)):
       if database[i].get('name') == name:
           temp = {'balance': newBalance}
           database[i].update(temp)
 
 
def savetoDatabase(name, pin, address, balance):
   f = open(databaseName, "a")
   f.write(name + ", " + pin + ", " + address + ", " + balance + "\n")
   f.close()
 
 
def getDatabaseContents():
   f = open(databaseName, "r")
   contents = []
 
   for l in f.readlines():
 
       l = l.strip("\n")
 
       name, pin, address, balance = l.split(", ")
 
       contents.append({
           'name': name,
           'pin': pin,
           'address': address,
           'balance': balance
       })
 
       f.close()
       return contents
 
 
def main():
    initDatabase()
    database = getDatabaseContents()
 
    choice = input(
       "Type 'newuser' to create an account, 'login' to log in to an existing account, or 'delete' to delete your account: "
   )
 
    if choice == "newuser":
 
        name = input("Please enter your full name: ")
        pin = int(input("Please enter your PIN number: "))
        address = input("Please enter your home address: ")
        balance = int(input("Please enter your bank balance: "))
        savetoDatabase(name, str(pin), address, str(balance))
        print("New Data Saved to Database")
 
    elif choice == "login":
        userName = input("Please enter your full name: ")
        userPin = input("Please enter your 4 digit PIN: ")
       
        for i in range(len(database)):
           
            if database[i].get('name') == userName:
                if database[i].get('pin') == userPin:
                    print("Logged In!")
                    accountBalance = int(database[i].get('balance'))
                    print("Your balance is:", "$", accountBalance)
 
                    userChoice = input(
                       "Enter 'withdraw' to withdraw from your account or 'deposit' to deposit to your account: "
                    )
                    if userChoice == "withdraw":
                        withdrawAmount = int(input("How much would you like to withdraw?: "))
                        newBalance = accountBalance - withdrawAmount
                        print(database)
                        updateBalance(userName, newBalance, database)
                        print(database)
                        print("$", withdrawAmount," withdrawn from your account. Your new balance is: ",newBalance)
                        
                    elif userChoice == "deposit":
                        depositAmount = int(input("How much would you like to deposit?"))
                        newBalance = accountBalance + depositAmount
                        print("$", depositAmount," deposited into your account. Your new balance is: ",accountBalance)
                        updateBalance(name, newBalance, database)
    elif choice == "delete":
        userName = input("Please enter your full name: ")
        userPin = input("Please enter your 4 digit PIN: ")
        userAddress = input("Please enter your home address: ")
        userBalance = input("Please enter your bank balance: ")
 
        infile = "database.txt"
        outfile = "database.txt"
 
        delete_list = [userName, userPin, userAddress, userBalance]
        fin = open(infile)
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
               line = line.replace(word, "")
            fout.write(line)
        fin.close()
        fout.close()
        print("Account Successfully Deleted")
esad = 1
while esad == 1:
    main()
 


