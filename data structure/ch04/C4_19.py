def even_odd(data, redata):
    if len(data) == 0:
        return redata
    else:
        if data[0] % 2 == 0:
            redata.insert(0, data[0])
            return even_odd(data[1:], redata)
        else:
            redata.append(data[0])
            return even_odd(data[1:], redata)

if __name__ == '__main__':
    print(even_odd([1,2,3,4,5,6,7],[]))
    print(even_odd([1,3,5,7,2,4,6,8],[]))
