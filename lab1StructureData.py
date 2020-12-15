def EuclideanAlgorithm(firstValue, secondValue):
	if secondValue == 0:
		return firstValue, 1, 0
	else:
		greatestCommonDivisor, x, y = EuclideanAlgorithm(secondValue, firstValue % secondValue)
		return greatestCommonDivisor, y, x - y * (firstValue // secondValue)

print("----------------------------------------------------------------------------")
print("Работу выполнил Шевченко Богдан Александрович, группа 2-5Б(020303-АИСа-о19)")
print("----------------------------------------------------------------------------")

firstValue = int(input("Введите первое число: "))
secondValue = int(input("Введите второе число: "))

greatestCommonDivisor, x, y = (EuclideanAlgorithm(firstValue, secondValue))

print("Наибольший общий делитель: " + str(greatestCommonDivisor));
print("Числа x = " + str(x) + " и y = " + str(y) + "(такие что: x*a + y*b = Наибольший общий делитель)")