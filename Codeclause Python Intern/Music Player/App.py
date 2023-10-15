from tkinter import *
from tkinter import filedialog
from pygame import *
from os import *

root = Tk()
root.geometry('920x670+490+85')
root.resizable(False,False)
root.title("Music Player")
root.configure(bg="#0f1a2b")
init()


def open_folder():
    path = filedialog.askdirectory()
    if path:
        chdir(path)
        songs = listdir(path)
        for i in songs:
            if i.endswith(".mp3"):
                playlist.insert(END,i)

def play_song():
    song = playlist.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    music_name.config(text=song[0:-4])

img1 = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\logo.png")
root.iconphoto(False,img1)

top = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\top.png")
Label(root,image=top,bg="#0f1a2b").pack()

logo = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\logo.png")
Label(root,image=logo,bg="#0f1a2b",activebackground="#0f1a2b").place(x=65,y=115)

music_name = Label(root,text="",font=('arial',15),fg="white",bg="#0f1a2b")
music_name.place(x=150,y=340,anchor='center')

start_img = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\play.png")
Button(root,image=start_img,bg="#0f1a2b",activebackground="#0f1a2b",cursor="hand2",bd=0,command=play_song).place(x=100,y=400)

stop_img = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\stop.png")
Button(root,image=stop_img,bg="#0f1a2b",activebackground="#0f1a2b",cursor="hand2",bd=0,command=mixer.music.stop).place(x=30,y=510)

resume_img = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\resume.png")
Button(root,image=resume_img,bg="#0f1a2b",activebackground="#0f1a2b",cursor="hand2",bd=0,command=mixer.music.unpause).place(x=115,y=510)

pause_img = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\pause.png")
Button(root,image=pause_img,bg="#0f1a2b",activebackground="#0f1a2b",cursor="hand2",bd=0,command=mixer.music.pause).place(x=200,y=510)

menu = PhotoImage(file="E:\\Codeclause Python Intern\\Music Player\\images\\menu.png")
Label(root,image=menu,bg="#0f1a2b",activebackground="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

frame = Frame(root,bd=2,relief=RIDGE,bg="grey")
frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",width=15,fg="black",activeforeground="black",bg="#21b3de",activebackground="#21b3de",cursor="hand2",height=2,font=('arial',10,'bold'),relief=GROOVE,command=open_folder).place(x=330,y=300)

scroll = Scrollbar(frame)
playlist = Listbox(frame,width=100,font=('arial',12),bg='#333333',fg='white',selectbackground="lightblue",selectforeground="black",cursor="hand2",border=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)
    
root.mainloop()
