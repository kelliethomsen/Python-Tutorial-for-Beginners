# nested loop = the "inner loop" will finish all of its interations before finishing one interation of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns: "))
symbol = input("what is your symbol?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
    