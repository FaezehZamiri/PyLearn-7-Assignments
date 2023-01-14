def generate_rug(x):
    list1 = []
    list2 = []
    for _ in range(x):
        list1.append(int(x / 2))
    for _ in range(x):
        list2.append(list1)
        list1 = list(list1)
    rug = list2
    length = len(rug)
    rug_border = rug[0][0]
    diff = rug_border
    left = 0
    right = length

    for i, j in enumerate(rug):
        if i == (length - 1):
            break
        if i == 0:
            continue
        left += 1
        right -= 1
        if left >= right:
            break
        for k in range(left, right):
            rug[i][k] = rug_border - i
        rug[i + 1] = list(j)


    top = rug[:rug_border + 1]
    bottom = rug[:rug_border]
    bottom.reverse()

    for item in bottom:
        top.append(item)

    rug = top

    for i, j in enumerate(rug):
        print(j)
    


n = int(input('Please enter a number :'))
generate_rug(n)