import tkinter as tk
import math

root = tk.Tk()
root.title("Converter")

a = 6375137
f = 1/298.257223563
e2 = 2*f - f**2


def compute():
    h = math.radians(float(hentry.get()))
    ph = math.radians(float(phentry.get()))
    la = math.radians(float(laentry.get()))
    N = a/(1-e2*(math.sin(ph))**2)

    x = (N+h)*math.cos(ph) * math.cos(la)
    y = (N+h)*math.cos(ph) * math.sin(la)
    z = (N*(1-e2)+h) * math.sin(ph)

    resultlabel["text"] = f"Cartesian Coordinates are:\nx: {x}\n, y: {y}\n, z: {z}"
    resultlabel.grid(column=1, columnspan=2)


label1 = tk.Label(root, text=" Input the Geodetic coordinates: ")
label1.grid(column=1, row=1, columnspan=2)

hlabel = tk.Label(root, text="h:")
hentry = tk.Entry(root)
hlabel.grid(column=1, row=2)
hentry.grid(column=2, row=2)

phlabel = tk.Label(root, text="ϕ(lat):")
phentry = tk.Entry(root)
phlabel.grid(column=1, row=3)
phentry.grid(column=2, row=3)

lalabel = tk.Label(root, text="ƛ(lon):")
laentry = tk.Entry(root)
lalabel.grid(column=1, row=4)
laentry.grid(column=2, row=4)

resultlabel = tk.Label(root, text="")

calcbutton = tk.Button(root, text='Calculate Cartesian Coordinates!', command=compute)
calcbutton.grid(column=1, row=5, columnspan=2)

root.mainloop()
