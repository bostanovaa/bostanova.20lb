a = [-28, 2, 44, -7, -45, 1, 12, -77]
sum = 0
for a in a:
    if a < 0:
        sum += a ** 3
print("Сумма кубов отрицательных чисел:", sum)