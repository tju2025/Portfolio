import re
from tkinter import *
from tkinter import ttk 
vc = {
  "A1":"Pringles c&o", "A2":"Pringles s&v", "A3":"Pringles rs",
  "A4":"Pringles pc", "A5":"Pringles sc&o",
  "B1":"Doritos tc", "B2":"Doritos ch", "B3":"Walkers c&o",
  "B4":"Walkers s&v", "B5":"Walkers pc",
  "C1":"Mars", "C2":"Twix", "C3":"Kitkat",
  "C4":"Twirl", "C5":"Galaxy",
  "D1":"Milkyway", "D2":"Malteser", "D3":"Blue ribbon",
  "D4":"Eclair", "D5":"Double decker",
  "E1":"Oasis", "E2":"Vimto", "E3":"Rubicon",
  "E4":"Ribena", "E5":"Juice burst",
  "F1":"Coca cola", "F2":"Coca cola cherry", "F3":"Pepsi",
  "F4":"Sprite", "F5":"Dr. pepper"
} #vending machine contents
vcp = {
  "Pringles c&o":"2.00", "Pringles s&v":"2.00",
  "Pringles rs":"2.00", "Pringles pc":"2.00",
  "Pringles sc&o":"2.00",
  "Doritos tc":"2.00", "Doritos ch":"2.00",
  "Walkers c&o":"2.30", "Walkers s&v":"2.30", "Walkers pc":"2.30",
  "Mars":"0.75", "Twix":"0.60", "Kitkat":"0.70", "Twirl":"0.50",
  "Galaxy":"0.65", "Milkyway":"0.65", "Malteser":"0.65",
  "Blue riband":"0.20", "Eclair":"0.70", "Double decker":"0.70",
  "Oasis":"1.50", "Vimto":"1.00", "Rubicon":"0.70",
  "Ribena":"1.45", "Juice burst":"1.00",
  "Coca cola":"1.00", "Coca cola cherry":"1.25", "Pepsi":"1.00",
  "Sprite":"0.65", "Dr pepper":"0."
} #vending machine content price
def vend(*args):
  pattern = r"[A-F][1-5]"
  if (re.match(pattern, (location.get()))):
    value = str(location.get())
    i = vc[value]
    item.set(i)
    price.set("£"+ str(vcp[i]))
  else:
    item.set("Format:\"A-F,1-5\", e.g. A4")
    price.set("")
root = Tk()
root.title("Vending machine")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, S, E, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
item = StringVar()
item_disp = ttk.Label(mainframe, textvariable=item).grid(column=0, row=0, sticky=(N, W))
location = StringVar()
location_name = ttk.Entry(mainframe, width=29, textvariable=location)
location_name.grid(column=0, row=1, padx = 10, pady = 5)
ttk.Button(mainframe,  text="Enter", command=vend).grid(column=0, row=2)
price = StringVar()
price_disp = ttk.Label(mainframe, textvariable=price).grid(column=0, row=0, sticky=(N, E))
root.bind("<Return>", vend)
root.mainloop()