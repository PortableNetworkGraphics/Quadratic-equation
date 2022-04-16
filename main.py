import math
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print("brak miejsc zerowych.")
    elif delta == 0:
        x0 = -(b) // 2 * a
        print(x0)
    elif delta > 0:
        pierwiastekDelta = math.sqrt(delta)
        x1 = (-b - pierwiastekDelta)/(2 * a)
        x2 = (-b + pierwiastekDelta)/(2 * a)
        print(x1, x2)
quadratic(1, 5, 3)