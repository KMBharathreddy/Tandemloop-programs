def generate_sequence(a):
    # Generate the sequence until a
    result = [i for i in range(1, a * 2, 2)]
    # If `a` is even, return up to the previous odd
    if a % 2 == 0:
        result.pop()
    print(", ".join(map(str, result)))

# Example usage
a = int(input("Enter a value for a: "))
generate_sequence(a)
