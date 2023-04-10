# import math
# l_1, w_1, h_1 = map(float, input().split())
# square = l_1 * h_1 * 2 + w_1 * h_1 * 2
# banki = math.ceil(square / 16)
# # num_2 = int(input())
# # num_3 = int(input())
# # kol_part = math.ceil(num_1 / 2) + math.ceil(num_2 / 2) + math.ceil(num_3 / 2)
# print(banki)

# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# if num_1 == num_2 == num_3:
#     print(3)
# elif num_1 == num_2 or num_2 == num_3 or num_1 == num_3:
#     print(2)
# else:
#     print(0)

# psw_1 = input()
# psw_2 = input()
# if len(psw_1) < 7: print('Short')
# elif psw_1 == psw_2: print('OK')
# else: print('Difference')


# s = 'hEllO WoRlD'
# print(s.swapcase().capitalize().swapcase().lower())
# print(len(input().split()))
# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# print('-'.join(list_strings))
# str = input().lower()
# print(str.startswith('mam'))
# prefix = input()
# postfix = input()
# print(s.startswith(prefix) and s.endswith(postfix))
# print(input().islower())
# str = input()
# print(input().rstrip('-_!?'))

# n = input()
# match n:
#     case 'Овен' | 'Лев' | 'Стрелец':
#         print('Огненный')
#     case 'Телец' | 'Дева' | 'Козерог':
#         print('Земной')
#     case 'Близнецы' | 'Весы' | 'Водолей':
#         print('Воздушный')
#     case 'Рак' | 'Скорпион' | 'Рыбы':
#         print('Водный')
#     # case 5:
#     #     print('Босс качалки')
#     case _:
#         print('Неизвестный курс')

# a, b = map(int, input().split())
# ostatok = a
# while ostatok > 0:
#     ostatok = ostatok // b
#     a = a + ostatok
# print(a)

# num = int(input())
# # a = 0
# while str(num)[0] != '1' and num < 10 ** 9:
#     num = int(str(num)[0]) * num
# print(num)
# objs = iter([23, 78, True, 'hello', [123, 433]])
# print(next(objs))

