# Лабораторная работа №2 (Решение)
###  Выполнил: Миноцкий Ян Анатольевич ББСО-01-18

### Задание 1 - Установка ОС, настройка LVM, RAID
По заданию я выбрал создаваемой виртуальной машине соответствующие характеристики в настройках.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.1.png)

Далее я начал процесс установки. И дойдя до разметки дисков начал ручную разметку.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.2.png)

Создал разметку на жёстких дисках под raid...

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.3.png)

Создал RAID1 (зеркальный).

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.4.png)

Создал группу томов LVM.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.5.png)

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.6.png)

Установил томам LVM точки монтирования

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.8.png)

Далее установил GRUB на sda/

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.9.png)

После того, как ОС загрузилась, я проверил её работоспособность. Всёоказалось в норме. Результат ожидаем

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.10.png)

Далее я установил GRUB на sdb, чтобы система в случие отказа sda смогла запуститься. Но сделать это с помощью команды dd у меня не получилось. Пришлось использовать ...

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.11.png)

dd превосходит cp в том отношении, что при обнаружении ошибки cp прекратит работу, а dd не прекратит
