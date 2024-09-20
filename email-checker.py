email = input("Enter your email: ")

if len(email) >= 6:
    if "@" in email and "." in email:
        if (email.count("@") == 1) and (email.count(".") == 1):
            if (email.index("@") < email.index(".")) and (email.index("@") != 0) and (email.index(".") > email.index("@")):
                if "gmail" in email:
                   if email.count("gmail") == 1:
                      if email.index("gmail") > email.index("@") and (email.index("gmail") < email.index(".")) and email.index("gmail") != 0:
                          print("Valid Gmail")
                      else:
                          print("Invalid Gmail 7")
                   else:
                       print("Invalid Email 6")
                else:
                    print("Invalid email 5")
            else:
                print("Invalid Email 4")
        else:
            print("Invalid email 3")
    else:
        print("Invalid email 2")
else:
    print(" Invalid email 1")
                         