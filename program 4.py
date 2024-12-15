def count_multiples(input_list):
    
    numbers = range(1, 10)
    result = {n: sum(1 for x in input_list if x % n == 0) for n in numbers}
    return result

input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(input_list)
print(output)
