from tkinter import *

top = Tk()
top.title("GUI Decoder & Encoder Base64")
L1 = Label(top, text="Encode or Decode")
L1.pack(side="left")
E1 = Entry(top, bd = 5)
E1.pack(side="left")

#creating checkbox
check_var1 = IntVar()
check_var2 = IntVar()

C1 = Checkbutton(top,text="Encode", variable = check_var1, onvalue=1, offvalue =0, height=1, width=20)
C2 = Checkbutton(top,text="Decode", variable = check_var2, onvalue=1, offvalue =0, height=1, width=20)
B = Button(top, text = "Calculate") 




C1.pack()
C2.pack()
B.pack()

top.mainloop()
