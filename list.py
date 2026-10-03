#about list 
print(" welcome learning about python ")
# list is the collection of element 
item1 = "bru"
item2 = "milk"
item3 = "sugar"
items = ["bru","sugar","milk","tea powder","biscate","rusk"]
print(item1,item2,item3)
print(items)  
items.pop()
print(items)
items.pop(0)
print(items)
items.append("mom's magic")
print(items)
print(items[1:3])
items.insert(2,"bun")
print(items)
items[0] = "coffee powder"
print(items)
print(len(items))
print(sorted(items))
items.clear()
print(items)
