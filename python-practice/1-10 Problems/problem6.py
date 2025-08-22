# Q6. Convert temperature from Celsius to Fahrenheit.

# Let's give a chance to user to type temperature in celcius
celcius = input("Type the temperature in celcius: ") # input() always takes input as a string

celcius = int(celcius) # Converts the value into integer

fahrenheit = ((9/5) * celcius) + 32 # calculation of celcius to fahrenheit

print(f"{celcius}°C --> {fahrenheit}°F")

