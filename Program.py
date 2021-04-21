def CheckPassword():
    password = input("Enter Password: ") #Asks for the user's input.
    print()
    badchar = False #Variable which stores whether the user's input is valid or invalid.
    length = len(password) #Stores the password length in a variable.
    symbols = ['!', '$', '%', '-', '*', '(', ')', '^', '_', '=', '+'] #Variable which holds valid symbols.
    for i in range(length):
        if not password[i].isupper() and not password[i].islower() and not password[i].isnumeric() and password[i] not in symbols: #Validates whether the password meets the program's requirements.
            badchar = True #The password does not meet requirements and is considered invalid .

    score = CalculatePoints(password)
    if badchar: #checking whether the password is valid or invalid which is stored in the variable badchar.
        print('Invalid Characters\nSCORE:', score) #Outputs on screen on the occasion of a password being invalid along with the points scored.
    else:
        print('Password Accepted!\nSCORE:', score) #Ouputs on screen when a password is valid along with the points scored.

    print()


def CalculatePoints(password): #Subroutine which will store the requirements for point scoring.
    score = len(password)
    numbers = False
    lower = False
    upper = False
    symbol = False
    AllowedChr = ['!', '$', '%', '-', '*', '(', ')', '^', '_', '=', '+'] #Variable which stores the allowed symbols.

    for i in range(len(password)): #Scans the password given
        if password[i].isupper: #Examines whether the password contains of uppercase letters.
            upper = True #Uppercase letters present.
            score = score + 5 ´#Adds 5 points onto the Score variable as uppercase letters were present.
    for i in range(len(password)): #Checks the password given
        if password[i].islower: #Inspects whether the password contains of lowercase letters.
            lower = True #When lowercase letters present.
            score = score + 5 #Adds 5 points onto the score variable.
    for i in range(len(password)): #Checks the password given
        if password[i].isnumeric: #Checks whether the password contains of numeric characters.
            numbers = True #When numeric characters present
            score = score + 5 #Adds 5 points onto the Score variable.
    for i in range(len(password)): #Inspects the password given.
        if password[i] in AllowedChr: #Investigates whether the password includes any symbols stored in the AllowedChr variable.
            symbol = True #When valid symbols found.
            score = score + 5 #Adds 5 points onto the score variable.

    if upper and lower and numbers and symbol: #Checks whether there is uppercase, lowercase or symbols present.
        score = score + 10 #Adds 10 points onto the score variable.

    if upper and lower and not numbers and not symbol:
        score = score - 5
    if symbol and not lower and not numbers and not upper:
        score = score - 5
    if numbers and not lower and not upper and not symbol:
        score = score - 5

    runscounted = 0
    run1 = 'qwertyuiop'
    run2 = 'asdfghjkl'
    run3 = 'zxcvbnm'
    for i in range(len(password) - 2):
        if password[i:i + 3] in run1 or password[i:i + 3] in run2 or password[i:i + 3] in run3:
            runscounted = runscounted + 1

    runscount = runscounted * 5
    score = score - runscount
    return score



# Menu
def Menu():
    option = input('\nChoose an Option from Below:\n[1] Check Password\n[2] Generate Password\n[3] Quit\n\n')
    print()
    while option != '3':
        if option == '1':
          CheckPassword()  

        elif option == '2':
            print('Generating Password . . .')

        else:
            print("Invalid Option!")

        option = input('\nChoose an Option from Below:\n[1] Check Password\n[2] Generate Password\n[3] Quit\n')
        print()

    print('Closing Program . . .')



# Main Program
Menu()
