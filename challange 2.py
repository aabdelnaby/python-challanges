# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


#solution

List = list()
test = input()
for test in range(int(test)):
    test = input()
    instruction = test.split(" ")
    if instruction[0] in dir(List) and callable(getattr(List, instruction[0])):
        args = instruction[1:]
        args = list(map(int, args))
        f = getattr(List, instruction[0])
        f(*args)
    else:
        if instruction[0] == "print":
            print(List)