import tkinter as tk
import math

root = tk.Tk()
root.title("Converter")

a = 6375137
f = 1/298.257223563
e2 = 2*f - f**2


def compute():
    ph = math.radians(float(phentry.get()))

    rm = a*(1-e2)/(1-e2*(math.sin(ph))**2)**1.5
    rn = a/(1-e2*(math.sin(ph))**2)**0.5
    resultlabel["text"] = f"Rm: {rm}\n Rn: {rn}\n Rmn: {(rm*rn)**0.5}"
    resultlabel.grid(column=1, columnspan=2)


label1 = tk.Label(root, text=" Input the latitude: ")

phlabel = tk.Label(root, text="ϕ:")
phentry = tk.Entry(root)
phlabel.grid(column=1, row=1)
phentry.grid(column=2, row=1)

resultlabel = tk.Label(root, text="")

calcbutton = tk.Button(root, text='Calculate radii!', command=compute)
calcbutton.grid(column=1, row=2, columnspan=2)

root.mainloop()
