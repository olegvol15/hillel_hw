sentence = input("Enter the sentence at least with 3 words: ")
words = sentence.split(" ")
non_empty_words = []
for word in words:
    if word != "":
        non_empty_words.append(word)


non_empty_words.sort()

print("index\tword")

for index in range(len(non_empty_words)):
    print(f"{index + 1}\t{non_empty_words[index]}")


print(f"Number of words: {len(non_empty_words)}")