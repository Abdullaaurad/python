def test(num):
    if num < 0 or num > 100:
        return (f"{num} is either less than 0 or greater than 100.")
    else:
        return (f"{num} is between 0 and 100.")

result = test(23)
print(result)
result = test(-1)
print(result)