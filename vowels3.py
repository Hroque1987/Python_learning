vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide word for searching vowels:')
found = {}
for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 1
        else:
            found[letter] += 1

for i, k in sorted(found.items()):
    print(i , "was found", k, "times")
