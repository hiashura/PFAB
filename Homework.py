#!/usr/bin/env python

import math

first = "Shawn"
last = "Heimbigner"
age = 31

print first, last, age

sideA = 12.55
sideB = 17.85
sideC = math.sqrt(sideA * sideA + sideB * sideB)
print sideC

operand1 = 95
operand2 = 64.5

print operand1, "+", operand2, "=", operand1 + operand2
print operand1, "-", operand2, "=", operand1 - operand2
print operand1, "*", operand2, "=", operand1 * operand2
print operand1, "/", operand2, "=", operand1 / operand2
print "Remainder after", operand1, "/", operand2, "=", operand1 % operand2

#My code is just a solution. I used it because it would require less to rewrite if the numerical value of operand1 or operand 2 changed. I also decided to note that % was the remainder after a division