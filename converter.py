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
    else:
        print('Invalid second argument')
