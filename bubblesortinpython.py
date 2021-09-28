def test():
    list = []
    numberofinputs = int(input("Enter the number of inputs: "))
    x = 0
    while x<numberofinputs:
        listnumber = int(input("Enter a number: "))
        list.append(listnumber)
        x = x + 1
    print(list)
    for i in range(0, len(list)):
        for y in range(0, len(list) - i - 1):
            if list[y]>list[y + 1]:
                list[y], list[y + 1] = list[y + 1], list[y]
            elif list[y]<=list[y + 1]:
                pass
    print(list)
test()