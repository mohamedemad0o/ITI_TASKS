def checkvowels(words):
    n=0
    l = ["a","e","i","o","u"]
    for i in words :
        if i in l:
            n+=1
    return n


def location(vocab):
    x = "i"
    for i in range(len(vocab)):
        if vocab[i] == x:
            return i
    return -1

def factorial(x):
    for i in range(1,x+1):
         for j in range(1,i+1):
            print (i*j)
    return

def mario(height):
    for i in range(height+1):
        print(" "*(height)+"*"*i)
        height-=1

def factoriallist(fact):
    l = []
    for i in range(1,fact+1):
        smallfact =[]
        for j in range(1,i+1):
            multiplication = i*j
            smallfact.append(multiplication)
        print(smallfact , end=" ")
    l.append(smallfact )
    print(l)

 # def validation(email):
 #     if '@' in email and '.' in email:
 #         username, domain = email.split('@')
 #         if username and domain:
 #             x,y=domain.split('.')
 #             if x and y:
 #                 return True
 #     else:
 #         return False

# import re
# def mailvalidation(mail):
#
#     pattern = r"^[a-zA-Z0-9@._-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$"
#     if re.match(pattern,mail):
#         return True
#     return False
import re
def validation(mail):
    pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, mail)

