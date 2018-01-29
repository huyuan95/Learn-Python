def palindrom(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if s[0] == s[-1]:
        return palindrom(s[1:-1])
    return False

if __name__ == '__main__':
    print(palindrom('racecar'))
    print(palindrom('gohangasalamiimalasagnahog'))
    print(palindrom('gohangasalamiimalcsagnahog'))
