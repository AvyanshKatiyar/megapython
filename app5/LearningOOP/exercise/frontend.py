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
#importing Database class from database
from backend import Database
#Database class; database is an (object) instance of Database() class
# and database is sent to init
database=Database()


class Window:
    def __init__(self, window):


        #inheriting from dynamic object vv intresting 
        #takes window as an argument, window is another object from tkinter 
        self.window=window
        self.window.wm_title("BookStore")

        #labels dont need methods
        l1=Label(window, text="Title")
        l1.grid(row=0,column=0)

        l2=Label(window, text="Year")
        l2.grid(row=1,column=0)

        l3=Label(window, text="Author")
        l3.grid(row=0,column=2)

        l4=Label(window, text="ISBN")
        l4.grid(row=1,column=2)
        ####
        #printing in entry widgit
        self.title_value=StringVar()
        self.title=Entry(window,textvariable=self.title_value)
        self.title.grid(row=0,column=1)
        #printing in entry widgit
        self.year_value=StringVar()
        self.year=Entry(window,textvariable=self.year_value)
        self.year.grid(row=1,column=1)
        #printing in entry widgit
        self.author_value=StringVar()
        self.author=Entry(window,textvariable=self.author_value)
        self.author.grid(row=0,column=3)
        #printing in entry widgit
        self.isbn_value=StringVar()
        self.isbn=Entry(window,textvariable=self.isbn_value)
        self.isbn.grid(row=1,column=3)



        #list box
        self.list1=Listbox(self.window, height=6,width=35)
        #list1.grid(row=2, column=0) this wont work as the listbox is very big
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)


        #scroll bar
        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        sb1.configure(command=self.list1.yview)

        #buttons
        b1=Button(window, text="View all", width=12, command=self.view_command)#no brackets after view_command as adding brackets will execute the function and place its value we want to call the function later one
        b1.grid(row=2, column=3)

        b2=Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3=Button(window, text="Add Entry", width=12, command = self.add_entry)#wrapper function
        b3.grid(row=4, column=3)

        b4=Button(window, text="Update", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5=Button(window, text="Delete", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6=Button(window, text="Close", width=12, command=self.window.destroy)
        b6.grid(row=7, column=3)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)
    def get_selected_row(self,event):
        #this is next key op? global var
            
        
        
        try:
            global selected_tuple

            #list1 is the list box
            self.index=self.list1.curselection()[0] #it is a tupple of lists so get 0#startsfrom0
            self.selected_tuple=self.list1.get(self.index)
            self.title.delete(0,END)
            self.title.insert(END, self.selected_tuple[1])
            self.author.delete(0,END)
            self.author.insert(END, self.selected_tuple[2])
            self.year.delete(0,END)
            self.year.insert(END, self.selected_tuple[3])

            self.isbn.delete(0,END)
            self.isbn.insert(END, self.selected_tuple[4])
            return(self.selected_tuple)
        
        #created when click on empty list
        except IndexError:
            pass

    def view_command(self):
        #delete old entries first
        self.list1.delete(0,END)
        for row in database.view():
            #insert has an insert function first place is 0
            # END means after existing rows
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        #title is not a string it is a string var so to het the string value we have to do stringvar.get()
        for row in database.search(self.title_value.get(), self.author_value.get(),self.year_value.get(), self.isbn_value.get()):
            self.list1.insert(END, row)


    def add_entry(self):
        self.list1.delete(0,END)
        database.insert(self.title_value.get(), self.author_value.get(),self.year_value.get(), self.isbn_value.get())
        
        self.list1.insert(END,(self.title_value.get(), self.author_value.get(),self.year_value.get(), self.isbn_value.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        #database.update(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])
        #print(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])
        #aaah the above statement is the static value of the selected tuple we havbev to send the values in the boxes
        database.update(self.selected_tuple[0],self.title_value.get(), self.author_value.get(),self.year_value.get(), self.isbn_value.get())
        

    #creates window
   





#close


window =Tk()
Window(window)
window.mainloop()
