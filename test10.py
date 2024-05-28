username = "ugopulo"
password = "12345"

username1 = input("Enter your username:")
password1 = input("Enter your password:")
if username == username1 and password == password1:
  print("Hello user")
elif username == username1 and password != password1:
    print("worng passworld")
elif username != username1 and password != password1:
    print("invalit user")
elif username != username1 and password == password1:
    print("worng username")
else:
    print("Stystem Error!")
