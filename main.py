from tkinter import *
from backend import *
import csv

root = Tk()
root.geometry('690x400')
lb = Label(root, text='PERIODIC TABLE', font={'Helvetica', 15, 'bold'})
lb.place(x=205, y=10)

''' This function is used as button command which basically opens a new window and 
lists all the details of each element '''
def func(list_, x):
    win = Toplevel(root)
    win.geometry('350x150')
    temp = list_[x]
    v = temp.split(' ')
    lb = Text(win)
    lb.insert(INSERT, 'Symbol : ')
    lb.insert(END, v[0])
    lb.insert(INSERT, '\nName : ')
    lb.insert(END, v[1])
    lb.insert(INSERT, '\nAtomic Number : ')
    lb.insert(END, v[2])
    lb.insert(INSERT, '\nBlock : ')
    lb.insert(END, v[3])
    lb.insert(INSERT, '\nAtomic weight : ')
    lb.insert(END, v[4])
    lb.insert(INSERT, '\nElectronic configuration : ')
    st = ''
    for string in v[5:]:
        st += string
        st += ' '
    lb.insert(END, st)
    lb.pack()

''' The below function will open a file and read all the elements of 1st column and 18th(nobel gas) column 
and append the record of each element into a list '''
file1()

# Creating buttons for the elements in  1st and last column of the periodic table
r = 5  # row
c = 4  # column
k = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        b = Button(root, text=l[i][j], width=4, height=2, bg = b1[k])
        b.grid(row=r, column=c)
        b['command'] = lambda x=k: func(s1_s18, x)
        r += 1
        k += 1
    r = 5
    c = 21

''' The below function will open a file and read all the elements of 2nd column and append the 
record of each element into a list '''
file2()

# Creating buttons for the elements in 2nd column of the periodic table
r = 6
c = 5
k = 0
for i in range(0, 6):
    b = Button(root, text=c2[i], width=4, height=2, bg = b2[k])
    b.grid(row=r, column=c)
    b['command'] = lambda x=k: func(s2_, x)
    r += 1
    k += 1


''' The below function will open a file and read all the elements of 13th column to 17th column 
and append the record of each element into a list '''
file4()

# Creating buttons for the elements from 13th column till 17th column of the periodic table
r = 6
c = 16
k = 0
for i in range(len(l1)):
    temp = c
    for j in range(len(l1[i])):
        b = Button(root, text=l1[i][j], width=4, height=2, bg = b5[k])
        b.grid(row=r, column=temp)
        b['command'] = lambda x=k: func(s13_17, x)
        r += 1
        k += 1
    r = 6
    c += 1

''' The below function will open a file and read all the elements of 3rd column to 12th column 
and append the record of each element into a list '''
file3()

# Creating buttons for elements in 3rd,4th,5th,6th,7th,8th,9th,10th,11th,12th columns of the periodic table
r = 8
c = 6
k = 0
for i in range(len(l2)):
    for j in range(len(l2[i])):
        b = Button(root, text=l2[i][j], width=4, height=2, bg = b3[k])
        b['command'] = lambda x=k: func(s3_to_s12,x)
        b.grid(row=r, column=c)
        r += 1
        k += 1
    r = 8
    c += 1
    i += 1

''' The below function will open a file and read all the elements of Lanthanides and Actinides
and append the record of each element in a list '''
file5()

# Creating buttons for elements in  Lanthanides and Actinides
r = 13
c = 8
k = 0
n = 0
for i in range(len(l4)):
    for j in range(len(l4[i])):
        b = Button(root, text=l4[i][j], width=4, height=2, bg = b4[n])
        b.grid(row=r, column=c, pady=8)
        b['command'] = lambda x=k: func(s19_20,x)
        c += 1
        k += 1
    n += 1
    r += 1
    c = 8

root.mainloop()

