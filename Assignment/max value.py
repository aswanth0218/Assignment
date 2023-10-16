#3.array of num from largest value

from itertools import permutations
array = [54,546,548,60]

# using itertools.permutation() + join() + max()
res = int(max((''.join(i) for i in permutations(str(i)
                     for i in array)), key = int))
print (str(res))