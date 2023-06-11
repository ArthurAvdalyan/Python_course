#Task 1
#Ծրագրի մուտքին տրված է երկու բնական թիվ։ Համեմատել նրանք և տպելարդյունքը
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if int(a) < int(b):
    print(a, "<", b)
elif int(a) > int(b):
    print(a, ">", b)
else:
    print(a, "==", b)

#Task 2
#Մուտքագրել 3 թիվ, a,b,c: Օգտագործելով պայմանի ստուգման և որոշման
#հրամանները, տպել այդ երեք թվից ամենամեծը։ Նույն անել ամենափոքրը
#տպելու համար ևս։

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

print("The largest number is:", max_num)

min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c

print("The smallest number is:", min_num)

#Task 3
#Մուտքագրել որևէ թիվ, և պարզել այն դրական է, բացասական թե հավասար է զրոի։

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is neither positive nor negative")

#Taask 4
#Մուքագրել որևէ բնական թիվ՝ N: Պարզել այն կենտ է թե զույգ, և տպել պատասխանը։

N = int(input("Enter a number: "))

if N % 2 == 0:
    print(N, "is even")
else:
    print(N, "is odd")

#Task 5
#Տրված է ցանկացած բնական թիվ՝ N: Ստուգել արդյոք նա բաժանվում է
#միաժամանակ 5-ի և 7-ի:

N = int(input("Enter a number: "))

# ստուգել եթե թիվը բաժանվում է 5-ի և 7-ի, ապա տպել True, հակառակ դեպքում False
if N % 5 == 0 and N % 7 == 0:
    print(True)
else:
    print(False)