def fun():
    a = 3
    b = 1
    c = 2
    b = b ^ a ^ c * 2
    if b and c:
        b = 1
        if a:
            a = a * a % 5
        c = 0
    print(a+b+c)


fun()
