def is_distinct(data):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False
