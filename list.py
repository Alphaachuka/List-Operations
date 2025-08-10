# create an empty list

my_list = []



# append some items to the list

my_list.append("10")
my_list.append("20")
my_list.append("30")
my_list.append("40") 

# insert an item at the second position

my_list.insert(1, "15")

# extend the list with another list

my_list.extend(["50", "60", "70"])

# removing last item from the list

my_list.pop()

# sort the list ascendingly

my_list.sort()

# find the index of an item

index_of_30 = my_list.index("30")

# print the index of the item
print("my_list", my_list)
print(f"Index of '30': {index_of_30}")





