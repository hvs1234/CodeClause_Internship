from tkinter import *
from pyshorteners import *

root = Tk()
root.resizable(False,False)
root.title('Url Shortener')
root.geometry('500x500+580+180')
root.configure(bg='lightgrey')

def shorten():
    if shorten_entry.get():
        shorten_entry.delete(0,END)
    if enter_link.get():
        url = Shortener().tinyurl.short(enter_link.get())
        shorten_entry.insert(END,url)

img1 = PhotoImage(file="E:\\pyImages\\cyber.png")
root.iconphoto(False,img1)

heading = Label(root,text='Enter Original Link To Shorten',font=('Algerian',20),background='lightgrey',foreground="black")
heading.pack(pady=20)

enter_link = Entry(root,background="lightgrey",foreground="darkred",font=('Calibri',20),bd=4,justify=CENTER)
enter_link.pack(pady=20)

shorten_button = Button(root,text="Shorten Link",command=shorten,font=('Cambria',24),foreground="darkblue",background="lightgrey",bd=2,activebackground="lightgrey",cursor="hand2",relief="sunken",activeforeground="darkgreen")
shorten_button.pack(pady=20)

shorten_label = Label(root,text="Shorten Link Here . . .",font=('Cambria',18),background="lightgrey")
shorten_label.pack(pady=50)

shorten_entry = Entry(root,font=("Calibri",22),justify=CENTER,background="lightgrey",border=0,foreground="black",width=30)
shorten_entry.pack(pady=10)
root.mainloop()