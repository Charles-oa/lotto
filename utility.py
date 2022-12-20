def ItemExist(listofNumbers, numberTofind):
    position = 0
    count = 0
    for number in listofNumbers:
        count = count + 1
        if (numberTofind == number):
            position = count
            break
        
    return position

def CalculateAmountWon(TotalWinningNums):
    match TotalWinningNums:
        case 2:
            return 500
        case 3:
            return 1000
        case 4 | 5:
            return 5000
        case _:
            return 0