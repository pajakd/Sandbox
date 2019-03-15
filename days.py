import datetime
from tkinter import *
from PIL import Image, ImageTk,ImageDraw

def display_window(days):
    pass

def get_list():
    today_ordinal = datetime.date.today().toordinal() # normalna liczba int
    arrival_ordinal = datetime.date(2019,4,17).toordinal()
    days = [datetime.date.fromordinal(i).isoformat() for i in range(today_ordinal,arrival_ordinal + 1)]
    return days

print(get_list())
