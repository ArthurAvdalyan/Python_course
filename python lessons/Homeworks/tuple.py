#Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում է ստացած արժեքը tuple մեջ։
#solve it python

def add_to_tuple(tup, val):
    new_tup = tuple(list(tup) + [val])
    return new_tup

my_tuple = (1, 2, 3)
my_object = "hello"
new_tuple = add_to_tuple(my_tuple, my_object)

print(new_tuple)

#Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuple֊ի x էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
#solve it python

def tuple_to_string(t):
    s = ""
    for i in range(len(t)):
        if i == len(t)-1:
            s += str(t[i])
        else:
            s += str(t[i]) + "-"
        return s

sample_tuple = ('hello', 'world', 'python')
result_string = tuple_to_string(sample_tuple)
print(result_string)

#Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։ Խնդիրը լուծել  իտերատիվ մեթոդներով։
#solve it python

#def fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)
#
#n = int(input("Enter a natural number: "))
#print("The", n, "th element of Fibonacci sequence is:", fibonacci(n))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

num = int(input("Enter a number: "))
result = fibonacci(num)

print("The", num, "th Fibonacci number is:", result)

#Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝ ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:
def deleteDigit(n):
    n_str = str(n)
    largest = 0
    for i in range(len(n_str)):
        new_num = int(n_str[:i] + n_str[i+1:])
        if new_num > largest:
            largest = new_num
    return largest

print(deleteDigit(452))

#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky 
# if the sum of the first half of the digits is equal to the sum of the second half. Given a ticket number n, determine if it’s lucky or not.
def my_count(n_len):
    n_len = len(n_str)
    if n_len % 2 != 0: 
        return (False)
    half_len = n_len // 2
    first_half_sum = sum([int(x) for x in n_str[:half_len]])
    second_half_sum = sum([int(x) for x in n_str[half_len:]])
    return (first_half_sum == second_half_sum)
print()