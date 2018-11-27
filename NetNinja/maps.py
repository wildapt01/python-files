from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# with for loop
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

# with map()
print(list(map(jumble, words)))

# with comprehension
print([jumble(word) for word in words])
