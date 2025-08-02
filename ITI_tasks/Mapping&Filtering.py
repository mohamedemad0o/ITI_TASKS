from helping import validation

mails = []
for i in range (5):
    mail = input("please enter your mail: ")
    mails.append(mail)

check_mail = filter(validation,mails)
check_mail=list(check_mail)
print(list(check_mail))

collection_of_domains = map(lambda m : m.split("@")[1] ,check_mail)
print(list(collection_of_domains))