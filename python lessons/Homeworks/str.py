#Գրել ծրագիր, որը տրված տողային փոփոխականից կստանա նորը,
#կազմված այդ փոփոխականի առաջին երկու և վերջին երկու սիմվոլներից։ Եթե տրված փոփոխականի երկարությունը փոքր է 2֊ից, ապա թող վերադարձնի դատարկ արժեք։
variable = input("Enter a string: ")
if len(variable) < 2:
    print("Empty")
else:
    new_var = variable[0:2] + variable[-2:]
print(new_var)

#Գրել ծրագիր, որը տրված տողային փոփոխականի և բնական n թվի համար,
#կհեռացնի տրված տողային փոփոխականի n-րդ սիմվոլը
string = input("Enter a string: ")
n = int(input("Enter the index of the character to remove: "))

new_string = string[:n] + string[n+1:]

print("New string:", new_string)

#Գրել ծրագիր, որը տրված տողային փոփոխականից կստանա նոր տողային
#փոփոխական առաջին և վերջին սիմվոլները տեղերով փոխելով 
string = input("Enter a string: ")
new_string = string[-1] + string[1:-1] + string[0]
print("New string: ", new_string)

#Գրել ծրագիր, որը տրված տողային փոփոխականից կստանա նոր տողային
#փոփոխական կազմված տրված փոփոխականի վերջին երկու սիմվոլները 4
#անգամ իրար կողքի գրելուց։
string = input("Enter a string: ")
new_string = string[:-2] + string[-2]*4
print("New string:", new_string)

#Գրել ծրագիր, որը տրված float թվի համար(10-ից փոքր), կստանա նրա նրա կրճատ ձևը ստորակետից հետո 2 թվի ճշտությամբ
num = float(input("Enter a number less than 10: "))
rounded_num = int(num * 100) / 100.0
print("Rounded to 2 decimal places: ", rounded_num)