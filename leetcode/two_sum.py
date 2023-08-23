from itertools import combinations
nums=[2,7,11,15]
target=9
new_nums=combinations(nums,2)
answer=[]
for char in new_nums:
    if char[0]+char[1]==target:
        answer.append(nums.index(char[0]))
        answer.append(nums.index(char[1]))
print(answer)
