mat = []
n = int(input())
for i in range(n):
	temp = list(map(int , input().split()))[:n]
	mat.append(temp)

rCount, cCount = 0, 0

for row in mat:
	_dict = {}
	for item in row:
		if item in _dict.keys():
			rCount += 1
			break
		else:
			_dict[item] = 1

for i in range(n):
	_dict = {}
	for j in range(n):
		if mat[j][i] in _dict.keys():
			cCount += 1
			break
		else:
			_dict[mat[j][i]] = 1


print(rCount, cCount)
