ask = "yes"
while ask != "no":
    print("Choose option: 1. Celsius to Fahrenheit, 2. Fahrenheit to Celsius")
    option = input("Enter your option: ")
    
    if option == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = round((celsius * 9/5) + 32,2)
        print(f"Temperature in Fahrenheit is: {(fahrenheit)} °F")
        
    elif option == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = round((fahrenheit - 32) * 5/9,2)
        print(f"Temperature in Celsius is: {(celsius)} °C")
        
    else:
        print("Invalid option. Please choose 1 or 2.")
    
    ask = input("Do you want to continue? (yes/no): ").strip().lower()
print("\n Thank you for using the converter!")
