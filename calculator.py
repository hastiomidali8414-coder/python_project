print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation: ")

if choice == "1":
    print("Result: ", num1 + num2)

elif choice == "2":
    print("Result: ", num1 - num2)

elif choice == "3":
    print("Result: ", num1 * num2)

elif choice == "4":
    if num2  != 0:
        print("Result: ", num2 / num1)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid choice!")
