from helping import validation

for i in range (5):
    mail=input("please enter your email : ")
    try:
        if validation(mail):
            print("hello")
            break
    except:
        print("enter a valid mail")

else:
    raise Exception("expected attack")






