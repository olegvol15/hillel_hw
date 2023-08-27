list1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 9,2, 132, 45, 23, 934]


counts = {}
for num in list1:
    counts[num] = list2.count(num)

print("Number\tNumber of appearences")
for num, count in counts.items():
    print(f"{num}\t{count}")