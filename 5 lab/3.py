days = ('Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскреснье")
hoche = input('Сколько выходных на неделе вы хотите?')
wd = days[:-int(hoche)]
od = days[-int(hoche):]
print('Ваши выходные дни:', *od)
print('Ваши рабочие дни:', *wd)