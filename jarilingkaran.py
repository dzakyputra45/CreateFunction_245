import math
area_of_circle = lambda radius: math.pi * radius ** 2

radius = float(input("Masukkan jari-jari lingkaran: "))
print(f"Luas lingkaran dengan jari-jari {radius} adalah {area_of_circle(radius)}")