from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=290, height=100)
window.config(padx=60, pady=20)


def calculate_km():
    # Get the entered by user value of miles
    miles_value = entry.get()
    label_km_value.config(text=f"{float(miles_value)*1.609344}")


entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to:")
label_equal.grid(column=0, row=1)

label_km_value = Label(text=0)
label_km_value.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()
