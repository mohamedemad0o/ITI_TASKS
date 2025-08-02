import json
from helping import validation
import csv

with open("users_data.csv", "r", newline="", encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    mails=[]
    for row in reader:
        #print(row[3])
        mails.append(row[3])

#filter
clean_mails = filter(validation,mails)
clean_mails=list(clean_mails)
print(clean_mails)

#mappping
collection_of_domains = map(lambda m: m.split("@")[1],clean_mails)
collection_of_domains = list(collection_of_domains)

#set
for i in range(len(collection_of_domains)):
    collection_of_domains[i]=collection_of_domains[i].lower()
clean_domains = set(collection_of_domains)
clean_domains = list(clean_domains)

print(collection_of_domains)
print(clean_domains)

users_data={
    "valid_mails" : clean_mails,
    "all of domains": collection_of_domains,
    "clean domains": clean_domains
}
for key, value in users_data.items():
    print(f"{key}: {list(value)}")

with open("users_data.json", "w", newline="", encoding='utf-8-sig') as data:
    json.dump(users_data, data, indent= 4)


