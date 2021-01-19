monday_temperatures=[9.1, 9.7, 7.6]
#rounding 

print(round(monday_temperatures[0]))


for temperature in monday_temperatures:
    print(round(temperature))


#loop goes through all the variables 


#looping through a dictionary 


student_grades={"Marry": 9.1, "Sim": 8.8, "John": 7.5}
#chose what you want to iterate over items keys values

for grades in student_grades.items():
    print(grades)

for grades in student_grades.values():
    print(grades)

for grades in student_grades.keys():
    print(grades)



phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}


for a, b in phone_numbers.items():
    print("%s: %s"%(a,b))

#while loops 

username = ''

while username != "pypy":
    username=input("Enter username: ")

#break and other stuff 

while True:
    username=input("Enter yo name: ")
    if username== "pypy":
        break
    else:
        continue

