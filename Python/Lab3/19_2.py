def str_to_tuple(s):
    liters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if s[0] in liters:
        a = liters.index(s[0]) + 1
    else:
        return ValueError
    b = int(s[1])
    return a, b


def tuple_to_str(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        liters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        return liters[x-1] + str(y)
    else:
        return ValueError


def possible_turns(s):
    x, y = str_to_tuple(s)
    list_possible_turns = []
    if 1 <= x+2 <= 8 and 1 <= y+1 <= 8:
        list_possible_turns.append(tuple_to_str(x+2, y+1))
    if 1 <= x+1 <= 8 and 1 <= y+2 <= 8:
        list_possible_turns.append(tuple_to_str(x+1, y+2))
    if 1 <= x-1 <= 8 and 1 <= y+2 <= 8:
        list_possible_turns.append(tuple_to_str(x-1, y+2))
    if 1 <= x-2 <= 8 and 1 <= y+1 <= 8:
        list_possible_turns.append(tuple_to_str(x-2, y+1))
    if 1 <= x-2 <= 8 and 1 <= y-1 <= 8:
        list_possible_turns.append(tuple_to_str(x-2, y-1))
    if 1 <= x-1 <= 8 and 1 <= y-2 <= 8:
        list_possible_turns.append(tuple_to_str(x-1, y-2))
    if 1 <= x+1 <= 8 and 1 <= y-2 <= 8:
        list_possible_turns.append(tuple_to_str(x+1, y-2))
    if 1 <= x+2 <= 8 and 1 <= y-1 <= 8:
        list_possible_turns.append(tuple_to_str(x+2, y-1))
    return sorted(list_possible_turns)
