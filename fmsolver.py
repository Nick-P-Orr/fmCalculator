a = 1
b = [1,2,3]


interest = input('Enter interest')
discount = input('Enter discount')

if interest == "" and discount == "":
    print 'exiting'
    exit(0)

if interest == "":
    interest = (discount/(1-discount))

if discount == "":
    discount = (interest/(1+interest))

vNew = (1/(1+interest))



'''
accumulation


annuityImmediate = ((1-v^n)/i)
'''
