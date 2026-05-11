def check(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
num = int(input("Enter a number: "))
result = check(num)
print(result)