def sum_of_number(num_string):
    total = 0
    for digit in num_string:
        total += int(digit)
    print("Sum: ", total)
    
sum_of_number("24453")
