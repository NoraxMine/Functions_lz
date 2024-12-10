r = int(input('Введите радиус окружности: '))


def circle(k):
    S = 3.1415 * (int(k)*int(k))
    return S

S = circle(r)
print("Площадь окружности с данным радиусом равна: " + str(S))



def circle(k):
    C = 2 * 3.1415 * int(k)
    return C

C = circle(r)
print("Длина окружности с данным радиусом равна: " + str(C))