largest = None
smallest = None
while True:
    num=input('Enter value: ')
    if num == 'done':
        break
    try:
        num=int(num)
    except:
        print('Wrong Number')
        continue
    if largest is None:
        largest=num
        smallest=num
    elif num > largest:
        largest=num
    elif num < smallest:
        smallest=num

print('Largest',largest)
print('Smallest',smallest)
print('All DONE')
