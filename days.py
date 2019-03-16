import datetime
from tkinter import *
from PIL import Image, ImageTk,ImageDraw

def display_window(days):
    window = Tk()
    window.title("Powrót Dominika")

    image_pil = Image.open("calendar.jpeg").resize((100, 100))
    img = ImageTk.PhotoImage(image_pil)
    text =days[0]

    w = Label(window,
                 compound=CENTER,
                 text=text,
                 image=img).pack(side="top")
    window.geometry('450x300')
    window.mainloop()


def get_list():
    today_ordinal = datetime.date.today().toordinal() # normalna liczba int
    arrival_ordinal = datetime.date(2019,4,17).toordinal()
    days = [datetime.date.fromordinal(i).isoformat() for i in range(today_ordinal,arrival_ordinal + 1)]
    return days

print(get_list())

display_window(get_list())
