def celsius_to_fahrenheit(c):
    # BUG: The formula is incorrect; the correct formula should be (c * 9/5) + 32
    return c * 9 / 5

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def meters_to_feet(m):
    # BUG: Syntax error, intentional
    return m * 3.28084