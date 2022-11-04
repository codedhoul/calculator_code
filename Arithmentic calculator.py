arithmetic = dict()

choice = None

while choice != "0":
    print(
               '''
               Arithmetic Operations

               0-Exit
               1-Addition
               2-Subration
               3-Multiplication
               4-division
               5-Exponetial
               ''')
    choice = input("choice: ")
    print(choice)

    if choice == "0":
        print("you can now click on the close button")
        break

    elif choice == "1":
        x = float(input("Enter the first Number:"))
        y = float(input("Enter the second number:"))
        print("the sum is ", x + y)

    elif choice == "2":
        x = float(input("Enter the first Number:"))
        y = float(input("Enter the second number:"))
        print("the sum is ", x - y)

    elif choice == "3":
        x = float(input("Enter the first Number:"))
        y = float(input("Enter the second number:"))
        print("the sum is ", x * y)

    elif choice == "4":
        x = float(input("Enter the first Number:"))
        y = float(input("Enter the second number:"))
        print("the division is ", x / y, "\n OR")
        print("the division is ", int(x // y) , "reminder", int(x % y))
        

    elif choice== "5":
        x = float(input("Enter the first Number:"))
        y = float(input("Enter the second number:"))
        print("the sum is ", x ** y)
    else:
        print("INVALID INPUT.PLEASE CHECK OPTION AND TRY AGAIN")

