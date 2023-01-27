tableData = [['apples', 'oranges', 'cherries', 'banana'], 
 ['Alice', 'Bob', 'Carol', 'David'], 
 ['dogs', 'cats', 'moose', 'goose'],
 ['rodrick', 'philo', 'kagaiga', 'jonathan']]

def printTable(tableData):
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        currMax = len(tableData[i][0])
        for item in tableData[i]:
            if len(item) > currMax:
                currMax = len(item)
        colWidths[i] = currMax + 1

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end = '')
        print('\n')

    print(colWidths)
    
printTable(tableData)
