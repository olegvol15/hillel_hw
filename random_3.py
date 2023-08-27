import random

numbers = [random.randint(1, 100) for _ in range(15)]
print("Generated list: ", numbers)

odd_sum = sum(num for num in numbers if num % 2 != 0)
even_sum = sum(num for num in numbers if num % 2 == 0)

if odd_sum > even_sum:
    print("Yes")
else:
    print("No")
