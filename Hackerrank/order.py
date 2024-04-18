from collections import Counter

def calculate_earned_money(shoe_sizes, customers):
    shoe_inventory = Counter(shoe_sizes)
    total_earned = 0
    
    for customer in customers:
        size, price = customer
        if shoe_inventory[size] > 0:
            total_earned += price
            shoe_inventory[size] -= 1
    
    return total_earned

# Take user inputs
shoe_count = int(input())
shoe_sizes = list(map(int, input().split()))
customer_count = int(input())
customers = []
for _ in range(customer_count):
    size, price = map(int, input().split())
    customers.append((size, price))

# Calculate and print the earned money
earned_money = calculate_earned_money(shoe_sizes, customers)
print(earned_money)