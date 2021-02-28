lastTicket = 0


def lucky(ticket):
    global lastTicket
    lt, t = str(lastTicket), str(ticket)
    if len(lt) < 6:
        lt.rjust(6, '0')
    if len(t) < 6:
        lt.rjust(6, '0')
    print(lt, t)
    if lt == lt[::-1] and t == t[::-1]:
        return 'Счастливый'
    return 'Несчастливый'



