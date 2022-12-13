from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=60, pady=100)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km_calc = Label()
label_km_calc.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Text input
input = Entry(width=10)
input.grid(column=1, row=0)

# button
def calculate():
    output = float(input.get()) * 1.6
    label_km_calc.config(text=int(output))

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.mainloop()