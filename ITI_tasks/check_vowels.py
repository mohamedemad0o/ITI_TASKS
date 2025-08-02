from helping import checkvowels


words = input("please enter your word: ")
words=words.lower()
if not words.isalpha():
    print("please enter words only ")
else:
    print(checkvowels(words))