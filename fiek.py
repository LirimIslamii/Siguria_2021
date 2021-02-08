from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile

def hap():
    try:
        filename = askopenfile(mode='r',filetypes=[("Files","*.txt")])
        content = filename.read()
        messagebox.showinfo("Connected",content)
    except:
        messagebox.showerror("Error","Ju Lutem Specifikoni nje Program!")
def ndihma():
    messagebox.showinfo("Kontribues","\n".join(["Lirim Islami©","Uran Lajqi©","Jon Rexhbogaj©"]))


window = Tk()
window.title("Connecting...")
window.geometry('510x290')
C = Canvas(window, bg="blue", height=250, width=300)
bg = PhotoImage(file = "C:/Users/DELL/Desktop/New folder/j.png");
label1 = Label(window, image = bg)
label1.place(x = 0,y = 0,relwidth=1, relheight=1)
C.pack()
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
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...",command=ndihma)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.mainloop()
