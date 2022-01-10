def test():
    x = []
    y = int(input("Enter the number of inputs: "))
    z = 0
    while z<y:
        a = int(input("Enter the number: "))
        x.append(a)
        z = z + 1
    for i in range(1, len(x)):
        b = x[i] 
        c = i - 1
        while c>=0 and b<x[c]:
            x[c + 1] = x[c]
            c = c - 1
        x[c + 1] = b
    print(x)
test()