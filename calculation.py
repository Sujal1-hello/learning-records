num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation: +  -  *  /")
op = input("Enter operation: ")

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2

else:
    result = "Invalid operation"

print("Result:", result)