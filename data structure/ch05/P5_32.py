def comp_add(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(a[0][0])):
                a.[i][j][k] += b[i][j][k]
