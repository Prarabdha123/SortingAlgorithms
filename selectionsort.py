def test():
    x = []
    y = int(input("Enter the number of inputs: "))
    z = 0
    while z<y:
        a = int(input("Enter the number: "))
        x.append(a)
        z = z + 1
    for i in range(0, len(x)):
        b = i 
        for c in range(i + 1, len(x)):
            if x[c]<x[b]:
                b = c 
        x[i], x[b] = x[b], x[i]
    print(x)
test()