#Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։
def max_element(list):
    max_element = list[0]
    i = 1
    while i < len(list):
        if list[i] > max_element:
            max_element = list[i]
        i += 1
    return max_element
my_list = [1,2,3,4]
print(max_element(my_list))

#Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։


#Գրեք ֆունկցիա որը տրված ցուցակի բոլոր էլեմենտները բազմապատկելու համար:
def any_list(lst):
    result = 1
    i = 0
    while i < len(lst):
        result *= lst[i]
        i += 1
    return result
my_list = [1,2,3]
print(any_list(my_list))

#Գրեք ֆունկցիա որը տրված ցուցակից՝ 0-րդ, 4-րդ և 5-րդ էլեմենտները հեռացնելուց հետո նոր ցուցակ տպելու համար, որը համարժեք է տվյալ ցանկին:
#def remove(lst):
#    new_lst = []
#    i = 0
#    while i < len(lst):
#        if i != 0 and i != 4 and i != 5:
#           new_lst.append(lst[i])
#           i += 1
#    return new_lst
#lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#new_lst = remove(lst)
#print(new_lst)

#Գրեք ֆունկցիա ցուցակի էլեմենտների հաճախականությունը ստանալու համար
def get_sum(lst):
    i = 0
    list_sum = 0
    while i < len(lst):
        list_sum += lst[i]
        i += 1
    return list_sum
lst = [1,1,2,3,4,4,5,6,7]
print(get_sum(lst))