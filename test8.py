x = 10
answer = int(input("Guess the number between 1 to 15 :"))
if answer > x:
    print("Guess smaller number")
elif answer < x:
    print("Guess bigger number")
elif answer == x:
    print("You Won")