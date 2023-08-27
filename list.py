filtered_numbers = []

numbers = list(range(10, 251))

for num in numbers:
    if num % 20 != 0:
        filtered_numbers.append(num)

print(filtered_numbers)

