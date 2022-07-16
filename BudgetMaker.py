import math
expNum = int(input('Enter the number of expenses you have in a month.\n '))

expDict = {}

while expNum != 0:
    expName = input('Type the names of your current expenses hitting enter after each one.\n ')
    expNum = expNum - 1
    expDict[expName] = 0

for expName, v in expDict.items():
    if v is 0:
        print(expName)
        expDict[expName] = int(input('\nHow much did the following cost this month?: '))



print(sum(expDict.values()))
print (expDict)
