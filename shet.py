username = input("enter user name: ")
password = input ("Enter password: ")
correct_user = "user 153"
correct_pass = "pass 456"
if username == correct_user and password == correct_pass:
    print("authentication")
else:
    print("error")