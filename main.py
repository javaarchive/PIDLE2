from tkinter import *
tk=Tk()
tk.overrideredirect(True)

photo = PhotoImage(file="LOGO.gif")
label = Label(tk,image=photo)
label.image = photo # keep a reference!
label.pack()
l=Label(tk,text="LOADING")
l.pack()
sf=None
def save():
    global sf
    if sf==None:
        sf=filedialog.asksaveasfilename(title = "Select file to save to",filetypes = (("Python files","*.py"),("all files","*.*")))
        print(sf)
    if sf=='':
        sf=None
        return None
    a=open(sf,"w")
    a.write(t1.get(0.0,END))
    a.close()
    
def openf():
    sf=filedialog.askopenfilename(title = "Select file to save to",filetypes = (("Python files","*.py"),("all files","*.*")))
    a=open(sf,"r")
    t1.delete("0.0",END)
    t1.insert(END,a.read())
    a.close()
        
def build():
    t1.insert(0.0,"Welcome to PIDLE")
    menu=Menu(tk)
    print("CONFIGURING MENUS")
    tk.config(menu=menu)
    l["text"]="LOading stage 1:Completed"
    menu.add_command(label="Save",command=save)
    menu.add_command(label="Open",command=openf)
    print("MENU DONE")
    tk.title("PIDLE 2.0")
    tk.overrideredirect(False)
    
    label.destroy()
    tk.mainloop()
def init():
    global t1
    t1=Text(tk)
    t1.pack()
    tk.after(1000,build)
    
def test():
    import time,random,re
    l["text"]="Loaded main libraries"
    time.sleep(0.7)
    l["text"]="Tested time"
    text=None
    
    l["text"]="Starting"
    
    tk.after(1000,init)
tk.after(1000,test)
