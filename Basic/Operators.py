num = 7
if num > 5 and num < 10:
    print(f"{num} is between 5 and 10.")
else:
    print(f"{num} is not between 5 and 10.")

num = 120
if num < 0 or num > 100:
    print(f"{num} is either less than 0 or greater than 100.")
else:
    print(f"{num} is between 0 and 100.")

num = 5
if not num == 0:
    print(f"{num} is not equal to 0.")      # is a string literal that allows for embedding expressions
else:
    print(f"{num} is equal to 0.")
