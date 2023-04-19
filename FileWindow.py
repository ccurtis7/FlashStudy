from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Create an instance of tkinter frame or window
win = Tk()
win.geometry("500x500")
#Define a function to Opening the specific file using filedialog
def open_files():
    path= filedialog.askopenfilename(title="Select a file", filetypes=(("text files","*.py"), ("all files","*.*")))
    
    file= open(path,'r')
    txt= file.read()
    label.config(text=txt, font=('Courier 13 bold'))
    file.close()
    button.config(state=DISABLED)
    win.geometry("750x450")
    
#Create an Empty Label to Read the content of the File
label= Label(win,text="", font=('Courier 13 bold'))
label.pack()
#Create a button for opening files
button=ttk.Button(win, text="Open",command=open_files)
button.pack(pady=30)

def close():
   #win.destroy()
   win.quit()
# Create a Button to call close()
Button(win, text= "Close the Window", command=close).pack(pady=20)

win.mainloop()
