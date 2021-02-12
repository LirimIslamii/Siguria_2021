from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import time as tm

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
   text_input = tm.strftime("%H:%M:%S")


window = Tk()
window.title("Siguri 2021©")
icon = PhotoImage(file = "C:\\Users\\DELL\\Desktop\\New folder\\k.png")
window.iconphoto(False,icon)
canvas = Canvas(window,width=500, height=300)
canvas.pack(fill="both", expand=True)
label = Label(canvas, text="Spam")
label.place(relx = 0.0, rely =1.0, anchor='sw')
my_image = ImageTk.PhotoImage(file="C:\\Users\\DELL\\Desktop\\New folder\\j.jpg")
canvas.create_image(0,0,anchor=NW,image=my_image)
menubar = Menu(window)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=hap)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)

view = Menu(menubar, tearoff=0)
view.add_command(label="Zoom In")
view.add_command(label="Zoom Out")
view.add_command(label="Show Time",command=show)
menubar.add_cascade(label="View", menu=view)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...",command=ndihma)
menubar.add_cascade(label="Help", menu=helpmenu)



window.config(menu=menubar)
window.bind('<Configure>',resize) #funksioni Resize
window.mainloop()
