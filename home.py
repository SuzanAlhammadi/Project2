num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("Invalid operator")



if num1 > num2:
    print(num1, "greater than", num2)
elif num1 < num2:
    print(num1, "less than", num2)
else:
    print(num1, "equal to", num2)


if num1 > 0:
    print(num1, "is positive")
elif num1 < 0:
    print(num1, "is negative")
else:
    print(num1, "is zero")

if num2 > 0:
    print(num2, "is positive")
elif num2 < 0:
    print(num2, "is negative")
else:
    print(num2, "is zero")