a = int(input("Введите желаемое значение: "))


def dig(s):
    s = str(s)
    k = 0
    for i in range(len(s)):
        k += int(s[i])
    return k

Digitds = dig(a)
print("Преобразованное значение: " + str(Digitds))

