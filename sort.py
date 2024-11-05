
list_1 =[2, 56, 32, 21 , 34 , 12,  18, 13, 9, 43]
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(list_1)-1):
        if list_1[i] < list_1[i+1]:# если первое число меншевторого, то мы меняем их менстами
            change = list_1[i]
            list_1[i] = list_1[i+1]#меняем местами числа
            list_1[i+1] = change
            stop_flag = True
        print(list_1)# выписываем состояние списка после каждой итерации


list_2 = list_1.copy


list_2 = [1, 26, 9, 19, 5, 12]
n = len(list_2)
for i in range(n):
        h = i
        for j in range(i, n):
            if list_2[j] > list_2[h]:# сравнтваем два элимента
                h = j
        list_2[i], list_2[h] = list_2[h], list_2[i]#записываем новый порядок

        print(list_2)