def proc1():
    spisok = [2, 5, 7, 9, 11]
    ch = input('Введите число:')
    if int(ch) in spisok:
        print('Поздравляю, вы угадали число!')
    else:
        print('Такого числа нет!')

def proc2():
    spisok = [2, 5, 7, 3, 3, 11]
    for i in range(len(spisok) - 1):
        if spisok[i] == spisok[i + 1]:
            ch = i
            print('Повторяющиеся элемент:', ch)

def proc3():
    days = ('Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскреснье")
    hoche = input('Сколько выходных на неделе вы хотите?')
    wd = days[:-int(hoche)]
    od = days[-int(hoche):]
    print('Ваши выходные дни:', *od)
    print('Ваши рабочие дни:', *wd)

def proc4():
    spisok1 = ['Кутилина', "Аги", "Лавриненко", "Клинова", "Поликарпова"]
    spisok2 = ['Сидоров', "Петров", "Иванов", "Трусов", "Холланд"]
    sport = (spisok1[2:] + spisok2[2:])
    print('Список первой группы:', *spisok1)
    print('Список второй группы:', *spisok2)
    print('Спортивная команда:', *sport)
    print(len(sport))
    sport = tuple(sorted(sport))
    ch = 0
    if 'Иванов' in sport:
        ch += 1
        print('Фамилия Иванов входит в список спортивной команды и встречается:', ch)
    else:
        print('Фамилии Иванов нет в списке спортивной команды')


proc1(), proc2(), proc3(), proc4()