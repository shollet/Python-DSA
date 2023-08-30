def numberOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(twoDArray,0,col-1,cost-twoDArray[0][col])
    elif col == 0:
        return numberOfPaths(twoDArray,row-1,0,cost-twoDArray[row][0])
    else:
        op1 = numberOfPaths(twoDArray, row-1, col, cost - twoDArray[row][col])
        op2 = numberOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col])
        return op1+op2