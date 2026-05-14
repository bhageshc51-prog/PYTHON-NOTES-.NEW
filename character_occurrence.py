data = "database"

result = {}

for i in data:
    result[i] = result.get(i, 0) + 1

print(result)
