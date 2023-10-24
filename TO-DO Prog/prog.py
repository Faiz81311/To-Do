import random
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk



# Create root window
root=Tk()

# change icon
root.iconbitmap('D:\\My Python\\TO-DO Prog\\notebook.png')

# change root window bg color
root.config(bg='black')

# change the title
root.title('TO-DO COMP')

# change windo sizw
root.geometry('558x450')



# # background
load=Image.open("D:\\My Python\\TO-DO Prog\\pen.jpg")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=-100,y=-20)


# create an mt list
tasks=[]


# Functions


def update_listbox():
    # mt the list after
    clear_listbox()
    # to insert into the list
    for task in tasks:
        lb_tasks.insert('end',task)
    

def clear_listbox():
    lb_tasks.delete(0,'end')

def add_task():
    # task to add
    task=text_input.get()
    if task=='':
        messagebox.showwarning('WARNING','You Need To Enter A Task')
    else:
        tasks.append(task)
        update_listbox()

    text_input.delete(0,'end')

def del_all():
    con=messagebox.askyesno('Please Confirm','Do You Want To Delete All Tasks ?' )
    if con==True:
        global tasks
        tasks=[]
        update_listbox()


def del_one():
    # to get selected item
    task=lb_tasks.get('active')
    # conforim it is in the list
    if task in tasks:
        tasks.remove(task)
    update_listbox()
    

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_rand():
    task=random.choice(tasks)
    #update display
    lbl_display['text']=task


def show_number_of_tasks():
    number_of_tasks=len(tasks)
    msg='Number Of Tasks: %s'%number_of_tasks
    # display msg
    lbl_display['text']=msg



# title of prog (in the window)
lbl_title=Label(root,text='To-Do List',bg='white',fg='black')
lbl_title.grid(row=0,column=1)

lbl_display=Label(root,text='',bg='white',fg='black')
lbl_display.grid(row=1,column=1)

text_input=Entry(root,justify=CENTER,width=20,fg='black',bg='white')
text_input.grid(row=2,column=1)

# to add a task
btn_add_task=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Add Task',fg='black',bg='white',command=add_task)
btn_add_task.grid(row=3,column=0)

# to delete all task
btn_del_all=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Delete All',fg='black',bg='white',command=del_all)
btn_del_all.grid(row=4,column=2)

# to delete one task
btn_del_one=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Delete One',fg='black',bg='white',command=del_one)
btn_del_one.grid(row=3,column=2)

# to sort by asc
btn_sort_asc=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Sort (ASC) ',fg='black',bg='white',command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

# to sort by desc
btn_sort_desc=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Sort (DESC)',fg='black',bg='white',command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

# random
btn_choose_rand=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Choose random',fg='black',bg='white',command=choose_rand)
btn_choose_rand.grid(row=6,column=0)

# to show number of tasks
btn_number_of_tasks=Button(root,activeforeground='light green',bd=5,activebackground='grey',width=20,text='Number Of Tasks',fg='black',bg='white',command=show_number_of_tasks)
btn_number_of_tasks.grid(row=5,column=2)

# to exit
btn_exit=Button(root,bd=5,activebackground='Red' ,width=20,text='Exit',fg='black',bg='white',command=exit)
btn_exit.grid(row=6,column=2)


# Task Disaplay
lb_tasks =Listbox(root,width=40,fg='black',bg='white')
lb_tasks.grid(row=3,column=1,rowspan=7)


# start the events
root.mainloop()

    