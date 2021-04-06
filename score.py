score=input('Enter Score:')
try:
    sc=float(score)
except:
    sc=2
if sc>1.0:
    print('Score should be between 0.0 and 1.0')
elif sc < 0:
    print('Score must be between 0.0 and 1.0')
else:
    if sc < 0.6:
        print('F')
    elif sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
