def  calculator():
    print("Simple Calculator")
    print("Select your operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Power")
    print("7. Square Root") 
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice  in ['1', '2', '3', '4', '5', '6', '7']:
        if choice == '1':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             result = num1 + num2
             print(f"Result: {result}")
        elif choice == '2':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             result = num1 - num2
             print(f"Result: {result}")
        elif choice == '3':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             result = num1 * num2
             print(f"Result: {result}")
        elif choice == '4':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
             else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             result = num1 % num2
             print(f"Result: {result}")
        elif choice == '6':
            num1 = float(input("Enter first number: "))
            result = num1 ** 2
            print(f"Result: {result}")  
        elif choice == '7':
             num1 = int(input("Enter first number: "))
             if num1 >= 0:
                result = num1 ** 0.5
                print(f"Square Root of {num1} is: {result}")
             else:
                print("Error: Cannot calculate square root of a negative number.")
        elif choice == '8':
           print("Exiting the calculator. Goodbye!")
        else:
         print("Invalid choice. Please select a valid operation.")


if __name__=="__main__":
    calculator()
        
      
