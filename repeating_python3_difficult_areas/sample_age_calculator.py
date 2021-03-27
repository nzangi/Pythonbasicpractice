import datetime
import tkinter as tk
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ")

# labels
name_label = tk.Label(text="Name")
name_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=3)

date_label = tk.Label(text="Day")
date_label.grid(column=0, row=4)

# entry_fields
name_entry = tk.Entry()
name_entry.grid(column=1, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)

date_entry = tk.Entry()
date_entry.grid(column=1, row=4)


def my_main_function():
    name = name_entry.get()
    my_names = Person(name, datetime.date(int(year_entry.get()), int(month_entry.get()), int(date_entry.get())))
    text_area = tk.Text(master=window, height=15, width=25)
    text_area.grid(column=1, row=6)
    answer = " Hey {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=my_names.age())
    text_area.insert(tk.END, answer)


# button
button = tk.Button(window, text="Calculate Age", command=my_main_function, bg="pink")
button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


# image
image = Image.open('castle.png')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

window.mainloop()
