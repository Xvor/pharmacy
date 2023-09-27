from tkinter import *
import datetime
from tkinter import messagebox

OWAIS = Tk()
OWAIS.title("sales form for Medicine")
OWAIS.geometry("600x500")
OWAIS.configure(bg="light blue")

Medicine1_list = ["Cold Medicine(3.25$)", "Cough Medicine(4.75$)", "Fever Medicine(4.50$)"]
skin_care_list = ["Moisturizer(1.75$)", "Sun cream (2.00$)", "Care tools(2.25$)"]
pills_list = ["Panadol(1.75$)", "Panadol Extra(2.00$)", "Panadol Night(4$)"]


def cal():
    messagebox.showinfo("Thanks", "Thank you for purchase from us -please visit us again- :)")
    name = myNameString.get()

    Medicine = md.curselection()
    skin_care = sl.curselection()
    pills = pl.curselection()

    if Medicine[0] == 0:
        mc = 3.25
    elif Medicine[0] == 1:
        mc = 4.75
    elif Medicine[0] == 2:
        mc = 4.5

    if skin_care[0] == 0:
        sc = 1.75
    elif skin_care[0] == 1:
        sc = 2
    elif skin_care[0] == 2:
        sc = 2.25

    if pills[0] == 0:
        pc = 1.75
    elif pills[0] == 1:
        pc = 2
    elif pills[0] == 2:
        pc = 4

    if v.get() == 1:
        loc = "Ibra"
        ans.set(f"{loc}")
    elif v.get() == 2:
        loc = "Muscat"
        ans.set(f"{loc}")
    elif v.get() == 3:
        loc = "Nizwa"
        ans.set(f"{loc}")
    elif v.get() == 4:
        loc = "Ibri"
        ans.set(f"{loc}")
    elif v.get() == 5:
        loc = "Bidya"
        ans.set(f"{loc}")

    if j.get() == 1:
        com = "Yes :)"
        ans.set(f"{com}")
    elif j1.get() == 1:
        com = "no :("
        ans.set(f"{com}")

    totalCost = mc + sc + pc
    total.set(f"{totalCost}")

    d = datetime.datetime.today()

    print("==============================")
    print("------------------------------")
    print()
    print("Date:", d.strftime("%d-%B-%Y"))
    print("Time:", d.strftime("%H:%M:%S"))
    print()
    print("==============================")
    print("RECEIPT FOR PURCHASE")
    print()
    print("Customer:", name.upper())
    print("locatio:", loc)
    print("Are you happy:", com)
    print()
    print("==============================")
    print("ITEMS:")
    print(Medicine1_list[Medicine[0]])
    print(skin_care_list[skin_care[0]])
    print(pills_list[pills[0]])
    print()

    print("Total: $", f"{totalCost}")
    print("==============================")
    print()

    file = open("pharmacyData.txt", "w")

    file.write(d.strftime("%d-%B-%Y") + "\n")
    file.write(d.strftime("%H:%M:%S") + "\n")
    file.write(name.upper() + "\n")
    file.write(loc.upper() + "\n")
    file.write(Medicine1_list[Medicine[0]] + "\n")
    file.write(skin_care_list[skin_care[0]] + "\n")
    file.write(pills_list[pills[0]] + "\n")
    file.write(f"TOTAL={totalCost}" + "\n")

    file.close()


v = IntVar()
l1 = Label(OWAIS, text="you're welcome to buy it anytime", fg="lightseagreen", font="Arial 20 bold", justify="center")
l2 = Label(OWAIS, text="Enter Your Name :", fg="teal", bg="light blue", font="Arial 10 bold")

l4 = Label(OWAIS, text="Choose the location of the pharmacy:", fg="teal", bg="light blue", font="Arial 10 bold")
r1 = Radiobutton(OWAIS, text="Ibra pharmacy", variable=v, value=1, bg="light blue")
r2 = Radiobutton(OWAIS, text="Muscat pharmacy", variable=v, value=2, bg="light blue")
r3 = Radiobutton(OWAIS, text="Nizwa pharmacy", variable=v, value=3, bg="light blue")
r4 = Radiobutton(OWAIS, text="Ibri pharmacy", variable=v, value=4, bg="light blue")
r5 = Radiobutton(OWAIS, text="Bidya pharmacy", variable=v, value=5, bg="light blue")
l5 = Label(OWAIS, text="Name of Medicine:", bg="light blue", fg="teal", font="Arial 10 bold")

l1.grid(row=0, column=0, columnspan=3)
l2.grid(row=1, column=0, sticky=W)

l4.grid(row=3, column=0)
l5.grid(row=8, column=0, sticky=W)

r1.grid(row=5, sticky=W)
r2.grid(row=5, column=1, sticky=W)
r3.grid(row=6, sticky=W)
r4.grid(row=6, column=1, sticky=W)
r5.grid(row=7, sticky=W)

D1 = Label(OWAIS, text="Medicine:", fg="lightseagreen", font="Arial 10 bold")
D1.grid(row=9, column=0, padx=0, pady=10)

D2 = Label(OWAIS, text="skin_care:", fg="lightseagreen", font="Arial 10 bold")
D2.grid(row=9, column=1, padx=0, pady=10)

D3 = Label(OWAIS, text="pills:", fg="lightseagreen", font="Arial 10 bold")
D3.grid(row=9, column=2, padx=0, pady=10)

D4 = Label(OWAIS, text="TOTAL:", fg="lightseagreen", font="Arial 10 bold")
D4.grid(row=15, column=0, padx=10, pady=15)

MString = StringVar()
md = Listbox(OWAIS, listvariable=MString, exportselection=0, width=22, height=3)
md.grid(row=14, column=0, padx=10, pady=10)
MString.set(Medicine1_list)

SString = StringVar()
sl = Listbox(OWAIS, listvariable=SString, exportselection=0, width=22, height=3)
sl.grid(row=14, column=1, padx=10, pady=10)
SString.set(skin_care_list)

PString = StringVar()
pl = Listbox(OWAIS, listvariable=PString, exportselection=0, width=22, height=3)
pl.grid(row=14, column=2, padx=10, pady=10)
PString.set(pills_list)

myButton = Button(OWAIS, text="Add to the order", width=15, fg="darkslategrey", bg="wheat", font="Arial 12 bold",
                  command=cal)
myButton.grid(row=16, column=1, padx=10, pady=15)

total = StringVar()
myTotal = Entry(OWAIS, state="readonly", width=20, textvariable=total)
myTotal.grid(row=15, column=1)
T1 = Entry(OWAIS)

myNameString = StringVar()
myName = Entry(OWAIS, textvariable=myNameString)
myName.grid(row=1, column=0, sticky=E)
ans = StringVar()

myloc = Entry(OWAIS, textvariable=ans)
e1 = Button(OWAIS, text="Exit", width=15, fg="darkslategrey", bg="tomato", font="Arial 12 bold", command=OWAIS.destroy)
e1.grid(row=17, column=1)

j = IntVar()
j1 = IntVar()
m1 = Label(OWAIS, text="Are you happy with the service:", bg="light blue", font="Arial 10 bold")
m1.grid(row=16, column=0, sticky=W)
ds = Checkbutton(OWAIS, text="Yes :)", bg="lightgreen", variable=j).grid(row=17, column=0, sticky=W)
ds = Checkbutton(OWAIS, text="No :(", bg="salmon", variable=j1).grid(row=17, column=0)

OWAIS.mainloop()