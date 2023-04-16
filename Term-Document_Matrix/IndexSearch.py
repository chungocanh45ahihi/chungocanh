import itertools

file = open("D:/IR/Term-Document_Matrix/index.txt", 'r')
id = {}

for line in file:
    col = line.strip().split()
    key = col[0].replace('-', ' ') 
    val = col[2:]
    id[key] = val 
file.close() 

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
print(search("Num tonn", id)) 
print(search_And("Num","Num tonn",id))
print(search_Or("Num pct","Num tonn",id))
# print(andNot("on","year",id))
# print(orNot("on","year",id))
