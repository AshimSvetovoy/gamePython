import random

print('1.Камень\n2.Ножницы\n3.Бумага')
choice = int(input('1 игрок или 2 игрока? '))
if choice == 1:
  ps = int(input("ход игрока: "))
  bs = random.randint(1,3)
  if bs == 1:
    print('Бот выбрал камень')
  elif bs == 2:
    print('Бот выбрал ножницы')
  elif bs == 3:
    print('Бот выбрал бумагу')
else:
  ps = int(input("ход игрока1: "))
  bs = int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1.Камень\n2.Ножницы\n3.Бумага\nход игрока2: "))

if ps == bs:
  print('Ничья')
elif (ps == 1 and bs == 2) or (ps == 2 and bs == 3) or (ps == 3 and bs == 1):
  print('Игрок1 выйграл')
elif (bs == 1 and ps == 2) or (bs == 2 and ps == 3) or (bs == 3 and ps == 1):
  print('Игрок2 выйграл')
