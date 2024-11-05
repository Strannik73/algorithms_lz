list_1 = [1, 26, 9, 19, 5, 12]
n = len(list_1)
for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if list_1[j] < list_1[m]:
                m = j
        list_1[i], list_1[m] = list_1[m], list_1[i]

        print(list_1)