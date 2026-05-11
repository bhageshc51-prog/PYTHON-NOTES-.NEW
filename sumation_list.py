def summation(my_list):
    sum = 0
    for i in my_list:
        sum = sum + i
    return sum
my_list = [1, 2, 3, 4, 5]
x = summation(my_list)
print(x)