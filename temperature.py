C = float(input("Введите ваше значения: "))


def Per(d):
    Di = (d * (9/5)) + 32
    return Di
    
Perevod = Per(C)
print("Ваше значение после перевода: " + str(round(Perevod, 4)) + " F")