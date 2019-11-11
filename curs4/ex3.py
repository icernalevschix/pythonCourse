a = input()
if a.isnumeric():
    print("I am integer")
elif a.isalpha():
    print("I am text")
else:
    print("I am text with numbers")