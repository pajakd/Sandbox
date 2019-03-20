import datetime # object, supplies classes for manipulating dates and times
from tkinter import * # standard Grafical User Interaces (GUI)
from PIL import Image, ImageTk,ImageDraw # Imaging Library

def display_window(days): #def - marks the start of function header which show window
    window = Tk()
    window.title("Powrót Dominika")

    image_pil = Image.open("calendar.jpeg").resize((100, 100))
    img = ImageTk.PhotoImage(image_pil)
    text =days[0]

    w = Label(window, # is a Tkinter Widget class, which is used to display text or image
                 compound=CENTER,
                 text=text,
                 image=img).pack(side="top")
    window.geometry('450x300')
    window.mainloop() # is an infinite loop to run the application, wait for an event to occur and process the event till the window is not closed
def get_list():
    today_ordinal = datetime.date.today().toordinal() # normalna liczba int
    arrival_ordinal = datetime.date(2019,4,17).toordinal()
    days = [datetime.date.fromordinal(i).isoformat() for i in range(today_ordinal,arrival_ordinal + 1)]
    return days

print(get_list())

display_window(get_list())
