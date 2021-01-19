from tkinter import *

#creates window
window =Tk()

def km_to_miles():
    print(e1_value.get())
    
    #e1_value.get() this is a string ok
    kg=float(e1_value.get())
    #end means ki output mein will keep on adding execute multiple times to figure out
    t1.insert(END,kg*1000)
    t2.insert(END,kg*2.2046200)
    t3.insert(END,kg*35.274)






#COMMAND FOR FUNCTION

b1=Button(window, text="Execute",command=km_to_miles)
#this places the button
#b1.pack()
# however grid used as more control

b1.grid(row=0,column=0)

#peinting in entry widgit

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=3)

#close program with this function
window.mainloop()