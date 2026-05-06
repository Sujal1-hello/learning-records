# Problem 1: Even or Odd
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

# Problem 2: Sum
total = 0

for i in range(1, 101):
    total += i

print("Total sum:", total)

# Problem 3: Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
