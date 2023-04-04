# def bubble_sort(my_list):
#     for i in range(len(my_list)-1):
#         for j in range(len(my_list)-i-1):
#             if my_list[j] > my_list[j+1]:
#
#                 my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#
#     return my_list
#
#
# print(bubble_sort([5,3,2,1,6]))

# def selection_sort(my_list):
#     for i in range(len(my_list)):
#         min_index = i
#         for j in range(i+1, len(my_list)):
#             if my_list[j] < my_list[min_index]:
#                 my_list[j], my_list[min_index] = my_list[min_index], my_list[j]
#
#     return my_list
#
#
# print(selection_sort([4,2,5,1,6,3]))

# def insertion_sort(my_list):
#     for i in range(1,len(my_list)):
#         key = my_list[i]
#         j = i-1
#         while j >= 0 and key < my_list[j]:
#             my_list[j+1] = my_list[j]
#             j -= 1
#
#         my_list[j+1] = key
#     return my_list
#
#
# print(insertion_sort([4,2,5,1,6,3]))

# def partition(list1, left, right):
#     i = left
#     j = right - 1
#     pivot = list1[right]
#
#     while i < j:
#         while list1[i] < pivot and i <= right:
#             i += 1
#         while list1[j] > pivot and j >= left:
#             j -= 1
#
#         if i < j:
#             list1[i],list1[j] = list1[j],list1[i]
#
#     if j <= i:
#         list1[i], list1[right] = list1[right],list1[i]
#
#     return i
#
#
# def quick_sort(list1, left, right):
#     if left < right:
#         partition_point = partition(list1, left, right)
#         quick_sort(list1, left, partition_point-1)
#         quick_sort(list1,partition_point+1,right)
#
#
# arr1 = [22,11,88,66,55,77,33,44]
#
# quick_sort(arr1, 0, 7)
# print(arr1)


# def heapify(list1, list1_len, index):
#     root_index = index
#     left_index = (root_index*2) + 1
#     right_index = (root_index*2) + 2
#
#     if left_index < list1_len and list1[left_index] < list1[root_index]:
#         root_index = left_index
#
#     if right_index < list1_len and list1[right_index] < list1[root_index]:
#         root_index = right_index
#
#     if root_index != index:
#         list1[index], list1[root_index] = list1[root_index], list1[index]
#         heapify(list1, list1_len, root_index)
#
#
# def heap_sort(list1):
#     list1_len = len(list1)
#     for i in range((list1_len//2)//2, -1, -1):
#         heapify(list1, list1_len, i)
#
#     for i in range(list1_len-1, 0, -1):
#         list1[i], list1[0] = list1[0], list1[i]
#         heapify(list1, i , 0) # used i here so it will not consider the last element in heapify as it will do < len .

import math

def bubble_sort(list1):
    no_of_buckets = round(math.sqrt(len(list1)))
    max_no = max(list1)
    bucket_list = []

    for i in range(no_of_buckets):
        bucket_list.append([])

    for i in list1:
        index = math.ceil((i*no_of_buckets)/max_no) - 1
        bucket_list[index].append(i)

    for bucket in bucket_list:

            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1

                while j >= 0 and key < bucket[j]:
                    bucket[j+1] = bucket[j]
                    j -= 1

                bucket[j+1] = key
    k = 0
    for bucket in bucket_list:
        for element in bucket:
            list1[k] = element
            k += 1


list1 = [7,5,2,3,1,4,9,8,6]
bubble_sort(list1)
print(list1)















