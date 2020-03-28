# inputs:
# 1. total miles driven per year
# 2. current mpg
# 3. mpg with upgrade
# 4. cost of fuel per gallon
# 5. mpg incrrease of current mpg 
# 6. furmula
#     10400 per year / 52 = miles per week = 200/ current mpg of 22 = gallons per week 9.09 x cost of fuel= 3.45x9.09=31.36d mpg
# out put how long to pay backtotal miles driven a year /current mpg.  take gallons per year  x price per gallon. compair with same same formula and change mpg to estimate mpg.

carOneMpg = input('current car mpg: ')
print (carOneMpg)

carTwoMpg = input('new car mpg: ')
print (carTwoMpg)

milesPerYear = input('total miles driven per year: ')
print (milesPerYear)

currentMpg = input('current Mpg: ')
print (currentMpg)

costPerGallon =input('cost of fuel per gallon: ')
print (costPerGallon)

increceMpg = input('mpg increase of current mpg: ')
print (increceMpg)

milesPerWeek = int(milesPerYear) / 52
print ('Miles Per Week: ' + str(milesPerWeek))

gallonsPerWeek = milesPerWeek / int(currentMpg)
print ('gallons Per Week: ' + str(gallonsPerWeek))

costOfFuel = gallonsPerWeek * float(costPerGallon)
print ('cost per week: $' + str(costOfFuel))

newGallonsPerWeek = milesPerWeek / int(increceMpg)
print ('New gallons Per Week: ' + str(newGallonsPerWeek))

newCostOfFuel = newGallonsPerWeek * float(costPerGallon)
print ('New cost per week: $' + str(newCostOfFuel))

defferenceInCost = costOfFuel - float(newCostOfFuel)
print ('Defference  in cost per week: $' +str(defferenceInCost))

defferenceInGallons = gallonsPerWeek - float(newGallonsPerWeek)
print ('defference In Gallons:' + str(defferenceInGallons))

defferenceInMpg = int(carOneMpg) -int(carTwoMpg)
print ('difference in mpg:' + str(defferenceInMpg))
