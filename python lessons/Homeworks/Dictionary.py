#Write a python programm, which add a new value with given key in dict.
my_dict = {'home':'white',"door":"open","color":"red"}
my_dict["work"] = "dictionary"
print(my_dict)

#Write a python program which concat 2 dicts
dict1 = {'our': "homework", 'is': "good"}
dict2 = {'that': "was", 'good': "homework"}
connected_dict = dict()
for key, value in dict1.items():
    connected_dict[key] = value
for key, value in dict2.items():
    connected_dict[key] = value
print(connected_dict)

#Write a python programm, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers
def create_dict(num):
    my_dict = {}
    for i in range(1, num+1):
        my_dict[i] = i**3
    return my_dict
number = int(input("Enter a number: "))
my_dict = create_dict(number)
print(my_dict)

#Write a python programm which create dict from 2 lists with the same length
def  new_dict(list1, list2):
    if len(list1) != len(list2):
        return "Error,same length"
    else:
        my_dict = {}
    for i in range(len(list1)):
        my_dict[list1[i]] = list2[i]
    return my_dict
list1 = ["home","door","dog","cat"]
list2 = ["car","home","branche","cat"]
my_dict = new_dict(list1,list2)
print(my_dict)

#Write a python programm which get the maximum and minimum values of dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 0,'d':4}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Maximum value in dictionary:", max_value)
print("Minimum value in dictionary:", min_value)

#Write a python programm which combine 2 dictionaries into one, if there is an elements with the same key, appropriate element of combined dict will be element with that key, and sum of values as value.
def comb_dicts(d1, d2):
    result = dict(d1)
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
d1 = {"first":10,"second":14,"third":5}
d2 = {"first":7,"third":9,"fourth":5}
print(comb_dicts(d1,d2))


def create_dict(string):
    new_keys = {}
    for i in string:
        if i in new_keys:
            new_keys[i] += 1
        else:
            new_keys[i] = 1
    return new_keys
string = "hello world"
print(create_dict(string))
