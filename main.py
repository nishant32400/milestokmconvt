# 1 mile = 1.60 km

from tkinter import *

window = Tk()
window.title("Miles to Km conveter")
window.minsize(height=100, width=100)
window.config(padx=20,pady=20)

#Entry
entry = Entry(width=10)
# entry.grid(column=0, row=0)
entry.grid(column=2,row=2)


#Label 
label1 = Label(text="Miles")   # right side of entry
label1.grid(column=3,row=2)

label2 = Label(text="Is equal to")      # just below the lablel1
label2.grid(column=1,row=3)

lable3 = Label(text="0")                # right side of lable2 
lable3.grid(column=2,row=3)

lable4 = Label(text="Kms")
lable4.grid(column=3,row=3)

#botton
def calculate():
    miles = float(entry.get())       # Taking input from entry and saving it in miles variable
    ans = miles * 1.60
    lable3.config(text= '%.2f'%ans)

button = Button(text="Calculate", command=calculate)
button.grid(column=2,row=4)


















window.mainloop()