def convert_temperature(value, unit):
    if unit.upper() == 'C':
        # Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        # Fahrenheit ke Celsius
        return (value - 32) * 5/9
    else:
        return "Unit tidak valid, gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Meminta input dari pengguna
print("Pilih konversi suhu:")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
choice = input("Masukkan pilihan (1/2): ")

if choice == '1':
    temp = float(input("Masukkan suhu dalam Celsius: "))
    result = convert_temperature(temp, 'C')
    print(f"{temp}°C adalah {result}°F")
elif choice == '2':
    temp = float(input("Masukkan suhu dalam Fahrenheit: "))
    result = convert_temperature(temp, 'F')
    print(f"{temp}°F adalah {result}°C")
else:
    print("Pilihan tidak valid!")