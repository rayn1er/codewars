def digitize(n):
    s = str(n)
    list = []
    for i in s:
        i = int(i)
        list.append(i)

    
    return list[::-1]


print(digitize(35231))