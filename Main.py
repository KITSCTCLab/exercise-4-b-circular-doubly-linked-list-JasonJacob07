# Read an integer that denotes the the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here

# print(length_of_circular_linked_list)
# print(circular_linked_list)


# final_list = [circular_linked_list[i] for i in range(3)]
# for i in range(5,length_of_circular_linked_list,3):
#     if i == final_list[0]:
#         break
#     final_list.append(circular_linked_list[i])
# if final_list[len(final_list)-1] == final_list[0]:    
#     final_list.pop()

# print(len(final_list))
# for i in final_list:
#     print(i,end=" ")

# final_list = [circular_linked_list[i] for i in range(3)]
# for i in range(5,length_of_circular_linked_list,3):
#     final_list.append(circular_linked_list[i])
# if final_list[len(final_list)-1] == final_list[0]:    
#     final_list.pop()

# print(len(final_list))
# for i in final_list:
#     print(i,end=" ")

final_list = [circular_linked_list[i] for i in range(3)]
for i in circular_linked_list:
    if i not in final_list:
        final_list.append(i)
    
# if final_list[len(final_list)-1] == final_list[0]:    
#     final_list.pop()
print(len(final_list))
for i in final_list:
    print(i,end=" ")
