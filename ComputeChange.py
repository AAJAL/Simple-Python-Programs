

def change(amount):
    #amount in cents
    remainingAmount = int(amount * 100)

    #Number of dollars
    numberOfDollars = remainingAmount // 100
    remainingAmount = remainingAmount % 100

    #Number of quarters
    numberOfQuarters = remainingAmount // 25
    remainingAmount = remainingAmount % 25

    #Number of dimes
    numberOfDimes = remainingAmount // 10
    remainingAmount = remainingAmount % 10

    #Number of nickels
    numberOfNickels = remainingAmount // 5
    remainingAmount = remainingAmount % 5

    #Number of pennies
    numberOfPennies = remainingAmount

    return str(numberOfDollars) + " dollars\n" + str(numberOfQuarters) + " quarters\n" + str(numberOfDimes) + " dimes\n" + \
    str(numberOfNickels) + " nickels\n" + str(numberOfPennies) + " pennies\n"


amount = eval(input("Enter an amount: "))
print(change(amount))