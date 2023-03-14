# Ask the user for the temperature outside in Celsius, then convert it to Fahrenheit

celsiustemp = input("How many degrees is it outside?")
fahrenheittemp = float(celsiustemp) * 9/5 + 32
print(fahrenheittemp)