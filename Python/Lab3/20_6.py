list_bet = []


def do_bet(num, sum):
    global list_bet
    if num not in list_bet and sum > 0:
        print('Ваша ставка в размере', str(sum), 'на лошадь', str(num), 'принята.')
        list_bet.append(num)
    else:
        print('Что-то пошло не так, попробуйте еще раз.')
