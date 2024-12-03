a = int(input())
b = int(input())
c = int(input())
d = int(input())

case1 = max(a, b) + 1 + 1
case2 = 1 + max(c, d) + 1
case3 = a + 1 + c + 1
case4 = b + 1 + d + 1

if a == 0:
    if max(c, d) == d:
        print(1, c + 1)
    else:
        print(1, max(c, d) + 1)
elif b == 0:
    if max(c, d) == c:
        print(1, d + 1)
    else:
        print(1, max(c, d) + 1)
elif c == 0:
    if max(a, b) == b:
        print(a + 1, 1)
    else:
        print(max(a, b) + 1, 1)
elif d == 0:
    if max(a, b) == a:
        print(b + 1, 1)
    else:
        print(max(a, b) + 1, 1)

elif min(case1, case2, case3, case4) == case1:
    print(max(a, b) + 1, 1)
elif min(case1, case2, case3, case4) == case2:
    print(1, max(c, d) + 1)
elif  min(case1, case2, case3, case4) == case3:
    print(a + 1, c + 1)
elif min(case1, case2, case3, case4) == case4:
    print(b + 1, d + 1)