import math

a = float (input ("Введіть перше невідємне число a  "))

while a < 0:
    print ("Число a невідємне ")
    a = float (input ("Введіть перше невідємне число a "))

b = float (input ("Введіть друге невідємне число b (не може бути 0) "))

while b <= 0:
    print ("Число b має бути відмінне від нуля і невідємне ")
    b = float (input ("Введіть друге невідємне число b (не може бути 0) "))


sqrt = math.sqrt(a*b)
e = math.e

x = sqrt / ((e**a)*b) + a * (e**((2*a)/b))

formated_res = "{:.12f}".format(x)

print ("Результат:' ", formated_res )