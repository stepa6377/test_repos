def func(number):
  number = number * 5
  count = 0
  while True:
    print(5)
    count += 1
    number += 2
    print('hello')
    if count == 100:
      print('STOP')
      print('Программа окончена')
      print(count, number)
      break

number = int(input('Введите число: '))

func(number)