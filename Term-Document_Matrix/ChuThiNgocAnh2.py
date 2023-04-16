import itertools

file = open("D:/IR/Term-Document_Matrix/index.txt", 'r')
id = {}

for line in file:
    col = line.strip().split()
    key = col[0] 
    val = col[2:]
    id[key] = val 
file.close() 

# id = {
#         'tom': ['d1', 'd4', 'd8', 'd10'],
#         'jerry': ['d1', 'd4', 'd7'],
#         'dog': ['d1', 'd7', 'd11', 'd13'],
#         'cat': ['d2', 'd4', 'd7']
#     }

search = lambda a, id: list(id[a])

search_And = lambda a, b, id: list(filter(lambda x: x in id[a], id[b]))

search_Or = lambda a, b, id: list(set(id[a]) | set(id[b]))

andNot = lambda a, b, id: list(filter(lambda x: x not in id[b], id[a]))

def orNot(a, b, id):

    all_id = list(itertools.chain.from_iterable(id.values()))
    result = list(filter(lambda x: x not in id[b], all_id))
    result.extend(id[a])

    return list(set(result))

# print(id)
print(search("tom", id)) 
print(search_And("on","year",id))
print(search_Or("on","year",id))
print(andNot("on","year",id))
print(orNot("on","year",id))
