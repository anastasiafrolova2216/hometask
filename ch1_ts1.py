from hometask.ch1 import Ch1

weight = float(input("Введите вес (кг.): "))
height = float(input("Введите рост (м.): "))

result = Ch1.BMI(weight, height)

print(result)
