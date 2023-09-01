colors = ["Green", "Blue", "Black", "White", "Red", "Blue"]
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[0])
print(colors[-1])
print(colors[-2])

print(colors[1:4]) # khode 4 ro nemide
print(colors[:3]) #az ebbteda ta 3 vali 3 nist
print(colors[1:]) # 1 ta akhar
print(colors[1:-2])

colors[1] = "Yellow"

print(len(colors))
colors.extend(["Orange", "Gray"])
print(colors)

colors.append("Orange") # yedoone be akhar ezafe mikone
print(colors)

colors.insert(2, "Pink") #mizare pink ro rooye index 2
print(colors)
colors.remove("Blue") #Blue aval o pak mikone
#colors.clear() # list ro khali mikone

print(colors.index("Black"))
print(colors.count("Orange"))
print(colors)

colors_sorted = sorted(colors)
print(colors)
print(colors_sorted)

# del colors    delete mikonad

colors.reverse()
print(colors)
