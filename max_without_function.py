def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
p = maximum(5, 4, 9)
print("Maximum Number =", p)