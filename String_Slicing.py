# slicing = create a substring by extracting elements from another string
#           indexing[] or slice ()
#           [start:stop:step]

name = "Kellie Thomsen"
first_name = name[0:6]
last_name = name[7:13]
funky_name = name[0:13:2]
reversed_name = name[0:13:-1]

print(reversed_name)

website = "http://google.com"

slice = slice(7,-4)
print(website[slice])