temp = [100, 202, 302]
#We have to divide by 10 

new_temp=[temp/10 for temp in temp]
print(new_temp)

#list comprehension with if conditionals

hello=[100, 3323, 3434, 5345]

new_hello=[a/10 for a in hello if a != 3323]

print(new_hello)  


#with else
new_hello=[a/10  if a != 3323 else 0 for a in hello ]
print(new_hello)  
#positional and non positional arguments
#non default and default parameters
#def function(a,b)
#basicall function(4,5)==function(a=4,b=5)==function(b=5,a=4)
# also def function(a=3,b) would mean
#function(5) is same as function(3,5) ok and function(2,3) overwrites the earlier value of a=3 in the function
# non default arguments follow defaualt arguments

#####################################
#Multiple args 

def mean(*args):
    return sum(args)/len(args)

print(mean(1,2,3,4))
#note args is a tupple of idefinite length can not take keyword arguments mean(z=1, 1 ,3) does not workk

#keyword arguments

def meana(**kwargs):
    return kwargs

meana(x=1,a=2,c=3)

#here kwargs is a dictionary