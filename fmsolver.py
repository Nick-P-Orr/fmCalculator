import os
import math
import numpy

#Place holders
a = 1
b = [1,2,3]

#Asks user for input, if interest/discount not entered, calculation will be based off other
try:
    i = input('Enter interest in decimal format: ')
except SyntaxError:
    i = None

try:
    discount = input('Enter discount in decimal format: ')
except SyntaxError:
    discount = None

#If neither are entered, it quits for now.
if i == None and discount == None:
    print 'exiting'
    exit(0)


try:
    n = input('Time in Years: ')
except SyntaxError:
    n =  None


if i == None:
    i = (discount/(1-discount))

if discount == None:
    discount = (i/(1+i))


#Current approach to formulas is shotgunning it and running and calculating each one.
#May add functionality later to select which you need? Or maybe just print the ones selected?


v = (1/(1+i))

presValue = v**n

simpInterest = (1 + (i*n))

compInterest = ((1+i)**n)

annuityImmediate = ((1-(v**n))/i)

annuityDue = ((1-(v**n))/discount)

ssub = (((1+i)**n)*annuityImmediate)

decreasingPaymentDA = ((n-annuityImmediate)/i)

decreasingPaymentDS = (((1+i)**n) * decreasingPaymentDA)

'''
Too be implemented
accumulation

#Force of interest will require integral

#Geometric series,
((r(1-(r**n)))/(1-r))
(assumes k starting at 1)

(r/(1-r))
|r|<1
(assumes k starting at 1)


'''
