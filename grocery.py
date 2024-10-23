groceries = {}

while True:
    try:
        item = input("").upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break

sorted_groceries = [(count, item) for item, count in groceries.items()]
sorted_groceries.sort(key=lambda x: x[1])

for count, item in sorted_groceries:
    print(f"{count} {item}")
