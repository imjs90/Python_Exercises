# find replicated values
my_list = [1,1,1,2,3]
#a = [i for i in my_list if my_list.count(i) == 1]

unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
