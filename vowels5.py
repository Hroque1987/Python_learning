def search_for_vowels (word:str) -> set:
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)



search_for_vowels ('gggg')
