#Find Odd Number

#First way
def find_it(seq):
    res = []
    for ele in seq: 
        if not isinstance(ele, list): 
            res.append(ele)
        return res

#Second way
def find_it(seq):
    return [ele for ele in seq if not isinstance(ele, list)]

#Third way
def find_it(seq):
    for ele in seq: 
        if not isinstance(ele, list): 
            return ele

#Forth way
def find_it(seq):
    for i in seq:
        if not type(i) == int:
            return i

#Sixth way
def find_it(seq):
    res = []
    for i in seq:
        if not type(i) == int:
            res.append(i)
        return res

#Seventh way
def find_it(seq):
    return [i for i in seq if not type(i) == list]


print(find_it(([1,1,2,-2,5,2,4,4,-1,-2,5], -1)))

