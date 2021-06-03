import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Entry, messagebox
import re
import requests
import os

data=""
root =tk.Tk()
mystring =tk.StringVar(root)
def getvalue():
    open_button["state"]="active"
    global data
    url = str(mystring.get())
    mylist.delete(0,tk.END)
    msg=""
    text = requests.get(url).text
    x = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", text)   #Regex query which search for the particular email format.
    val=""
    count=0
    for i in x: 
        val+=i+"\n"
        mylist.insert(count,str(i))
        count+=1
    if val=="":
        msg="No emails found in the website"
    else:
        msg="Email(s) found:\n"
    email_found.config(text=msg)
    mylist.grid(row=3,column=1)
    root.geometry('500x300') 
    data=""
    data+=(msg+val)
    print(data)
    
root.geometry('500x150') 
tk.Label(root, text="Website url: ").grid(row=0)
e1 = Entry(root,textvariable = mystring,fg="blue",width=50, bd=3,selectbackground='violet').grid(row=0, column=1, padx = 5, pady = 5)
button1 = tk.Button(root, 
                text='Search the website', 
                fg='White', 
                bg= 'dark green', command=getvalue).grid(row=2,column=1)

print(data)
email_found = tk.Label(text="")
email_found.grid(row=3,column=0)

scroll_bar = tk.Scrollbar(root)
mylist = tk.Listbox(root, width=50, yscrollcommand = scroll_bar.set)

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwdb(),
        filetypes=filetypes)
    with open(f"{filename}","w") as file:
        file.write(data)
        #rint("val:"+val)
        print("dta"+data)
        print("Your File has been Saved")

# open button
open_button = tk.Button(
    root,
    text='Save E-Mails in a file',
    command=select_file,
)
open_button['state'] = "disabled"
open_button.grid(row=4,column=1)

root.mainloop()
