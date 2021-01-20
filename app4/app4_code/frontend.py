"""
A program that stores this book information:
Title, Author
Year, ISBN

User can: 
View all records
Search an Entry
Add Entry
Update Entry
Delete
Close
"""
# pyinstaller --onefile -windowed frontend.py 
###############

from tkinter import *
#another script
import backend

def get_selected_row(event):
    #this is next key op? global var
    try:
        global selected_tuple


        index=list1.curselection()[0] #it is tupple so get 0#startsfrom0
        selected_tuple=list1.get(index)
        title.delete(0,END)
        title.insert(END, selected_tuple[1])
        author.delete(0,END)
        author.insert(END, selected_tuple[2])
        year.delete(0,END)
        year.insert(END, selected_tuple[3])

        isbn.delete(0,END)
        isbn.insert(END, selected_tuple[4])
        return(selected_tuple)
    except IndexError:
        pass

def view_command():
    #delete old entries first
    list1.delete(0,END)
    for row in backend.view():
        #insert has an insert function first place is 0
        # END means after existing rows
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    #title is not a string it is a string var so to het the string value we have to do stringvar.get()
    for row in backend.search(title_value.get(), author_value.get(),year_value.get(), isbn_value.get()):
        list1.insert(END, row)


def add_entry():
    list1.delete(0,END)
    backend.insert(title_value.get(), author_value.get(),year_value.get(), isbn_value.get())
    
    list1.insert(END,(title_value.get(), author_value.get(),year_value.get(), isbn_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    #backend.update(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])
    #print(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])
    #aaah the above statement is the static value of the selected tuple we havbev to send the values in the boxes
    backend.update(selected_tuple[0],title_value.get(), author_value.get(),year_value.get(), isbn_value.get())
    

#creates window
window =Tk()

window.wm_title("Bookstore")


l1=Label(window, text="Title")
l1.grid(row=0,column=0)

l2=Label(window, text="Year")
l2.grid(row=1,column=0)

l3=Label(window, text="Author")
l3.grid(row=0,column=2)

l4=Label(window, text="ISBN")
l4.grid(row=1,column=2)
####
#peinting in entry widgit
title_value=StringVar()
title=Entry(window,textvariable=title_value)
title.grid(row=0,column=1)
#peinting in entry widgit
year_value=StringVar()
year=Entry(window,textvariable=year_value)
year.grid(row=1,column=1)
#peinting in entry widgit
author_value=StringVar()
author=Entry(window,textvariable=author_value)
author.grid(row=0,column=3)
#peinting in entry widgit
isbn_value=StringVar()
isbn=Entry(window,textvariable=isbn_value)
isbn.grid(row=1,column=3)



#list box
list1=Listbox(window, height=6,width=35)
#list1.grid(row=2, column=0) this wont work as the listbox is very big
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


#scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
sb1.configure(command=list1.yview)

#buttons
b1=Button(window, text="View all", width=12, command=view_command)#no brackets after view_command as adding brackets will execute the function and place its value we want to call the function later one
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command = add_entry)#wrapper function
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

list1.bind('<<ListboxSelect>>', get_selected_row)
#close
window.mainloop()
