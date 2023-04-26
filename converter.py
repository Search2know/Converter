def converter(degrees: str):
    try:
        value, unit = degrees.split(' ')
        value = float(value)
    except Exception:
        print('Invalid input')
        return

    unit = unit.lower()

    if unit == 'f':
        f_to_c = round((value - 32) / 1.8, 2)
        f_to_k = round((value - 32) / 1.8 + 273.15, 2)
        print(f'Conversion result: {value}°F = {f_to_c}°C')
        print(f'Conversion result: {value}°F = {f_to_k}°K')
    elif unit == 'k':
        k_to_c = round(value - 273.15, 2)
        k_to_f = round((value - 273.15) * 1.8 + 32, 2)
        print(f'Conversion result: {value}°K = {k_to_c}°C')
        print(f'Conversion result: {value}°K = {k_to_f}°F')
    elif unit == 'c':
        c_to_f = round(value * 1.8 + 32, 2)
        c_to_k = round(value + 273.15, 2)
        print(f'Conversion result: {value}°C = {c_to_f}°F')
        print(f'Conversion result: {value}°C = {c_to_k}°K')
    else:
        print('Invalid second argument')


print("Enter degrees by Celsius, Fahrenheit, or Kelvin, for example, '23 C', '23 F', or '23 K':")
degrees = input()
converter(degrees)
