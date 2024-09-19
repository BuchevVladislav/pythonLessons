lenght = float(input('Введите длину нити маятника '))
import math
g = 9.81
period = 2*math.pi*((lenght/g)**(1/2))
print('Период колебания: ' , period)