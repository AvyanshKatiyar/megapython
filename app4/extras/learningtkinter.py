from tkinter import *

#creates window
window =Tk()

def km_to_miles():
    print(e1_value.get())
    
    #e1_value.get() this is a string ok
    miles=float(e1_value.get())*1.6
    #end means ki output mein will keep on adding execute multiple times to figure out
    t1.insert(END,miles)





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
t1.grid(row=0,column=2)

#close program with this function
window.mainloop()