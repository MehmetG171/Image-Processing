# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Conversion formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperatures_fahrenheit = [-40, 0, 32, 68, 98.6, 212]

print('Fahrenheit to Celsius')

for fahrenheit in temperatures_fahrenheit:
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f'{fahrenheit} F = {celsius} C')
