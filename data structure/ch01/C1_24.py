def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for ch in string:
        if ch in vowels:
            result += 1
    return result
