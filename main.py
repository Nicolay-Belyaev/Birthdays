import datetime

budget = 12033
target_month = 7
employees = {
    'Иванов Сергей': datetime.date(1988, 5, 30),
    'Петров Михаил': datetime.date(1999, 4, 12),
    'Кузнецова Светлана': datetime.date(2002, 6, 1),
    'Смирнов Алексей': datetime.date(1978, 12, 12),
    'Сидорова Татьяна': datetime.date(1995, 4, 22),
    'Михайлов Андрей': datetime.date(1964, 7, 12),
    'Суворов Александр': datetime.date(2001, 7, 9),
    'Дмитриева Наталья ': datetime.date(1991, 12, 30)
}

# Алгоритм: выбрать из всего списка тех, у кого день рождения в текущем месяце и соберем их в новый словарь.
# Если таких нет - выводим соответствующее сообщение и выходим.
# Если есть, сортируем их по номеру дня рождения и собираем в итоговую строку.
# Считаем размер подарка, округляем и добавляем к итоговой строке.


def gift_count(budget: int, birthdays: dict, month):
    # соберем словарь из тех, у кого день рождения в этом месяце
    month_birthdays = {}
    for record in birthdays.items():
        if record[1].month == month:
            month_birthdays[record[0]] = record[1]
    birthday_boys_counter = len(month_birthdays)

    # проверим, может быть в этом месяце дней рождения нет
    if birthday_boys_counter == 0:
        print('В этом месяце нет именинников.')
        return

    sorted_month_birthdays_tuple = sorted(month_birthdays.items(), key=lambda x: x[1].day)  # отсортируем по номер дня
    result_string = f'Именинники в месяце {birthday_boys_counter}: '  # начнем собирать строку
    for birthday_boy in sorted_month_birthdays_tuple:
        result_string += f'{birthday_boy[0]}({birthday_boy[1].strftime("%d.%m.%Y")}), '  # добавим имена и даты
    gift = round(budget / birthday_boys_counter)  # посчитаем, сколько достанется каждому

    result_string = result_string[0:-2] + '.' + f' При бюджете {budget} они получат по {gift} рублей.'  # дособираем всё
    print(result_string)


gift_count(budget, employees, 12)
