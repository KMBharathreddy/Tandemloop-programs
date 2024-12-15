def generate_series(a):
    if a <= 0:
        return "Input must be a positive integer."
    
    series = [i for i in range(1, 2 * a, 2)]
    return ", ".join(map(str, series))

a = int(input("Enter a positive integer: "))
print(f"Generated series: {generate_series(a)}")
print("Error: Invalid input. Please enter a positive integer.")

#series = [i for i in range(1, 2 * a, 2)]
    #return ", ".join(map(str, series))

