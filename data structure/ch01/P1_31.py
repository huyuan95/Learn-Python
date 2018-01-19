change = [5, 2, 1]

def make_change(charge, give):
    change_amount = give - charge
    sum_change = 0
    for i in range(len(change)):
        ni = change_amount // change[i]
        sum_change = ni + sum_change
        change_amount = change_amount % change[i]
    return sum_change

if __name__ == '__main__':
    print(make_change(134,255))
