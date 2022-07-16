import math
expNum = int(input('Enter the number of expenses you have in a month.\n '))

expDict = {}

while expNum != 0:
    expName = input('\nType the names of your current expenses hitting enter after each one.\n ')
    expNum = expNum - 1
    expDict[expName] = 0

for expName, v in expDict.items():
    if v == 0:
        print(expName)
        expDict[expName] = int(input('\nHow much did the following cost this month?:\n '))

yearWageCheck = input('\nDo you know your annual wage? Yes or No? ')
if yearWageCheck in ['Yes', 'yes', 'Y', 'y']:
    yearWage = float(input('\nWhat is your annual wage? '))
    print('Nice! your yearly wage is \n$', yearWage)
if yearWageCheck in ['No', 'no', 'N', 'n']:
    yearWage = float(input('\nNo worries! What is your current hourly wage? '))
    yearWage = yearWage * 2080
    print('Nice! your yearly wage is \n$', yearWage)
elif yearWageCheck not in ['Yes', 'yes', 'Y', 'y', 'No', 'no', 'N', 'n']:
    print('\nInvalid Response :/ ')

payFreq = input('\nHow often do you get paid? (Weekly or Bi-Weekly) ')
if payFreq in ['Weekly', 'weekly', 'W', 'w']:
    yearWage = yearWage / 52
    yearWage = yearWage * 4
    print('\nSo you get paid Weekly, Nice! ')
if payFreq in ['BiWeekly', 'Biweekly', 'biWeekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly', 'bi-Weekly', 'bi-weekly', 'B', 'b']:
    yearWage = yearWage / 26
    yearWage = yearWage * 2
    print('\nSo you get paid Bi-Weekly, Nice! ')
elif payFreq not in ['BiWeekly', 'Biweekly', 'biWeekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly', 'bi-Weekly', 'bi-weekly', 'B', 'b' 'Weekly', 'weekly', 'W', 'w']:
    print('\nInvalid Response :/ ')

savPer = input('\nThe reccomended savings amount per month is 10% of monthly earnings. Is this a good amount? ')
if savPer in ['Yes', 'yes', 'Y', 'y']:
    savPer = .10
if savPer in ['No', 'no', 'N', 'n']:
    savPer = float(input('\nWhat percentage would you like to save? '))
    savPer = savPer / 100

monExp = (sum(expDict.values()))
savAmt = yearWage * savPer
leftOver = yearWage - monExp - savAmt
leftOverWeek = leftOver / 4

print('\n-------------------------------\n')
print('\nYour expense list is as follows\n', expDict)
print('\n-------------------------------\n')
print('Your mothly expense total is $', round(monExp,2) + round(savAmt,2), '\n')
print('\n-------------------------------\n')
print('\nYou are saving ', round(savAmt,2) ,' every month!')
print('\n-------------------------------\n')
print('\nOn a monthly basis, you have $', round(leftOver,2), 'Left over to work with for the month, or $', round(leftOverWeek,2), ' to left over to work with every week!')