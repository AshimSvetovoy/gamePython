from rich.console import Console
from rich.text import Text
from rich import print

O = "[magenta]0[/magenta]"
X = "[green]X[/green]"

win0 = False
winX = False
plain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nВыберите кто будет играть первый\n1.Крестики\n2.Нолики ")
choose = int(input())
if choose == 1:
  print()
  step = O
elif choose == 2:
  step = X
else: print("Неправильный ввод")
while win0 == False and winX == False:
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  if step == O:
    step = X
    print("Ходят крестики")
  else:
    step = O
    print("Ходят нолики")
  print(plain[0], plain[1], plain[2])
  print(plain[3], plain[4], plain[5])
  print(plain[6], plain[7], plain[8])
  cell = int(input("Введите номер клетки: ")) 
  if cell > 0 and cell < 10 and plain[cell - 1] != X and plain[cell - 1] != O:
     plain[cell - 1] = step   
     print(plain[cell - 1])
  elif plain[cell - 1] == X or plain[cell - 1] == O:
    if step == X:
      step = O
    if step == O:
      step = X    
  else:
    print("Неправильный ввод")