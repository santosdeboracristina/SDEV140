# Student: Debora Santos
# Class: SDEV140 / Instructor: Patrick Scherrer
# Final Project: This app allows the user to
# pull up the exchange rate for Dollar, Euro and Bitcoin
# considering brazilian Reais in real time.
# ----------------------------------------------

import requests
from tkinter import * #Importing all from Tkinter library
from tkinter.ttk import *

# Function that will get the exchange rate
def get_rate():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    request_dic = request.json()

    dolar_rate = request_dic['USDBRL']['bid']
    euro_rate = request_dic['EURBRL']['bid']
    btc_rate = request_dic['BTCBRL']['bid']

    text_answer['text'] = f'''
    Dolar: {dolar_rate}
    Euro: {euro_rate}
    BTC: {btc_rate}'''

# Creating the only window for the app
window1 = Tk()

# Creating the title for the main window (window1)
window1.title("My Exchange Rate App")

# Creating the photo next to the exchange button for the main window (window1)
photo1 = PhotoImage(file = r"debora.png")
photoimage = photo1.subsample(3,3)

# Creates the first label in the main window:
text = Label(window1, text="Click bellow to get updated Exchange Rates")

# Adjusts the position of the first label:
text.grid(column=0, row=0, padx=10, pady=10)

btn1 = Button(window1, text="Get Exchange Rate", image = photoimage, compound = LEFT,  command=get_rate)
# Adjusts the position of the first using grid:
btn1.grid(column=0, row=1, padx=10, pady=10)

# Creates the answer label in the main window where the exchange rates will be displayed:
text_answer = Label(window1, text="")
text_answer.grid(column=0, row=2, padx=10, pady=10)

# Creating the photo next to the exchange button for the main window (window1)
photo2 = PhotoImage(file=r"debora2.png")
photoimage2 = photo2.subsample(3,3)

#Creating the close window button using the command destroy:
btn_close = Button(window1, text="Close",image = photoimage2, compound = RIGHT, command=window1.destroy)

# Adjusts the position of the first button using grid:
btn_close.grid(column=0, row=3, padx=10, pady=10)

# Creates the credits label displayed on the bottom of the window:
credits = Label(window1, text="By Debora Santos")
credits.grid(column=0, row=10, padx=10, pady=10)

#Main loop will let us see the window and keep it opened until we close it.
window1.mainloop()