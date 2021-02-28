n = None
v = None


def setup_profile(name, vacationDates):
    global n, v
    n = name
    v = vacationDates


def print_application_for_leave():
    print('Заявление на отпуск в период ', v, '. ', n, sep='')


def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег.', n)


def print_attorney_letter(toWhorm):
    print('На время отпуска в период ', v, ' моим заместителем назначается ', toWhorm, '. ', n, sep='')
