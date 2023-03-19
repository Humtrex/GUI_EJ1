#Humberto Hernández Trejo

from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("600x450")

#barra
barra = ttk.Notebook(raiz)

frameADD = ttk.Frame(barra)
frameDelete = ttk.Frame(barra)
frameSearch = ttk.Frame(barra)
frameService = ttk.Frame(barra)
frameHelp = ttk.Frame(barra)


barra.pack(expand=True, fill="both")

barra.add(frameADD, text=    "    Add    ")
barra.add(frameDelete, text= "  Delete  ")
barra.add(frameSearch, text= "  Search   ")
barra.add(frameService, text="  Service   ")
barra.add(frameHelp, text=   "   Help    ")

style = ttk.Style()
style.theme_create("barra", parent="alt", settings={
    "TNotebook.Tab": {"configure": {"background": "deep sky blue", "foreground": "black", "font": ("Arial", 20)}},
    "TRadiobutton": {"configure": { "foreground": "black", "font": ("Arial", 15)}},
    "TButton": {"configure": { "foreground": "black", "font": ("Arial", 15), "relief":"ridge"}}
})
style.theme_use("barra")

#frames
mainframe = ttk.Frame(frameADD, padding="0 25 0 0")
mainframe.grid(column=0, row= 0)

datosFrame = ttk.Frame(mainframe, width=450, height=600, padding="30 5 100 5", relief="groove")
datosFrame.grid(column=0, row=1)
#frames en datos
birthFrame = ttk.Frame(datosFrame)
birthFrame.grid(column=0, row=2,columnspan=2, sticky=(W), padx=5, pady=5)
fechaFrame = ttk.Frame(birthFrame)
fechaFrame.grid(column=1, row=2, sticky=(W), padx=5, pady=5) 
coFrame = ttk.Frame(datosFrame)
coFrame.grid(column=2, row=2,columnspan=2, sticky=(W), padx=5, pady=5) 

creditFrame = ttk.Frame(mainframe,width=450,height=600, padding="30 5 115 15", relief="groove")
creditFrame.grid(column=0, row=2, sticky=())
#frames en credit
creFrame = ttk.Frame(creditFrame)
creFrame.grid(column=0,row=0,sticky=(W),columnspan=2, padx=5, pady=5)
tarjrame = ttk.Frame(creditFrame)
tarjrame.grid(column=1,row=2,sticky=(W), padx=5, pady=5)

roomFrame = ttk.Frame(mainframe, width=450,height=600, padding="30 5 42 5", relief="groove")
roomFrame.grid(column=0, row=3, sticky=(W))
#frames en room
tipoFrame = ttk.Frame(roomFrame)
tipoFrame.grid(column=1,row=0,sticky=(N), padx=10)

botonFrame = ttk.Frame(mainframe,width=450,height=600, padding="220 20 275 40", relief="groove")
botonFrame.grid(column=0, row=4, sticky=())
#datos
FirstN = StringVar()
LastN = StringVar()
Country = StringVar()
Dia = IntVar()
Mes = IntVar()
Año = IntVar()
#credit
Credit = IntVar()
#days
Days = IntVar()
#labels datos
ttk.Label(datosFrame, text="First Name: ",font=("Arial", 15)).grid(column=0, row=0,sticky=(W))
ttk.Label(datosFrame, text="Last Name:",font=("Arial", 15)).grid(column=2, row=0,sticky=(W),padx=5)
ttk.Label(datosFrame, text=" ",font=("Arial", 15)).grid(column=0, row=1, sticky=(W))
ttk.Label(birthFrame, text="Birth Date:",font=("Arial", 15)).grid(column=0, row=2, sticky=(W))
ttk.Label(coFrame, text="Country:",font=("Arial", 15)).grid(column=2, row=2, sticky=(W), padx=5)
#labels credit
ttk.Label(creFrame, text="Credit Card(if any):",font=("Arial", 15)).grid(column=0,row=0,sticky=(W))
ttk.Label(creditFrame, text=" ",font=("Arial", 5)).grid(column=0, row=1, sticky=(W))
ttk.Label(creditFrame, text=" Credit Card Type(if any): ",font=("Arial", 15)).grid(column=0, row=2,sticky=(W), pady=2)
#labels room
ttk.Label(roomFrame,text="Room Type:",font=("Arial", 15)).grid(column=0,row=0,sticky=(W,N))
ttk.Label(roomFrame,text="      ",font=("Arial", 15)).grid(column=2,row=0,sticky=(W,N))
ttk.Label(roomFrame,text="Total Staying Time(days):",font=("Arial", 15)).grid(column=3,row=0,sticky=(N,E))
#entry datos
FNEntry = ttk.Entry(datosFrame, textvariable=FirstN, width=11,font=("Arial", 13)).grid(column=1, row=0, sticky=(W),padx=5)
LNEntry = ttk.Entry(datosFrame, textvariable=LastN, width=13,font=("Arial", 13)).grid(column=3, row=0, sticky=(W),padx=5)
CountryEntry = ttk.Entry(coFrame,textvariable=Country, width=10,font=("Arial", 13)).grid(column=3, row=2, sticky=(W))
DayEntry = ttk.Entry(fechaFrame,textvariable=Dia, width=2,font=("Arial", 12)).grid(column=0, row=0, sticky=(W))
MesEntry = ttk.Entry(fechaFrame,textvariable=Mes, width=2,font=("Arial", 12)).grid(column=1, row=0, sticky=(W), padx=2)
AñoEntry = ttk.Entry(fechaFrame,textvariable=Año,width=4,font=("Arial", 12)).grid(column=2, row=0,sticky=(W), padx=2)
#entry credit
CreditEntry = ttk.Entry(creFrame, textvariable=Credit, width=12,font=("Arial", 14)).grid(column=1, row=0, sticky=(W))
#entry room
daysEntry = ttk.Entry(roomFrame,textvariable=Days,width=3,font=("Arial", 14)).grid(column=4,row=0,sticky=(NE))
#radiobutton credit
ttk.Radiobutton(tarjrame, text="Visa     ").grid(column=1, row=2, sticky=(W))
ttk.Radiobutton(tarjrame, text="MasterCard").grid(column=2, row=2, sticky=(W))
#radiobutton room
ttk.Radiobutton(tipoFrame, text="Normal").grid(column=0, row=1, sticky=(W))
ttk.Radiobutton(tipoFrame, text="Familiar").grid(column=0, row=2, sticky=(W))
ttk.Radiobutton(tipoFrame, text="Special").grid(column=0, row=3, sticky=(W))
#boton
ttk.Button(botonFrame, text="Submit",padding="10 0 28 6").grid(sticky=())

raiz.mainloop()