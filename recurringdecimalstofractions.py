#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:57:18 2020

@author: craigsim

Created using Spyder(Python 3.6)
"""
import re
import math


def lcm(a, b):
    #Compute the lowest common multiple LCM
    #use math.gcd to calculate the greatest common divisor GCD
    return a * b / math.gcd(a, b)


def compute_fraction_from_string(mystring):
    #Unpack the string into actual decimal
    #Use regular expressions to extract the numbers
    
    #Full decimal without brackets
    newstring = re.sub(r'[()]', '', mystring)
    #Extract the number after the decimal point
    newfloat = re.sub("^.*?\\.", "", newstring)
    #Extract the integer before the decimal point
    newint = re.sub("\..*$", "", newstring)
    
    #Convert to integer from string
    intint = int(newint)
    #Find the length of the repeating part of the decimal
    length = len(newfloat)
    #Convert full number to a float
    number = float(newstring)
    #Find the 
    sf = number - intint
    shiftfloat = round(sf, length)
    
    #Shift the decimal by the power of 10 the number of places to the left
    #that equals the length of the repeating number after the decimal point
    shift = 10 ** length
  
    #Need to make the decimal recur by concatenating the recurring floating point
    #values up to a precision of 50 to approximate the recurrance 
    newnumber = number #Initialise Values
    itershift = shiftfloat # Initialise Values
    i = 0
    k = length * 50
    while i < k:
        i += 1
        itershift = itershift / shift
        newnumber = newnumber + itershift
    
    #figure out the "SHIFTEDx-x" shifted equation to workout the fraction
    #Calculate what the shift is by counting the characters:
    #For Example:
    #6.(6) - 0.(6) = 6 
    #10x - x = 9
    #
    #Do the calculation  
    num_results = (newnumber * shift) - newnumber
    denom_results = shift - 1
    
    #Round the results as we're approximating the reccuring floating point 
    rounded = round(num_results)

    #Find the lowest common denominator LCD
    lcd = lcm(rounded, denom_results)

    #Calculate the LCD results
    #The lcd calc effectively flips the fractions denom and numerator, 
    #we need to flip back to display the correct lowest common denominator 
    #result - Hence the calculation is as follows:
    LCDdenom = lcd / rounded
    LCDnum = lcd / denom_results
    
    lcdresult = str(LCDnum) + "/" + str(LCDdenom)
    finalresult = mystring + " = " + lcdresult
    return finalresult


#Test the fraction function
#fractions("9.(0)") ? "9/1"
mystring = '9.(0)'
r = compute_fraction_from_string(mystring)
print(r)
#fractions("0.(6)") ? "2/3"
mystring = '0.(6)'
r = compute_fraction_from_string('0.(6)')
print(r)
#fractions("1.(1)") ? "10/9"
mystring = '1.(1)'
r = compute_fraction_from_string(mystring)
print(r)
#fractions("3.(142857)") ? "22/7"
mystring = '3.(142857)'
r = compute_fraction_from_string(mystring)
print(r)
#fractions("33.(142857)") ? "232/7"
mystring = '33.(142857)'
r = compute_fraction_from_string(mystring)
print(r)


