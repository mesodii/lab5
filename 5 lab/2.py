spisok = [2, 5, 7, 3, 3, 11]
for i in range(len(spisok)-1):
    if spisok[i] == spisok[i+1]:
        ch = i
        print('Повторяющиеся элемент:', ch)