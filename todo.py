import tkinter
from tkinter import *

root=Tk()
root.title("To-Do List")
root.geometry('300x500')
root.resizable(False,False)

tasks_list=[]

def add_task():
    task=task_entry.get()
    
    if task.strip():
        listbox.insert(END,task)
        tasks_list.append(task)
        task_entry.delete(0,END)
        
def add_in_file():
    with open("tasks.txt","w") as tasks:
        list_box=listbox.get(0,END)
        
        for i in list_box:
            tasks.write(i+'\n')
            
def export_file():
    with open("tasks.txt","r") as tasks:
        lines=tasks.readlines()
        
    for i in lines:
        if i != '\n':
            tasks_list.append(i)
            listbox.insert(END,i)
            
def delete_task():
    task=str(listbox.get(ANCHOR))
    if task in tasks_list:
        tasks_list.remove(task)
        listbox.delete(ANCHOR)
        
def update_task():
    task=str(listbox.get(ANCHOR))
    task_entry.insert(0,task)
    delete_task()

icon=PhotoImage(file="logo.png")
root.iconphoto(False,icon)

top_image=PhotoImage(file="bg3.png")

bg_label = Label(root, image=top_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root,width=300,height=25,bg="white")
frame.place(x=0,y=120)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 10",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button= Button(frame,text="Add",font="arial 13 bold",width=6,bg="black",fg="#fff",bd=0,command=add_task)
button.place(x=235,y=0)

frame1=Frame(root,bd=3,width=300,height=150,bg="#ffffb6")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=28,height=13,bg="#ffffb6",fg="black",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame1 = Frame(root,bg="#ffffb6")
button_frame1.pack(side=BOTTOM, pady=5)

Button(button_frame1, text="Delete", bd=0,font="arial 12 bold", width=12, bg="black", fg="#fff",command=delete_task).pack(side=LEFT, padx=10)
Button(button_frame1, text="Update", bd=0,font="arial 12 bold", width=12, bg="black", fg="#fff",command=update_task).pack(side=LEFT, padx=10)

button_frame2 = Frame(root,bg="#ffffb6")
button_frame2.pack(side=BOTTOM, pady=10)

Button(button_frame2, text="Save in file", bd=0,font="arial 13 bold", width=12, bg="black", fg="#fff",command=add_in_file).pack(side=LEFT, padx=10)
Button(button_frame2, text="Export from file", bd=0,font="arial 13 bold", width=12, bg="black", fg="#fff",command=export_file).pack(side=LEFT, padx=10)

root.mainloop()
