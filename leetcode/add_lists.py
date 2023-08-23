# Add a list.

import copy
total_list=[]
first_list=[1,2,3,9]
second_list=[1,2,1,1,9,1,1,1,1,1,1,1,1,1,1,1]
print(len(second_list))
total_list.append(first_list)
total_list.append(second_list)

length_of_lists=[]
for my_list in total_list:
    length_of_lists.append(len(my_list))
highest_length=max(length_of_lists)

for my_list in total_list:
    if len(my_list)<highest_length:
        increment=1
        while len(my_list)<highest_length:
            increment=len(my_list)+increment
            my_list.insert(increment,0)
            
final_answer=[]

index=0
remainder=0
for index in range(highest_length):
    index_answer=0
    for char in total_list:
        index_answer=char[index]+index_answer+remainder
        remainder=0
        if index_answer>9:
            new_index_answer=copy.deepcopy(index_answer)
            index_answer=str(index_answer)
            index_answer,remainder=index_answer[1],index_answer[0]
            index_answer,remainder=int(index_answer),int(remainder)

    final_answer.append(index_answer)
final_answer=tuple(final_answer[::-1])
print(final_answer)
print(len(final_answer))
