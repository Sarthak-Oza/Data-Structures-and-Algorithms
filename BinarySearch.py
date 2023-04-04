def binary_search(my_list, num):
    start = 0
    end = len(my_list) - 1
    middle = (start + end) // 2

    while my_list[middle] != num:
        if start == middle:
            return -1

        if num < my_list[middle]:
            end = middle

        if num > my_list[middle]:
            start = middle + 1

        middle = (start + end) // 2

    return middle


print(binary_search([1,2,3,4,5,6], 7))
