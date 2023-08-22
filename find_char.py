string = input("Enter a string: ")
char = input("Enter a character: ")

positions = ""
index = 0

while index < len(string):
    found_index = string.find(char, index)
    if found_index == -1:
        break
    positions += str(found_index)
    index = found_index + 1
    if index < len(string):
        positions += ", "

if positions:
    print("Character '{}' found at positions: {}".format(char, positions))
else:
    print("Character '{}' not found in the string.".format(char))
