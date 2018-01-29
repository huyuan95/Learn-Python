def PuzzleSolve(k, S, U):
    for i in range(len(U)):
        a = U[i]
        S.append(a)
        U.remove(a)
        if k == 1:
            if S[0] + S[1] == S[2]: #and S[3] + S[4] == S[5] and S[6] + S[7] \
#                    == S[8]:
                return 'Solution Found: ', S
        else:
            return PuzzleSolve(k-1, S, U)
        S.remove(a)
        U.insert(i, a)
            
if __name__ == '__main__':
    print(PuzzleSolve(3, [], [1, 3, 2]))
