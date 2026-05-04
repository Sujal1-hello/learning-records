num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
op = input("Enter operation:")

if op == "+":
    result = num1 + num2
    print("Result", result)
    
elif op == "-":
    result = num1 - num2
    print("Result", result)

elif op == "*":
    result = num1 * num2
    print("Result", result)

elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result", result)
    else:
         print("Cannot divide by zero")

else:
    print("invalid operation")