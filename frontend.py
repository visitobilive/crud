
'''
A program to store this book informaion
TiTle, Author
year, ISBN

user can
view all records
search enrty
Add entry
update
Delete
close
'''
# import Tkinter  as tk
from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    print (selected_tuple)
    print(index)
    entry1.delete(0, END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)
#check author_text and year_text
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get()
            , author_text.get()
            ,year_text.get()
            , isbn_text.get()):
        list1.insert(END, row)

def add_command():

    row = title_text.get(),author_text.get(),\
          year_text.get(),isbn_text.get()
    backend.insert(title_text.get(),
                   author_text.get()
                   ,year_text.get()
                   ,isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, row)
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0,END)
    entry4.delete(0,END)



def delete_command():
    backend.delete(selected_tuple[0])
# view_command()

def update_command():
    backend.update(selected_tuple[0],
                   title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get())
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)



window =Tk()

window.wm_title("Book store")

label1 = Label(window, text ='Title')
label1.grid(row = 0, column =0)
# creating the container that will hold string value data type for Entry
title_text = StringVar()
entry1 = Entry(window,
               textvariable=title_text)
entry1.grid(row = 0, column =1)


label2 = Label(window, text ='Author')
label2.grid(row = 0, column =2)

author_text = StringVar()
entry2 = Entry(window,
               textvariable=author_text)
entry2.grid(row = 1, column =1)


label3 = Label(window, text ='Year')
label3.grid(row = 1, column =0)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row = 0, column =3)


label4 = Label(window, text ='ISBN')
label4.grid(row = 1, column =2)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row = 1, column =3)

# creating listbox

list1 = Listbox(window, height=6, width=35)
list1.grid(row = 2, column =0,
           rowspan=6, columnspan=2)
# creating scrollbar
scroll_bar= Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)
# to add the scroll bar object to
# the list use configure object
list1.configure(yscrollcommand =
                scroll_bar.set)
scroll_bar.configure(command = list1.yview)

#
list1.bind('<<ListboxSelect>>',
           get_selected_row)

# creating button
btn1 = Button(window, text="view all",
              width=13, command=view_command)
btn1.grid(row=2, column =3)

btn2 = Button(window, text="Search Entry",
              width=13, command=search_command)
btn2.grid(row=3, column =3)

btn3 = Button(window, text="Add Entry",
              width=13, command=add_command)
btn3.grid(row=4, column =3)

btn4 = Button(window, text="update", width=13, command=update_command)
btn4.grid(row=5, column =3)

btn5 = Button(window, text="Delete", width=13, command=delete_command)
btn5.grid(row=6, column =3)

btn6 = Button(window, text="Close",
              width=13,
              command=window.destroy)
btn6.grid(row=7, column =3)

window.mainloop()



