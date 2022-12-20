#have a storage of the amount to win
#3 = 1000 GHS , 4 = 5000 GHS , 2 = 500 GHS
#have the list of winning numbers. This time make it static(literals, constant). we declare the winning numbers ourselves
#have the user enter his numbers into an empty list, when the list of numbers reaches 5 then you close the list.
#check if the users numbers are in the winning numbers
#count how many matched


import utility

WinNums = [42, 76, 19, 4, 50, 96]
UserNums =[]
UserWins = []
maxNums = 5
numsEntered = 0


while numsEntered < maxNums:
    ReadNum = int(input('Enter your ' + str(numsEntered +1) + ' number: '))
    UserNums.append (ReadNum)
    numsEntered = numsEntered +1
    

print('These are the numbers you entered: ',UserNums)

#Go through the list of user numbers
#for each number, compare with winnums
#if itemexist returns 0, user number did not win
#if itemexist returns a number > 0, then user number won and must be put in user wins list
for number in UserNums:
    found = utility.ItemExist(WinNums, number)
    if found > 0:
        UserWins.append(number)
        continue

print('The winning numbers are',WinNums)       
print('You won with', len(UserWins), 'numbers -', UserWins)
print('You won ', utility.CalculateAmountWon(len(UserWins)), 'GHS')

#print('For 4 or 5 numbers, you win', CalculateAmountWon(4),'GHS')
#print('For 3 numbers, you win', CalculateAmountWon(3),'GHS')
#print('For 2 numbers, you win', CalculateAmountWon(2),'GHS')


