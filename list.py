# ## creating empty list
# ls = []
# ls = list()

# ## coping list
# # wrong
# ls1 = [1,2,3,4]
# ls2 = ls1
# print(ls1[0])
# print(ls2[0])

# ls1[0] = 9
# print(ls1[0])
# print(ls2[0])

# # correct method 1
import copy
l1 = [1,2]
l2 = copy.copy(l1)
# to reverse

# l2.reverse()
# print(l2[::-1])

# # correct method 2
# l1 = [1,2]
# l2 = list(l1)

# enumerate
# for index, value in enumerate(l1):
# 	print(index, value)

# zip
for i, j in zip(l1, l2):
	print(i,j)

# extend
l1 = [1,2,3]
l2 = [4,5,6]
l1.append(l2)
l1 = [1,2,3]
l1.extend(l2)


#1-d
l = [0] * 8


# 2-d 
l = [ [0] * 5 ] * 5