# Binary search

def binary_search(my_list,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(my_list)-1
    mid_point=(low+high)//2
    if high<low:
        return f"{target} isn't in the list"
    if my_list[mid_point]==target:
        return f'{target} is located at index {mid_point}'
    elif target>my_list[mid_point]:
        return binary_search(my_list,target,low=mid_point+1,high=high)
    elif target<my_list[mid_point]:
        return binary_search(my_list,target,low=low,high=mid_point-1)
    

my_list=[1,2,3,4,5,6,7,8,9,10]
my_func=binary_search(my_list,7)
print(my_func)