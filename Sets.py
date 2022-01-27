# sets = collection which is unordered, unindexed. No duplicate values.

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

for x in utensils:
    print(x)



utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)


    print(dishes.difference(utensils))
    print(dishes.intersection(utensils))