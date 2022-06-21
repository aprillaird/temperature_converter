# Author Name: April Laird
# Date: 01/21/21
# Program name: Laird_temperature_converter.py
# Purpose: Convert temperature in Fahrenheit to Celsius

# Declare variable and prompt user for temperature in Fahrenheit
fahrenheitTemperature = int(input("Enter a temperature in Fahrenheit."))

# Declare variable and calculate
celsiusTemperature = (fahrenheitTemperature - 32) * 5/9

# Print result
print('The temperature in Celsius is',
      format(celsiusTemperature, '.1f'), 'degrees.')

