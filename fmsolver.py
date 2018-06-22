import os
import math
import numpy

#Place holders
a = 1
b = [1,2,3]

#Asks user for input, if interest/discount not entered, calculation will be based off other
try:
    interest = input('Enter interest in decimal format: ')
except SyntaxError:
    interest = None

try:
    discount = input('Enter discount in decimal format: ')
except SyntaxError:
    discount = None

#If neither are entered, it quits for now.
if interest == None and discount == None:
    print 'exiting'
    exit(0)


try:
    n = input('Time in Years: ')
except SyntaxError:
    n =  None


if interest == None:
    interest = (discount/(1-discount))

if discount == None:
    discount = (interest/(1+interest))

#Current approach to formulas is shotgunning it and running and calculating each one.
#May add functionality later to select which you need? Or maybe just print the ones selected?

vNew = (1/(1+interest))

presValue = vNew**n

simpInterest = (1 + (interest*n))

compInterest = ((1+interest)**n)

annuityImmediate = ((1-(vNew**n))/interest)

annuityDue = ((1-(vNew**n))/discount)





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
