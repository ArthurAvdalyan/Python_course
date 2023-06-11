#Write a python programm which return given list without duplicates.
myList = [1, 2, 3, 2, 4, 3, 5, 6, 5]
myList = list(set(myList))
print(myList)

#Write a python programm which return common elements of 2 lists.
def same_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4, 6, 8, 10, 12]
print(same_elements(list1, list2))

#Write a python programm which return elements are or in first list, either in second, but not in both
def unique(list1, list2):
    result = []
    for element in list1:
        if element not in list2:
            result.append(element)
    for element in list2:
        if element not in list1:
            result.append(element)
    return result
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
print(unique(list1, list2))

#Write  python function which get set and element value, and remove from set element with given value if exist
def remove_set(my_set, element):
    if element in my_set:
        my_set.remove(element)
        print(f"{element} removed from set.\nNew set: {my_set}")
    else:
        print(f"{element} not in set.")
my_set = {1, 2, 3, 4}
remove_set(my_set, 3)

#Write a python python program, which return list from given set, where each element of list, is equal to cub of set element
def cube_list(my_set):
    input_list = []
    for element in my_set:
        input_list.append(element ** 3)
    return input_list
given_set = {1,2,3}
given_list = cube_list(given_set)
print(given_list)

#Write a python programm which return elements which are or in first, either in second, or in both
def same(first, second):
    combined = set(first) | set(second)
    return list(combined)
first_list = [1,2,3]
second_list = [2,3,4]
print(same(first_list,second_list))
