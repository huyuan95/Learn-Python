def printTable(table):
    colWidth = [0] * len(table)
    for i in range(len(table)):
        colWidth[i] = max(len(s) for s in table[i])
    for j in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][j].rjust(colWidth[i])+' ', end = '')
        
        print('\n')
    return

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
