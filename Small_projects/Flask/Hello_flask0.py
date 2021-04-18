from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input('Enter word for vowel search:')
    found = []
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)

    for vowel in found:
        return vowel


app.run()
