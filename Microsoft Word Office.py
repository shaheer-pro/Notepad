from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os as OperatingSystem



if __name__ == "__main__":
    root = Tk()
    root.geometry("444x344")
    root.maxsize(width=500, height=500)
    root.minsize(width=200, height=200)

    root.title("Untitled - Microsoft Shaheer Word")
    root.wm_iconbitmap("1.ico")
    text_area = Text(root, font=("Courier New", 14))
    text_area.pack(fill=BOTH)
    
    File = None
    def NewFile():
        global File
        root.title("Untitled - Microsoft Shaheer Word")
        File = None
        text_area.delete(1.0, END)

    def OpenFile():
        global File
        File = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                    ("Text Documents", "*.txt")])

        if File == "":
            File = None
        else:    
            root.title(OperatingSystem.path.basename(File) + " - Microsoft Shaheer Word")
            text_area.delete(1.0, END)
            f = open(File, "r")
            text_area.insert(1.0, f.read())
            f.close()

    def SaveFile():
        global File

        if File == None:
            File = asksaveasfilename(initialfile="Untitled.txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if File == "":
                File = None
            else:
                f = open(File, "w")
                f.write(text_area.get(1.0, END))
                f.close()
                root.title(OperatingSystem.path.basename(File) + " - Microsoft Shaheer Word")
                showinfo("Successfully Saved!", "The File has been successfully saved!")
        else:
            f = open(File, "w")
            f.write(text_area.get(1.0, END))
            f.close()

    def Cut():
        text_area.event_generate(("<<Cut>>"))

    def Copy():
        text_area.event_generate(("<<Copy>>"))
        
    def Paste():
        text_area.event_generate(("<<Paste>>"))

    def About():
        showinfo("About", "Created By Shaheer Ahmed Raza")

    Menubar = Menu(root)

    FileMenu = Menu(Menubar)
    FileMenu.add_command(label="New", command=NewFile)
    FileMenu.add_command(label="Open", command=OpenFile)
    FileMenu.add_command(label="Save File", command = SaveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command = root.destroy)
    Menubar.add_cascade(label="File", menu=FileMenu)

    root.config(menu=Menubar)

    EditMenu = Menu(Menubar)
    EditMenu.add_command(label="Cut", command=Cut)
    EditMenu.add_command(label="Copy", command=Copy)
    EditMenu.add_command(label="Paste", command = Paste)
    Menubar.add_cascade(label="Edit", menu=EditMenu)
    root.config(menu=Menubar)
    
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label="About", command=About)
    Menubar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=Menubar)

    

    root.mainloop()