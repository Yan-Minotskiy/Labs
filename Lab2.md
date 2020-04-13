# Лабораторная работа №2 (Решение)
###  Выполнил: Миноцкий Ян Анатольевич ББСО-01-18

### Задание 1 - Установка ОС, настройка LVM, RAID
По заданию я выбрал создаваемой виртуальной машине соответствующие характеристики в настройках:
| Параметр  | Значение  |
| ------------ | ------------ |
| Операционная система | Debian 10.3 |
|  Оперативная память | 1 GB  |
| Процессор  |  1 ядро |
| SSD  | 2 шт.  |
| Объём дисков  | 8 GB  |
| SATA контроллер  | 4 порта  |

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.1.png)

Далее я начал процесс установки и, дойдя до разметки дисков, приступил к ручной разметке.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.2.png)

Создал разметку на жёстких дисках под raid...

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.3.png)

Создал RAID1.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.4.png)

> **RAID 1 (Mirror)**. Несколько дисков (обычно 2), работающие синхронно на запись, то есть полностью дублирующие друг друга.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/RAID1.jpg)

Создал группу томов LVM.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.5.png)

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.6.png)

Установил томам LVM точки монтирования.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.7.png)

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.8.png)

Далее установил GRUB на sda.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.9.png)

> **GRUB (GRand Unified Bootloader)** — программа-загрузчик операционных систем..

После того, как ОС загрузилась, я проверил её работоспособность. Всёоказалось в норме. Результат ожидаем.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.10.png)

Команда `lsblk`  выдала красивую информацию о состоянии дисков. С помощью команды `dd if=/dev/sda1 of=/dev/sdb1` я копировал содержимое раздела /boot с диска sda (ssd1) на диск sdb (ssd2).  Выполнил установку загрузчика ОС на второй диск с помощью `grub-install /dev/sdb`. Теперь в случае отказа первого диска система сможет спокойно загрузится.

![](https://github.com/Yan-Minotskiy/labOS/blob/master/screenshots/2.11.png)

C помощью команды `cat /proc/mdstat` я ознакомился с информацией о текущем состоянии raid, где md0 — имя RAID устройства; raid1 sda2[0] sdb2[1] — из каких дисков собран; 1046528 blocks — размер массива; [2/2] [UU] — количество юнитов, которые на данный момент используются.
- `pvs` - выводит информацию о физической памяти
- `lvs` - выводит информацию о Logical Volume
- `vgs` - выводит информацию о группе томов LVM

**Благодаря данному зданию я научился:**
- **устанавливать ОС Linux на VirtualBox;**
- **создавать диски;**
- **производить разметку дисков;**
- **создавать RAID;**
- **монтировать тома LVM;**
- **просматривать информацию о состояниях дисков и raid;**
- **устанавливать GRUB.**

------------

### Задание 2 - Эмуляция отказа одного из дисков
