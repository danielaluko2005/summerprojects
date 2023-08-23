# Count how many numbers are smaller than an object in a list

my_list=[8,1,2,2,3]
answer=[]

for char in my_list:
    checker=0
    for index in range(len(my_list)):
        if char>my_list[index]:
            checker+=1
    answer.append(checker)
print(answer)