def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    s=sorted(args, key=key, reverse=reverse)[0]
    return s

def min(*args, key=None):
    return get_first_from_sorted(args, key, False)

def max(*args, key=None):
    return get_first_from_sorted(args, key, True)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3
    assert min(3, 2) == 2
    assert max([1, 2, 0, 3, 4]) == 4
    assert min("hello") == "e"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
