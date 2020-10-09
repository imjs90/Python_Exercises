#return a new  list with the strings filtered out'
def filter_list(l):
    x = [i for i in l if not i == str(i)]
    return x

print(filter_list([1, 3, 'a', -1, 'b']))

#best solutions
def filter_list(l):
    return [i for i in l if type(i) is not str]

def filter_list(l):
    return filter(lambda i: not type(i) is str, l)
