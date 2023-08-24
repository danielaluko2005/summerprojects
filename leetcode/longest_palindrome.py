# Longest Palindrome
word="abccccdd"
# word="ccc"
my_dict={}
for letter in word:
    my_dict[letter]=my_dict.get(letter,0)+1 #counts how many of a letter is in it.

count=0 
odd=0 
for letter,number in my_dict.items():
    if number%2==0:
        count+=number
    else:
        count+=number-1
        odd=1
final=count+odd

print(final)
