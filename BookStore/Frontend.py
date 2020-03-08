from tkinter import *
from Backend import Database

database = Database("Database.db")
"""
A program that stores this book information:
Title, Author Year, ISBN 
User can: 
View all records
Search an entry
Add entry
Update entry
Delete Close
"""


# Creates a class
class Application(object):

    # Constructor
    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore")

        # Title text
        Title = Label(window, text="Title")
        Title.grid(row=0, column=0)
        self.Title_value = StringVar()
        self.Title_entry = Entry(window, textvariable=self.Title_value)
        self.Title_entry.grid(row=0, column=1)

        # Author text
        Author = Label(window, text="Author")
        Author.grid(row=0, column=2)
        self.Author_value = StringVar()
        self.Author_entry = Entry(window, textvariable=self.Author_value)
        self.Author_entry.grid(row=0, column=3)

        # Year text
        Year = Label(window, text="Year")
        Year.grid(row=1, column=0)
        self.Year_value = StringVar()
        self.Year_entry = Entry(window, textvariable=self.Year_value)
        self.Year_entry.grid(row=1, column=1)

        # ISBN text
        ISBN = Label(window, text="ISBN")
        ISBN.grid(row=1, column=2)
        self.ISBN_value = StringVar()
        self.ISBN_entry = Entry(window, textvariable=self.ISBN_value)
        self.ISBN_entry.grid(row=1, column=3)

        # Buttons
        View_all = Button(window, text="View all", height=1, width=15, command=self.view_command)
        View_all.grid(row=2, column=3)

        Search_Entry = Button(window, text="Search entry", height=1, width=15, command=self.search_command)
        Search_Entry.grid(row=3, column=3)

        Add_Entry = Button(window, text="Add entry", height=1, width=15, command=self.add_command)
        Add_Entry.grid(row=4, column=3)

        Update_Selected = Button(window, text="Update Selected", height=1, width=15, command=self.update_command)
        Update_Selected.grid(row=5, column=3)

        Delete_Selected = Button(window, text="Delete Selected", height=1, width=15, command=self.delete_command)
        Delete_Selected.grid(row=6, column=3)

        Close = Button(window, text="Close", command=self.window.quit, height=1, width=15)
        Close.grid(row=7, column=3)

        # Scrollbar
        scrollbar = Scrollbar(window)
        scrollbar.grid(row=2, column=2)

        # Listbox
        self.listbox = Listbox(window, height=6, width=35)
        self.listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.listbox.bind("<<ListboxSelect>>", self.get_selected_row)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)

    def view_command(self):
        self.listbox.delete(0, END)
        for row in database.view():
            self.listbox.insert(END, row)

    def search_command(self):
        self.listbox.delete(0, END)
        for row in database.search(self.Title_value.get(), self.Author_value.get(),
                                   self.Year_value.get(), self.ISBN_value.get()):
            self.listbox.insert(END, row)

    def add_command(self):
        database.insert(self.Title_value.get(), self.Author_value.get(),
                        self.Year_value.get(), self.ISBN_value.get())
        self.listbox.delete(0, END)
        self.listbox.insert(END, (self.Title_value.get(), self.Author_value.get(),
                                  self.Year_value.get(), self.ISBN_value.get()))

    def get_selected_row(self, event):
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
            self.Title_entry.delete(0, END)
            self.Title_entry.insert(END, self.selected_tuple[1])
            self.Author_entry.delete(0, END)
            self.Author_entry.insert(END, self.selected_tuple[2])
            self.Year_entry.delete(0, END)
            self.Year_entry.insert(END, self.selected_tuple[3])
            self.ISBN_entry.delete(0, END)
            self.ISBN_entry.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def update_command(self):
        database.update(self.selected_tuple[0], self.Title_value.get(), self.Author_value.get(),
                        self.Year_value.get(), self.ISBN_value.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])


window = Tk()

Application(window)
window.mainloop()
