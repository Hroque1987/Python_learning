phrase = 'Don´t panic!'
plist = list(phrase)

for i in range(4):#pops the last four elements of the list (and discards them)
    plist.pop()

plist.pop(0)

plist.remove('´')

plist.extend([plist.pop(),plist.pop()]) # pops p and a and then extends with a and p

plist.insert(2,plist.pop(3)) #insert on index 2 the pop value of index 3

new_phrase = ''.join(plist) # turns back a list to a string

print(plist)
print(new_phrase)
