choice =input("Enter a choice (+,-,*,/) : ")
num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))
if choice == "+":
    result = num1+num2
    print(result)
elif choice == "-":
    result = num1-num2
    print(result)
elif choice == "*":
     result = num1*num2
     print(result)
elif choice == "/":
    result = num1/num2
    print(result)
else:
    print("choice is not a valid choice")