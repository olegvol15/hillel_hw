numbers = list(map(int, input("Enter your list: ").split()))

min_value = min(numbers)
max_value = max(numbers)

min_index = numbers.index(min_value)
max_index = numbers.index(max_value)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]


print("New list:", numbers)
