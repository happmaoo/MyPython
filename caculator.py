
from tkinter import *
import tkinter
import tkinter.messagebox


# 也可以写在函数中方便调用
def tk_center(root,width, height):
    x = int(root.winfo_screenwidth() / 2 - width / 2)
    y = int(root.winfo_screenheight() / 2 - height / 2)
    size = '{}x{}+{}+{}'.format(width, height, x, y)
    return size

def calculate(minp,maxp,parts,buynum):
    minp = float(minp)
    maxp = float(maxp)
    parts = float(parts)
    buynum = float(buynum) / parts

    cal = (maxp - minp) / (parts -1)
    #print(cal)


    count = 0

    price = minp
    str1 = ""
    while count < parts:
        #print (count)
        print (round(price))
        str1 = str1 + str(round(price)) + "\n"
        price = price + cal
        count = count + 1
    return str1  + "\n" + str(buynum)


def on_click():
    te.delete('1.0','end')
    minp = text1.get()
    maxp = text2.get()
    parts = text3.get()
    buynum = text4.get()
    str1 = calculate(minp,maxp,parts,buynum)
    te.insert(tkinter.END,str1)

root = Tk()
root.title('Calculate')



fr = Frame(padx=10,pady=10)
fr.grid()


root.geometry(tk_center(root,500,250))
root.option_add("*font", "Tahoma 12")



label = Label(fr,text="min price",anchor=N).grid(column=0,row=0,padx=0,pady=0)
label = Label(fr,text="max price",anchor=N).grid(column=0,row=1,padx=0,pady=0)
label = Label(fr,text="parts",anchor=N).grid(column=0,row=2,padx=0,pady=0)
label = Label(fr,text="cost",anchor=N).grid(column=0,row=3,padx=0,pady=0)

text1 = Entry(fr)
text1.grid(column=1,row=0,padx=0,pady=0)
text2 = Entry(fr)
text2.grid(column=1,row=1,padx=0,pady=0)
text3 = Entry(fr)
text3.insert(0,5)
text3.grid(column=1,row=2,padx=0,pady=0)
text4 = Entry(fr)
text4.insert(0,10000)
text4.grid(column=1,row=3,padx=0,pady=0)

te = Text(fr,height=8,width=20)
te.grid(column=2,row=0,padx=10,pady=10,rowspan=3)

btn = Button(fr,text="Calculate",anchor=CENTER,height=1,command=on_click)
btn.grid(column=2,row=3,padx=0,pady=10)

root.mainloop()
