message_base = set()


def print_only_new(message):
    global message_base
    if message not in message_base:
        print(message)
        message_base.add(message)
