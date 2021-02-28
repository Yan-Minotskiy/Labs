import time

t = int(input())
while t > 0:
    print('Осталось секунд:', t)
    t -= 1
    time.sleep(1)
print('Осталось секунд: 0')
print('Пуск')
