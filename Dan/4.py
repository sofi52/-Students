for x in range(400000002, 600000000 + 1, 6):
    m = 0
    n = 0
    i = x
    while i % 2 == 0:
        m+=1
        i //= 2
    if m % 2 ==  0:
        i = x
        while i % 3 == 0:
            n+=1
            i //= 3
        if n % 2 != 0:
            if x == (2**m)*(3**n):
                print(x)
