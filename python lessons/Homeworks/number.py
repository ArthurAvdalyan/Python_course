#Տրված է ուղանկյունանիստ а, b կողմերով և h բարձրությունով։ Հաշվել ծավալը
a = 2
b = 3 * a
h = 4 * b

volume = (1/3) * b * h * a
print("The volume is:", volume)

#Տրված է երկու փոփոխական՝ a=4, b=5: a-ին վերագրել b-ի արժեքը, իսկ b-ին a-ի արժեքը։
a = 4
b = 5
a = b
b = a
a = a + b - a
print("a =", a)
print("b =", b)

#Ներմուծել բնական թիվ՝ x=5: Հաշվել նրա քառակուսին և տպել հետևյալ կերպ՝ the squere of 5 is 25:
x = 5
square = x ** 2
print("The square of", x, "is", square)

#Տրված է գունդ r շառավղով։ Հաշվել այդ գնդի ծավալը և մակերեսը, երբ r=1; 
r = 1
volume = (4/3) * 3.14 * r ** 3
surface_area = 4 * 3.14 * r ** 2
print("The volume of the sphere is", volume, "and the surface area is", surface_area)

#Ներմուծելa,b,c բնական թվերը, որոնք քառակուսային հավասարման գործակիցներն են՝ax**2+b*x+c=0:
# Հաշվել հավասարման արմատները տրված գործակիցների համար՝a=1,b=-6,c=8;
a = 1
b = -6
c = 8

discriminant = b ** 2 - 4 * a * c

root1 = (-b + discriminant ** 0.5) / (2 * a)
root2 = (-b - discriminant ** 0.5) / (2 * a)

print("The roots are:", root1, "and", root2)

#Տրված է ուղղանկյուն եռանկյան էջերը, а և b, գտնել նրա ներքնաձիքը
a = 5
b = 7
c = (a ** 2 + b ** 2) ** 0.5
print(c)

#Ներմուծել բնական թիվ՝ N, և ստանալ նրա վերջին թվանշանը։
n = int(input("Enter a number: "))
last_digit = n % 10
print("The last digit of the number is:", last_digit)

#Ներմուծել բնական թիվ՝ N, և ստանալ նրա թվանշանների գումարը և արտադրյալը։
N = int(input("Ներմուծել բնական թիվ՝ "))
sum = 0
product = 1

while N > 0:
    digit = N % 10
    sum += digit
    product *= digit
    N //= 10

print("Թվանշանների գումարը՝", sum)
print("Թվանշանների արտադրյալը",product)