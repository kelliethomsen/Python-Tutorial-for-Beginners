# dictioonary = a changeable, unordered collection of unique key:value pairs
#               fast because they use hashing, allow us to access a value quickly
#FIX!


monthconversions = {"Jan":"January",
"Feb":"Feburary",
"Mar":"March",
"Apr":"April"}

for key,value in monthconversions.items():
    print(key,value)

# monthconversions.pop("Feb")
