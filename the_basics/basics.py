import datetime
# datetime
datetime.datetime.now()
print("The date and time is:")
print(datetime.datetime.now())

# iteractive shell gives different thoda idk y dont ask
# use print in interactive shell to get print
#single line

print("The date and time is:", datetime.datetime.now())

#using a variable to print
#numbers cant be used in variable names 


##################################################################################

# Python string addition leads to concatenation

x=2
y='10'

print(x+x,y+y)
print(type(x), type(y))
##################################################################################

#list type

student_grades =[9.1,8.8,7.5]
#10 is not included
a=list(range(1,10))
a=list(range(1,10,2))

#can contain different types as well
temperatures = [2.1, 1,'a']
#bruh list can contain another list as well
rainfall = [1.2, 1,'a',[1,2,3]]
##################################################################################

#dir METODS

#dir gives method on datatypes forexample
# dir(str)

# help(type.attribute) attributes come from dir

a='hello'
a.upper()
print(a.upper())
##################################################################################
#BUILT IN FUNCTIONS

#average of grades

student_grades =[2.3, 3.3,10.1]
#dir(__builtins__)

mysum = sum(student_grades)
length= len(student_grades)

mean= mysum/length

print(mean)

##################################################################################

#dictionary 

student_dic ={"Marry": 9.1, "Sim": 8.8,"John": 7.5}
#pairs of keys and values
#dir(dict)

print(student_dic.values())

print(sum(student_dic.values())/len(student_dic.values()))
##################################################################################
# tupples are immutable 
#lists are not immutable 
# tuple in tuple color_codes=((1,2,3),(1,2),(3,2) )
monday_temperatures=(1,2,3)
monday_hi=[1,2,3]
monday_hi.append(2)
monday_hi.remove(1)
##################################################################################

#more on lists
#clear
#append
#index
#__getitem__ shortcut list[]

#slice list[1:4] returns another list and contains items from indices 1 2 3 not 4 index as the upper index
#is never included in python same as range
#list[:4] first item to4th index list[2:] 2nd index to the list
#negative index list[-1] gives the last index
#negative slice to get last 2 list[-2:]

#works on strings as well
mystring='hello'
mystring[:3]
newstrlist=["abcd",1,3,4]
newstrlist[0][1:]
##################################################################################
#dictionaries more

student_grades=["Marry":1,"Sim":8.8,"john":1]
student_grades["Marry"]

#tuple tolist
#list to tuple
#list to dictionary




