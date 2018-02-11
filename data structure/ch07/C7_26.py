def concatenate(Q2):
    Q1.enqueue( Q2._header._next)
    Q1._tail = Q2._tail

