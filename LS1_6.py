# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите результаты пробежки первого дня в км: "))
b = int(input("Введите желаемый результат в км: "))
day = 1
while a < b:
    a = a + 0.1 * a
    day += 1
if a >= b:
    print(f" Вы доcтигнете результата на %.d день" % day)
