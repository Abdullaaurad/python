import math

def pageCount(n, p):
    from_front = p // 2
    if n % 2 == 0:
        from_back = (n - p + 1) // 2
    else:
        from_back = (n - p) // 2
    return min(from_front, from_back)

print(pageCount(6,2))