# inputs:
# 1. total miles driven per year
# 2. current mpg
# 3. mpg with upgrade
# 4. cost of fuel per gallon
# 5. mpg incrrease of current mpg 
# 6. furmula
#     10400 per year / 52 = miles per week = 200/ current mpg of 22 = gallons per week 9.09 x cost of fuel= 3.45x9.09=31.36d mpg
# out put how long to pay backtotal miles driven a year /current mpg.  take gallons per year  x price per gallon. compair with same same formula and change mpg to estimate mpg.

NewCarMpg = input('new car mpg: ')
print (NewCarMpg)

OldCarMpg = input('current car mpg: ')
print (OldCarMpg)

mpgdifference = NewCarMpg - OldCarMpg 

print  ("mpg difference "+ str(mpgdifference))

MilesPerYear = input('MilesPerYear')

print (MilesPerYear)
