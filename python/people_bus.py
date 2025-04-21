def number(bus_stops):
    up = 0
    down = 0

    for i in bus_stops:
        up,down = up + i[0], down + i[1]
    
    return up - down


print(number([[10,0],[3,5],[5,8]]))