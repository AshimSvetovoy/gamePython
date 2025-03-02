import math
import random

ls = [4, 54, 287, math.pi, math.acos, True, "kto ya"]
result1 = random.choice(ls)
print(result1)

print("от 50 до 100", random.randint(50, 100))

print("от 0 до 993", random.randrange(993))

ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ls1)
resultls = random.shuffle(ls1)
print(resultls)

lsname = ['Jhonny', 'super sigma', 'oleg moroz', 'mario', 'valeriy', 'I always come back', 'random.choice(ls)']
print("Выйграл:", random.choice(ls))