def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"The result of {x} divided by {y} is {result}")
    finally:
        print("Execution completed.")


divide(10, 2)    
divide(10, 0)    
