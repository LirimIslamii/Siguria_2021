import os
import sys
import subprocess
from tkinter import *
from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
from tkinter import Text
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import time
from tkinter import Entry


def hap():
    try:
        filename = askopenfile(mode='r',filetypes=[("Files","*.txt")])
        content = filename.read()
        messagebox.showinfo("Connected",content)
    except:
        messagebox.showerror("Error","Ju Lutem Specifikoni nje Program!")
def ndihma():
    messagebox.showinfo("Kontribues","\n".join(["Lirim Islami©","Uran Lajqi©","Jon Rexhbogaj©"]))


def resize(e):
    global image1, resizer,image2
    image1 = Image.open("C:\\Users\\DELL\\Desktop\\New folder\\j.jpg")
    resizer = image1.resize((e.width,e.height), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resizer)
    canvas.create_image(0,0,anchor=NW,image=image2)

def show():
    newWindow = Toplevel(window)
    newWindow.title("Timer")
    newWindow.geometry("200x150")
    newWindow.resizable(0,0)
    hour=IntVar()
    minute=IntVar()
    second=IntVar()
    hour.set("00")
    minute.set("00")
    second.set("00")
    hourEntry= Entry(newWindow, width=3, font=("Arial",18,""),
                     textvariable=hour)
    hourEntry.place(x=20,y=20)

    minuteEntry= Entry(newWindow, width=3, font=("Arial",18,""),
                       textvariable=minute)
    minuteEntry.place(x=80,y=20)

    secondEntry= Entry(newWindow, width=3, font=("Arial",18,""),
                       textvariable=second)
    secondEntry.place(x=140,y=20)


    def submit():
        try:
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            while temp >-1:
                mins,secs = divmod(temp,60)
                hours=0
                if mins >60:
                    hours, mins = divmod(mins, 60)
                hour.set("{00:2d}".format(hours))
                minute.set("{00:2d}".format(mins))
                second.set("{00:2d}".format(secs))
                newWindow.update()
                time.sleep(1)
                if (temp == 00):
                    a = messagebox.askquestion("Timer", "Dritarja Kryesore do te mbyllet pas 4 sekondas! Deshironi ta mbyllni?")
                    newWindow.destroy()
                    if a == "yes":
                        window.after(4000,lambda:window.destroy())
                temp -= 1
        except:
            messagebox.showerror("Error","Ju lutem shenoni vetem numra!")



    btn = Button(newWindow, text='Timer',bg="blue",bd="5",command=submit)
    btn.place(relx=0.5,rely=0.7, anchor="center")

def Expand_In():
    width  = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(f'{width}x{height}+0+0')

def Expand_Out():
    width  = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    f = window.geometry('%sx%s' % (int(width/2.56), int(height/2.4)))

def struktura():
    global f,path
    f=Toplevel(window)
    f.geometry("300x200")
    f.resizable(0,0)

    tv=Treeview(f,show='tree')
    ybar=Scrollbar(f,orient=VERTICAL,command=tv.yview)
    tv.configure(yscroll=ybar.set)

    path = sys.executable
    directory = path.split('\\')[0]

    tv.heading('#0',text='Dir：'+directory,anchor='w')
    path=os.path.abspath(directory)
    node=tv.insert('','end',text=path,open=True)

    def traverse_dir(parent,path):
        if os.access(directory,os.X_OK):
            for d in os.listdir(path):
                full_path=os.path.join(path,d)
                isdir = os.path.isdir(full_path)
                id=tv.insert(parent,'end',text=d,open=False)
                try:
                    if isdir:
                        traverse_dir(id,full_path)
                except PermissionError:
                    print("PermissionError in file: " + full_path)
                except:
                    print("Something else went wrong")

    traverse_dir(node,path)
    ybar.pack(side=RIGHT,fill=Y)
    tv.pack()

def open():
    global inter
    inter = Toplevel(window)
    inter.title("Notepad")
    menubar = Menu(inter)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save as...")
    menubar.add_cascade(label="File", menu=filemenu)
    inter.config(menu=menubar)
    inter.minsize(height=250, width=350)
    inter.resizable(0,0)
    scrollbar = Scrollbar(inter)
    scrollbar.pack(side=RIGHT,fill=Y)
    text_info = Text(inter, yscrollcommand=scrollbar.set)
    text_info.pack(fill=BOTH)
    scrollbar.config(command=text_info.yview)
    inter.mainloop()


def hiqe():
    try:
        if f.winfo_exists():
            f.destroy()
        if inter.winfo_exists():
            inter.destroy()
    except:
        messagebox.showerror("Error","Nuk eshte e hapur asnje dritare!")

def help():
    global help
    help = Toplevel(window,bg='#ccffcc')
    help.geometry("300x300")
    help.title("Help Index")
    help.resizable(0,0)
    label = Label(help,text="Hello",bg="#ccffcc",font=("Perpetua",12))
    label.pack()
    help.mainloop()

window = Tk()
window.title("Siguri 2021©")
icon = PhotoImage(file = "C:\\Users\\DELL\\Desktop\\New folder\\k.png")
window.iconphoto(False,icon)
canvas = Canvas(window,width=500, height=300)
canvas.pack(fill="both", expand=True)
my_image = ImageTk.PhotoImage(file="C:\\Users\\DELL\\Desktop\\New folder\\j.jpg")
canvas.create_image(0,0,anchor=NW,image=my_image)
menubar = Menu(window)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=open)
filemenu.add_command(label="Open",command=struktura)
filemenu.add_command(label="Close",command=hiqe)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)


view = Menu(menubar, tearoff=0)
view.add_command(label="Expand In", command=Expand_In)
view.add_command(label="Expand Out",command=Expand_Out)
view.add_command(label="Clock Timer",command=show)
menubar.add_cascade(label="View", menu=view)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
helpmenu.add_command(label="About...",command=ndihma)
menubar.add_cascade(label="Help", menu=helpmenu)




window.config(menu=menubar)
window.bind('<Configure>',resize) #funksioni Resize
window.mainloop()
