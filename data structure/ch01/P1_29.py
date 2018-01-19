characters = ['c', 'a', 't', 'd', 'o', 'g']

def pick(s, a):
    if len(s) == 1:
        print(a + s[0])
        a=''
    else:
        for i in range(len(s)):
            a1=a
            a1 = a1 + s[i]
            s1=s.copy()
            s1.remove(s[i])
            pick(s1, a1)

pick(characters, '')
