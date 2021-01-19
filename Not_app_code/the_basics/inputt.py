#storithere=input("Enter : ")

#print(storithere)
#input is string

#storithere=int(input("Enter : "))
#now it is int

#user_input=input("Enter your name: ")
#string formatting or whatever

#message = "Hello %s!" %user_input
#print(message)
#message=f"Hello {user_input}!"
#print(message)

name = input("First name: ")
surname= input("Surname: ")
message="Hello %s %s"% (name, surname)
#or use
message=f"Hello {name} the {surname}"
print(message)


def a(s):
    return ("Hi %s"% s)
