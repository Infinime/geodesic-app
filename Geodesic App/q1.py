import tkinter as tk
import math

root = tk.Tk()
root.title("Converter")

a = 6375137
f = 1/298.257223563

label1 = tk.Label(root, text=" Input the Cartesian coordinates: ")
label1.grid(column=1, row=1, columnspan=2)

xlabel = tk.Label(root, text="x:")
xentry = tk.Entry(root)
xlabel.grid(column=1, row=2)
xentry.grid(column=2, row=2)

ylabel = tk.Label(root, text="y:")
yentry = tk.Entry(root)
ylabel.grid(column=1, row=3)
yentry.grid(column=2, row=3)

zlabel = tk.Label(root, text="z:")
zentry = tk.Entry(root)
zlabel.grid(column=1, row=4)
zentry.grid(column=2, row=4)

calcbutton = tk.Button(root, text='Calculate Geodetic Coordinates!')
calcbutton.grid(column=1, row=5, columnspan=2)

root.mainloop()
