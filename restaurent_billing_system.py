from tkinter import *

def addNumbers():
    res = int(e1.get() or 0) * 30 + int(e2.get() or 0) * 40 + int(e3.get() or 0) * 80 + int(e4.get() or 0) * 100 + int(e5.get() or 0) * 150 + int(e6.get() or 0) * 150 + int(e7.get() or 0) * 45
    if res > 500:
        r1 = 40
    else:
        r1 = 0
    r2 = res * 0.05
    r3 = r1 + r2
    t = res + r3
    myText.set(res)
    service_charge.set(r1)
    sales_tax.set(r2)
    sub_total.set(r3)
    total.set(t)

def clearFunc():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    myText.set("")
    service_charge.set("")
    sales_tax.set("")
    sub_total.set("")
    total.set("")

master = Tk()
master.configure(bg="light gray")

myText = StringVar()
service_charge = StringVar()
sales_tax = StringVar()
sub_total = StringVar()
total = StringVar()

frame = Frame(master, bg="white")
frame.pack(padx=20, pady=20)

Label(frame, text="FRIES", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
Label(frame, text="NOODLES", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
Label(frame, text="FRIED RICE", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=5)
Label(frame, text="BIRYANI", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=5)
Label(frame, text="BURGER", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=5)
Label(frame, text="PIZZA", font=("Arial", 14)).grid(row=6, column=0, padx=10, pady=5)
Label(frame, text="Flavours Restaurant", font=("Helvetica", 20, "bold"), bg="white").grid(row=0, column=1, columnspan=3, pady=10)
Label(frame, text="SOFT DRINKS", font=("Arial", 14)).grid(row=7, column=0, padx=10, pady=5)
Label(frame, text="30/-", font=("Arial", 14)).grid(row=1, column=2, padx=10, pady=5)
Label(frame, text="40/-", font=("Arial", 14)).grid(row=2, column=2, padx=10, pady=5)
Label(frame, text="80/-", font=("Arial", 14)).grid(row=3, column=2, padx=10, pady=5)
Label(frame, text="100/-", font=("Arial", 14)).grid(row=4, column=2, padx=10, pady=5)
Label(frame, text="150/-", font=("Arial", 14)).grid(row=5, column=2, padx=10, pady=5)
Label(frame, text="150/-", font=("Arial", 14)).grid(row=6, column=2, padx=10, pady=5)
Label(frame, text="45/-", font=("Arial", 14)).grid(row=7, column=2, padx=10, pady=5)
Label(frame, text="Cost of Meal", font=("Arial", 14)).grid(row=1, column=3, padx=10, pady=5)
Label(frame, text="Service Charge", font=("Arial", 14)).grid(row=2, column=3, padx=10, pady=5)
Label(frame, text="Sales Tax @5%", font=("Arial", 14)).grid(row=3, column=3, padx=10, pady=5)
Label(frame, text="Sub Total", font=("Arial", 14)).grid(row=4, column=3, padx=10, pady=5)
Label(frame, text="Total Cost", font=("Arial", 14)).grid(row=5, column=3, padx=10, pady=5)

result = Entry(frame, textvariable=myText, font=("Arial", 14), width=10)
result.grid(row=1, column=4, padx=10, pady=5)
result = Entry(frame, textvariable=service_charge, font=("Arial", 14), width=10)
result.grid(row=2, column=4, padx=10, pady=5)
result = Entry(frame, textvariable=sales_tax, font=("Arial", 14), width=10)
result.grid(row=3, column=4, padx=10, pady=5)
result = Entry(frame, textvariable=sub_total, font=("Arial", 14), width=10)
result.grid(row=4, column=4, padx=10, pady=5)
result = Entry(frame, textvariable=total, font=("Arial", 14), width=10)
result.grid(row=5, column=4, padx=10, pady=5)

e1 = Entry(frame, font=("Arial", 14), width=10)
e2 = Entry(frame, font=("Arial", 14), width=10)
e3 = Entry(frame, font=("Arial", 14), width=10)
e4 = Entry(frame, font=("Arial", 14), width=10)
e5 = Entry(frame, font=("Arial", 14), width=10)
e6 = Entry(frame, font=("Arial", 14), width=10)
e7 = Entry(frame, font=("Arial", 14), width=10)
e1.grid(row=1, column=1, padx=10, pady=5)
e2.grid(row=2, column=1, padx=10, pady=5)
e3.grid(row=3, column=1, padx=10, pady=5)
e4.grid(row=4, column=1, padx=10, pady=5)
e5.grid(row=5, column=1, padx=10, pady=5)
e6.grid(row=6, column=1, padx=10, pady=5)
e7.grid(row=7, column=1, padx=10, pady=5)

b = Button(frame, text="TOTAL", command=addNumbers, font=("Arial", 14), width=10)
Reset = Button(frame, text="RESET", command=clearFunc, font=("Arial", 14), width=10)
b.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
Reset.grid(row=8, column=4, columnspan=2, padx=10, pady=10)

master.mainloop()
