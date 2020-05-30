### PW GEN w/ GUI ###

import string
from random import *
from tkinter import *
import tkinter as tk

value = string.ascii_letters + string.punctuation + string.digits

# Title Name #
root = tk.Tk()
root.title("Password Vault")

# Create Canvas #
canvas1 = tk.Canvas(root, width=600, height=600, relief='raised')
canvas1.pack()

# Header labele #
header = tk.Label(root, text='WELCOME TO PASSWORD-VAULT')
header.config(font=('arial', 25, 'bold'))
canvas1.create_window(300, 25, window=header)
# Header labele #

########################## SECTION LABLE ################
create = tk.Label(root, text='CREATE',
                  bg='grey',
                  fg='white')
create.config(font=('arial', 20, 'bold'))
canvas1.create_window(170, 100, window=create)

find = tk.Label(root, text='FIND',
                bg='grey',
                fg='white')
find.config(font=('arial', 20, 'bold'))
canvas1.create_window(420, 100, window=find)
############################ SECTION LABLE #######################



######################################### WEBSITE ###########################
## C-WEBSITE ##
website = tk.Label(root, text="Website")
website.config(font=('arial', 20))
canvas1.create_window(170, 150, window=website)

WEntry = tk.Entry(root)
canvas1.create_window(175, 200, window=WEntry)
## C-WEBSITE ##

## F-WEBSITE ##
fwebsite = tk.Label(root, text='Website')
fwebsite.config(font=('arial', 20))
canvas1.create_window(420, 150, window=fwebsite)

FWentry = tk.Entry(root)
canvas1.create_window(420, 200, window=FWentry)
## F-WEBSITE ##
######################################### WEBSITE ###########################



######################################### USER NAME ###########################
## USER NAME ##
username = tk.Label(root, text="Username")
username.config(font=('arial', 20))
canvas1.create_window(174, 250, window=username)

UEnttry= tk.Entry(root)
canvas1.create_window(175, 300, window=UEnttry)
## USER NAME ##

## F-USERNAME ##
FUN = tk.Label(root, text='Username')
FUN.config(font=('airal', 20))
canvas1.create_window(420, 250, window=FUN)

FUEntry = tk.Entry(root)
canvas1.create_window(420, 300, window=FUEntry)
## F-USERNAME ##
######################################### USER NAME ###########################


######################################### LENGHT ###########################
## LENGHT ##
lenght = tk.Label(root, text="Lenght")
lenght.config(font=('airal', 20))
canvas1.create_window(157, 350, window=lenght)

entry3= tk.Entry(root)
canvas1.create_window(175, 400, window=entry3)
## LENGHT ##
######################################### LENGHT ###########################

########## DEF PW GEN #########
def genPW():
    x1 = entry3.get()
    x2 = WEntry.get()
    x3 = UEnttry.get()

    label3 = tk.Label(root, text='Your password for website ' + x2 + ' with username ' + x3 + ' is:' , font=('helvetica', 10))
    canvas1.create_window(300, 480, window=label3)
    test = float(x1)
    test = int(test)
    pw = "".join(choice(value) for x in range(test))
    print(pw)
    file = open('PassInfo.txt', 'a+')
    file.write('Password for website ' + x2 + ' with username ' + x3 + ' is: ' + pw + '\r\n')
    file.close()

    label4 = tk.Label(root, text=pw, font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 500, window=label4)
########## DEF PW GEN #########



########## DEF FIND PW#########
def findPW():
    Username = FWentry.get()
    Website = FUEntry.get()

    f = open('PassInfo.txt', "r")
    f1 = f.readlines()

    tomatch = Website + Username
    with open('PassInfo.txt', 'r') as file:
        for line in file:
            if Username and Website in line:
                tomatch = line
                print(tomatch)
                break


    Lfind = tk.Label(root, text=tomatch, font=('helvetica', 10,))
    canvas1.create_window(300, 550, window=Lfind)
########## DEF FIND PW#########



### BUTTON FOR FIND ###
fbutton = tk.Button(text='Find Password', command=findPW, bg='red', fg='white',
                    font=('helvetica', 9, 'bold')),
canvas1.create_window(430, 450, window=fbutton)
### BUTTON FOR FIND ###


### BUTTON FOR GENERATE ###
button1 = tk.Button(text='Generate Password', command=genPW, bg='red', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(175, 450, window=button1)
### BUTTON FOR GENERATE ###


root.mainloop()

