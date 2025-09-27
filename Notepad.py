from tkinter import *
from tkinter import filedialog
#Geometery
root=Tk()
root.geometry("600x600") 
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False,False)
#Button_function
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return 
    Text=str(entry.get(1.0,END))
    open_file.write(Text)
    open_file.close()

def open_file():
    open_file=filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    if open_file is not None:
        content=open_file.read()
    entry.insert(INSERT,content)

#Button_Coustomisation
b1=Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5)
#interface
entry=Text(root,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()


