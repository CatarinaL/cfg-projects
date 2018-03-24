# -*- coding: utf-8 -*-

names = ["Cat", "João", "Mariza", "Zé"]
names.append("Cátia")
print "How many names are in the list?", len(names)

for whatever in names:
    print whatever

shopping_bag = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in shopping_bag:
    print item
    #iteration number can be found with iter()(?) check pydoc

print "The first item in my list is", shopping_bag[0]
#list comprehensions - "split" lists etc
print "everything in my list after the first ", shopping_bag[1:]

#list of lists
list_lists = [shopping_bag, names]
print list_lists[0][0] #first list (row), first element (column)
