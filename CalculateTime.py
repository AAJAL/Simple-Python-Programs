#This program receives seconds from the user a calculates the number of minutes from those seconds

seconds = eval(input("Enter the number of seconds in integer form: "))

minutes = seconds // 60
remainingSeconds = seconds % 60
print(f"{seconds} seconds is {minutes} minutes and {remainingSeconds} seconds")