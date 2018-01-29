def v_c(s, v=0, c=0):
    if len(s) == 0:
        if v >= c:
            return True
        else:
            return False
    if s[0] in ['a', 'e','i','o','u']:
        return v_c(s[1:], v+1, c)
    else:
        return v_c(s[1:], v, c+1)

if __name__ == '__main__':
    print(v_c('bee'))
    print(v_c('caro'))
