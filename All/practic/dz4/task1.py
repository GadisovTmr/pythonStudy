# 1. Вычислить число c заданной точностью d
from decimal import Decimal

def accuracy():
    a = float(input('введите число '))
    b = Decimal(input('введите точность '))
    result = Decimal(a).quantize(Decimal(b))
    return result


print(accuracy())