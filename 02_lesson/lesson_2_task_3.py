def square(side):
    square_area = side * side
    return square_area


side_size = int(input("Введите сторону: "))
result = square(side_size)
print("Площадь квадрата:", result)
