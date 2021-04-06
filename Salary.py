hrs = input("Enter Hours:")
h = float(hrs)
if h<=40:
    print(h*10.5)
else:
    over40=h-40
    over40=over40*(10.5*1.5)
    forty=40*10.5
    print(over40+forty)
