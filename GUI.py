import tkinter
giao_dien = tkinter.Tk()
giao_dien.title("Máy tính cầm tay - Python")
giao_dien.geometry('500x500')
#def
tinh=""
def count(numbers):
    global tinh
    tinh =tinh+ str(numbers)
    tinh_toan.set(tinh)

#label
Font_tuple = ("Comic Sans MS", 12, "bold")
label = tkinter.Label(giao_dien,text="CHƯƠNG TRÌNH MÁY TÍNH" ,fg='black',font=Font_tuple)
label.place(relx = 0.5, rely = 0.05, anchor = 'center')


#text box
tinh_toan = tkinter.StringVar()
text_box1 = tkinter.Entry(giao_dien,width=590,bd=10,textvariable=tinh_toan, justify='right')
text_box1.place(rely = 0.07,height=55)
# text_box1.configure(state='normal')

#button
btn9 = tkinter.Button(giao_dien,command=count(9),text='9')
btn9.place(relx = 0.05, rely = 0.27,width=80,height=50)

btn8 = tkinter.Button(giao_dien,command=count(8),text='8')
btn8.place(relx = 0.25, rely = 0.27,width=80,height=50)

btn7 = tkinter.Button(giao_dien,command=count(7),text='7')
btn7.place(relx = 0.45, rely = 0.27,width=80,height=50)

btn6 = tkinter.Button(giao_dien,command=count(6),text='6')
btn6.place(relx = 0.05, rely = 0.42,width=80,height=50)

btn5 = tkinter.Button(giao_dien,command=count(5),text='5')
btn5.place(relx = 0.25, rely = 0.42,width=80,height=50)

btn4 = tkinter.Button(giao_dien,command=count(4),text='4')
btn4.place(relx = 0.45, rely = 0.42,width=80,height=50)

btn3 = tkinter.Button(giao_dien,command=count(3),text='3')
btn3.place(relx = 0.05, rely = 0.57,width=80,height=50)

btn2 = tkinter.Button(giao_dien,command=count(2),text='2')
btn2.place(relx = 0.25, rely = 0.57,width=80,height=50)

btn1 = tkinter.Button(giao_dien,command=count(1),text='1')
btn1.place(relx = 0.45, rely = 0.57,width=80,height=50)

# btn1 = tkinter.Button(giao_dien,command=count(1),text='1')
# btn1.place(relx = 0.05, rely = 0.22,width=80,height=50)


giao_dien.mainloop()