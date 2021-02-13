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

def help():
    global help
    help = Toplevel(window,bg='#ccffcc')
    help.geometry("500x80")
    help.title("Help Index")
    help.resizable(0,0)
    label = Label(help,text="Shiko linkun \n https://github.com/LirimIslamii/Siguria_2021/blob/main/README.m \n informacionet rreth programit dhe rreth krijimit të tij!",bg="#ccffcc",font=("Perpetua",12))
    label.pack()
    help.mainloop()


def jep():
    global inter
    inter = Toplevel(window)
    inter.title("Notepad")
    #save dhe save as
    global open_status_name
    open_status_name = False

    global selected
    selected = False

    # Ruaje si fajll
    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File",
                    filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
        if text_file:
            name = text_file
            name = name.replace("C:/gui/", "")
            window.title(f'{name} - Success!')

            # Ruan fajllin
            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))
            # Mbyll fajllin
            text_file.close()

    # Ruaje fajllin
    def save_file():
        global open_status_name
        if open_status_name:
            # Ruaje fajllin
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))
            # Mbyll fajllin
            text_file.close()
            # Rivendose emrin
            name = open_status_name
            window.title(f'{name} - Text Fajlli!')
        else:
            save_as_file()

    my_text = Text(inter, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black")
    my_text.pack()

    # Krijo menu-ne
    my_menu = Menu(inter)
    inter.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As...", command=save_as_file)


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
filemenu.add_command(label="New", command=jep)
filemenu.add_command(label="Open",command=struktura)
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
