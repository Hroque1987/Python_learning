def computepay(h,r):
    if h < 40:
        return h*r
    if h > 40:
        over40=h-40
        over40=over40*(r*1.5)
        forty=40*r
        return over40+forty
hrs = input("Enter Hours:")
r = input("Enter Rate:")
hrs = float(hrs)
r = float(r)
p = computepay(hrs,r)
print("Pay",p)
