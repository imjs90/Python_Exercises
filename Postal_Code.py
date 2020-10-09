# create postal code with ten numbers
def postal_code(numbers):
    parantises = '(' + numbers[0:3] + ')'
    dash = numbers[3:6] + "-" + numbers[6:10]
    total = parantises + " " + dash
    return total
print(postal_code('1234567890'))

    
