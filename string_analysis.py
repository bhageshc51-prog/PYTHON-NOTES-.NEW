word = "machinelearning"

frequency = {}

for char in word:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

print(frequency)
