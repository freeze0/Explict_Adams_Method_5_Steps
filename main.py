import math
import csv

def adams5(f, y0, x0, h, X):
    x_values = [x0]
    y_values = [y0]

    for i in range(4):
        k1 = h * f(x_values[i], y_values[i])
        k2 = h * f(x_values[i] + h / 2, y_values[i] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, y_values[i] + k2 / 2)
        k4 = h * f(x_values[i] + h, y_values[i] + k3)
        x_values.append(x_values[i] + h)
        y_values.append(y_values[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    while x_values[-1] < X:
        xn = x_values[-1]
        yn = y_values[-1]

        f1 = f(xn, yn)
        f2 = f(xn - h, y_values[-2])
        f3 = f(xn - 2 * h, y_values[-3])
        f4 = f(xn - 3 * h, y_values[-4])
        f5 = f(xn - 4 * h, y_values[-5])

        y_new = yn + (h / 720) * (1901 * f1 - 2774 * f2 + 2616 * f3 - 1274 * f4 + 251 * f5)
        xn_new = xn + h

        y_values.append(y_new)
        x_values.append(xn_new)

    return x_values, y_values


# 3 графика точное решение с h/2 второй адамс h/2 и адамс h
# надо выводить точное

def f(x, y):
    return -2*x*y**2/(x**2-1)
    #-2*x*y**2/(x**2-1) #x**3+x+3*y/x #2*x*y/(x**2+y**2) филиппов 106#


def func(x): #точная функция
    return 2-3*math.cos(x)
    #2-3*math.cos(x) #x**4-x**2+2*abs(x)**3 #x**2-y**2=y филиппов 106#


x_values, y_values = adams5(f, 5, 3.14, 0.1, 4)
#adams5(f, 1, 0, 0.1, 2) #adams5(f, 2, -1, 0.1, 0) #adams5(f, -1, 0, 0.1, 2) филиппов 106
x_values_h2, y_values_h2 = adams5(f, 5, 3.14, 0.1/2, 4) #шаг h/2
y_values_h2_toch = []
for i in x_values_h2: #точное с шагом h2
    y_values_h2_toch.append(func(i))


print("Решение уравнения y= 2*x*y/(x**2+y**2)")
for x, y in zip(x_values, y_values):
    print(f"y({x:.2f}) = {y}")

for x, y in zip(x_values_h2, y_values_h2):
    print(f"y({x:.2f}) = {y}")


with open('answer.csv', 'w', newline='') as csvfile:
    fieldnames = ['x_h/2', 'y_tochnoe_h/2', 'y_adams_h/2', 'x_h', 'y_adams_h']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(x_values_h2)):
        writer.writerow({'x_h/2': x_values_h2[i], 'y_tochnoe_h/2': y_values_h2_toch[i], 'y_adams_h/2': y_values_h2[i]})
    for i in range(len(x_values)):
        writer.writerow({'x_h': x_values[i], 'y_adams_h': y_values[i]})
