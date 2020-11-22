import math


def star_rating(rating: float):
    if rating > 5:
        return " ".join(["full"] * 5)
    decimal, integer = math.modf(rating)
    result = ['empty'] * 5
    i = 0
    while integer > i:
        result[i] = 'full'
        i += 1
    if i < 5:
        decimal = round(rating * 2) / 2
        result[i] = 'full' if decimal == 1 else 'half'
    return " ".join(result)

print(star_rating(4.85))