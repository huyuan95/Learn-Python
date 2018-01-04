def comma_add(spam):
    comma_str = ', '.join(str(x) for x in spam[:-1])
    comma_str =comma_str + ' and ' + spam[-1]
    return comma_str

spam = ['apple', 'banana', 23, 'cats']
print(comma_add(spam))
