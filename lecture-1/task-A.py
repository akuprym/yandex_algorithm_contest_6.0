x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

rect = {
    "NW" : ((x1 - x)**2 + (y2 - y)**2)**0.5,
    "N" : 0,
    "NE" : ((x2 - x)**2 + (y2 - y)**2)**0.5,
    "E" : 0,
    "SE" : ((x2 - x)**2 + (y1 - y)**2)**0.5,
    "S" : 0,
    "SW" : ((x1 - x)**2 + (y1 - y)**2)**0.5,
    "W" : 0
}

if x < x1 or x > x2:
    rect["N"] = 10 ** 10
else:
    rect["N"] = abs(y - y2)

if y > y2 or y < y1:
    rect["E"] = 10 ** 10
else:
    rect["E"] = abs(x - x2)

if x < x1 or x > x2:
    rect["S"] = 10 ** 10
else:
    rect["S"] = abs(y1 - y)

if y > y2 or y < y1:
    rect["W"] = 10 ** 10
else:
    rect["W"] = abs(x1 - x)

print(min(rect, key=rect.get))



