#this creates a temp object
myfile=open("fruits.txt")
#this is how you read it
a=myfile.read()
print(type(a))
print(myfile.read())
myfile.close()
#cursor moves down after reading once so repeating the read print does not double print the file only prints once

# this is better file is only opened under indentation

with open("fruits.txt") as aa:
    content=aa.read()
print(content)

#different filepaths

with open("lmao/newfroots.txt") as aa:
    content=aa.read()
print(content)



################################################
#writing
