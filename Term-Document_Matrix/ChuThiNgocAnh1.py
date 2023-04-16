import numpy as np


file = open("D:/IR/Term-Document_Matrix/index.txt", 'r')

my_dict = {}

# Lấy dữ liệu trong file index.txt
# Dữ liệu trong file có dạng như sau:
# Num 5 d0 d1 d2 d3 d4 
# a 5 d0 d1 d2 d3 d4 
# accord 1 d3 
# action 1 d4 
# addit 1 d0 

for line in file:
    columns = line.strip().split()
    key = columns[0] 
    values = columns[2:] 
    my_dict[key] = values 
file.close() 
# print(my_dict)

c = {
        'tom': ['d1', 'd4', 'd8', 'd10'],
        'jerry': ['d1', 'd4', 'd7'],
        'dog': ['d1', 'd7', 'd11', 'd13'],
        'cat': ['d2', 'd4', 'd7']
    }

def search(a, my_dict):
    return(my_dict[a])

def Intersection(a,b, my_dict):
    intersection = list(set(my_dict[a]) & set(my_dict[b]))
    intersection.sort
    return intersection

def Union(a, b, my_dict):
    union = list(set(my_dict[a]) | set(my_dict[b]))
    union.sort
    return union
    
def andNot(a, b, my_dict):
    andnot = list(set(my_dict[a]) - set(my_dict[b]))

    return andnot

def orNot(a, b, my_dict):
    ans = []

    for key, value in my_dict.items():
        if key != a and key != b:
            ans.extend(my_dict[key])

    result = list(set(ans) - set(my_dict[b]))
    result.extend(my_dict[a])

    return (list(set(result)))  

print(search("tom", c))
print(Intersection("tom", "jerry", c))
print(Union("tom", "jerry", c))
print(andNot("tom", "jerry",c))
print(orNot("tom", "jerry",c))
