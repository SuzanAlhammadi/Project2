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


