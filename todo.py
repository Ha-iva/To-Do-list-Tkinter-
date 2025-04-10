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
# Label(root,image=top_image,bg="#32405b").place(x=0,y=0)

# heading=Label(root,text="All task",font="arial 20 bold",fg="white",bg="#32405b")
# heading.place(x=130,y=20)



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

# Add buttons inside the frame
Button(button_frame1, text="Delete", bd=0,font="arial 12 bold", width=12, bg="black", fg="#fff",command=delete_task).pack(side=LEFT, padx=10)
Button(button_frame1, text="Update", bd=0,font="arial 12 bold", width=12, bg="black", fg="#fff",command=update_task).pack(side=LEFT, padx=10)


button_frame2 = Frame(root,bg="#ffffb6")
button_frame2.pack(side=BOTTOM, pady=10)

# Add buttons inside the frame
Button(button_frame2, text="Save in file", bd=0,font="arial 13 bold", width=12, bg="black", fg="#fff",command=add_in_file).pack(side=LEFT, padx=10)
Button(button_frame2, text="Export from file", bd=0,font="arial 13 bold", width=12, bg="black", fg="#fff",command=export_file).pack(side=LEFT, padx=10)

root.mainloop()














    
        
# task_list=[]

# def opentask():
#     with open("tasks.txt","r") as task:
#         tasks=task.readlines()
        
#     for i in tasks:
#         if i !='\n':
#             task_list.append(i)
#             listbox.insert(END,i)
            
            









# import tkinter
# from tkinter import *

# # Create main window
# root = Tk()
# root.title("To-Do List")
# root.geometry('300x500')
# root.resizable(False, False)

# # List to store tasks
# task_list = []

# ### 🟢 Function to Add Task to Listbox Directly ###
# def add_task():
#     task = task_entry.get()  # Get text from entry box
    
#     if task.strip():  # Avoid adding empty tasks
#         listbox.insert(END, task)  # Add to Listbox
#         task_list.append(task)  # Add to task_list (for future use)
#         task_entry.delete(0, END)  # Clear entry box after adding task

# # 🟢 Function to Open Tasks from File (Optional) ###
# def opentask():
#     try:
#         with open("tasks.txt", "r") as task_file:
#             tasks = task_file.readlines()

#         for task in tasks:
#             if task.strip():  # Ignore empty lines
#                 task_list.append(task.strip())
#                 listbox.insert(END, task.strip())

#     except FileNotFoundError:
#         open("tasks.txt", "w").close()  # Create an empty file if not found

# # 🟢 UI Elements 🟢
# frame = Frame(root, width=300, height=25, bg="white")
# frame.place(x=0, y=120)

# # Entry Box
# task_entry = Entry(frame, width=18, font="arial 10", bd=0)
# task_entry.place(x=10, y=7)
# task_entry.focus()

# # Add Button
# button = Button(frame, text="Add", font="arial 13 bold", width=6, bg="black", fg="#fff", bd=0, command=add_task)
# button.place(x=235, y=0)

# # Listbox Frame
# frame1 = Frame(root, bd=3, width=300, height=150, bg="#ffde59")
# frame1.pack(pady=(160, 0))

# # Listbox (To Display Tasks)
# listbox = Listbox(frame1, font=('arial', 12), width=28, height=10, bg="#ffde59", fg="black", cursor="hand2", selectbackground="#5a95ff")
# listbox.pack(side=LEFT, fill=BOTH, padx=2)

# # Scrollbar
# scrollbar = Scrollbar(frame1)
# scrollbar.pack(side=RIGHT, fill=BOTH)
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# # Load tasks from file (if any)
# opentask()

# # Buttons Frame
# button_frame = Frame(root)
# button_frame.pack(side=BOTTOM, pady=15)

# # Delete & Update Buttons
# Button(button_frame, text="Delete", bd=0, width=10, bg="red", fg="white").pack(side=LEFT, padx=10)
# Button(button_frame, text="Update", bd=0, width=10, bg="blue", fg="white").pack(side=LEFT, padx=10)

# root.mainloop()
