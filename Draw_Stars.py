
# first way
stars = ['   *', '  ***', ' ***** ', '*******']

for i in stars:
    print(i)


#second way
stars =  ' '
for i in range(1,8,2):
    i = i * '*'
    if i == '*':
        stars = '   ' + i
    elif i == '***':
        stars = '  ' + i
    elif i == '*****':
        stars = ' ' + i
    else:
        stars = '' + i
    print(stars)

#third way
for i in range(1,8,2):
    i = i * '*'
    if i == 1 * '*':
        stars = '   ' + i
    elif i == 3 * '*':
        stars = '  ' + i
    elif i == 5 * '*':
        stars = ' ' + i
    else:
        stars = '' + i
    print(stars)

# Morteza solution
def draw(n):
    for i in range(n):
        print( " " * ( n - (i + 1))  +  "*" * ( 2 * i + 1))
            
            
 
    

 
