import math
expNum = int(input('Enter the number of expenses you have in a month.\n '))

expDict = {}

while expNum != 0:
    expName = input('Type the names of your current expenses hitting enter after each one.\n ')
    expNum = expNum - 1
    expDict[expName] = 0

for expName, v in expDict.items():
    if v == 0:
        print(expName)
        expDict[expName] = int(input('\nHow much did the following cost this month?: '))

yearWageCheck = input('\nDo you know your annual wage? Yes or No? ')
if yearWageCheck in ['Yes', 'yes', 'Y', 'y']:
    yearWage = input('\nWhat is your annual wage? ')
    print('Nice! your yearly wage is \n', yearWage)
if yearWageCheck in ['No', 'no', 'N', 'n']:
    yearWage = input('\nNo worries! What is your current hourly wage? ')
    yearWage = yearWage * 2080
    print('Nice! your yearly wage is \n', yearWage)
elif yearWageCheck not in ['Yes', 'yes', 'Y', 'y', 'No', 'no', 'N', 'n']:
    print('\nInvalid Response :/ ')



print(sum(expDict.values()))
print(expDict)
