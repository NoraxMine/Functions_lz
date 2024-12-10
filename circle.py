r = float(input('Введите радиус окружности: '))


def circle(k):
    S = 3.1415 * (int(k)*int(k))
    return S

S = circle(r)
print("Площадь окружности с данным радиусом равна: " + str(round(S, 3)))



def circle(k):
    C = 2 * 3.1415 * int(k)
    return C

C = circle(r)
print("Длина окружности с данным радиусом равна: " + str(round(C, 3)))