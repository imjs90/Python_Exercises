#Count Values 
my_string = [1,1,2,1,3,2]
a = dict((i, my_string.count(i)) for i in set(my_string))
b = [[i , my_string.count(i)] for i in set(my_string)]
print(a, b)
