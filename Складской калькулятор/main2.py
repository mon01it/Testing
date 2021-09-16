d = 0
a = input('Цена с сотыми, без точки\n')
try:
    a = int(a)
except ValueError:
    a = input('Вы ввели буквы вместо цифр. Введите цену с сотыми, без точки\n')
while True:
  if d > 0:
   a = input("цена с сотыми, без точки или введите любую букву, для подсчета ндс\n")
  try:
      a = int(a)
  except ValueError:
        c = y / 100 * 120
        print("Стоимость с НДС", c, "рубля")
        break
  b = int(input("количество\n"))
  a = float(a)
  a = a / 100
  c = a * b
  if d > 0: # вторая и последущие этерации
    z = a * b + y
    d += 1
    y = z
    print("Итого: ", z, "рубля")
  else:#первая этерация
   y = c
   d += 1
   print("Итого: ", y, "рубля")
