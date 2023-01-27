spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
#print(spam)

def listToString(array):
    result = ''
    for i in range(len(array)):
        if i == len(array) - 1:
            result = result + 'and ' + array[i] +'.'
            print(result)
        else :
            result = result + array[i] + ', '

grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

for i in range(6):
    for j in range(len(grid)):
        print(grid[j][i], end = ' ')
    print('\n')
