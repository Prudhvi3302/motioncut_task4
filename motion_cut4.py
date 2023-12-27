def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Select an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter either '1' or '2'.")
        return

    temperature = float(input("Enter the temperature value: "))

    if choice == '1':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {result} Fahrenheit.")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {result} Celsius.")

if __name__ == "__main__":
    temperature_converter()
