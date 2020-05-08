## declaration
d = dict()
d = {}

## initialization
d = {0: 10, 1: [2, 0]}

## util function
k = list(d.keys())
l = list(d.values())

#iterating over dict
for key, value in d.items():
	print(key, value)

# update
d.update({0: 19})
print(d)
