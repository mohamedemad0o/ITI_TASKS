from helping import ascending , descending

x = input("please enter count of numbers : ")
x= int(x)
lista = []
for i in range(x):
    n=input("please enter your num: ")
    lista.append(n)

print(ascending(lista))
print(descending(lista))
