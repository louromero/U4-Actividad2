from tkinter import *
from tkinter import ttk
import requests

class Aplicacion:
    __ventana=None
    __dolares=None
    __total=None

    def __init__ (self):
        self.__ventana=Tk()
        self.__ventana.geometry('300x115')
        self.__ventana.title("Conversor de moneda")
        self.__ventana.resizable(True,False)

        mainFrame=ttk.Frame(self.__ventana,padding="20 20 50 50")
        mainFrame.grid(column=0,row=0,sticky=(N,W,E,S))

        mainFrame.columnconfigure(0,weight=1)
        mainFrame.rowconfigure(0,weight=1)

        mainFrame['borderwidth']=2
        mainFrame['relief']='sunken'

        self.__dolares=StringVar()
        self.__dolares.trace("w",self.setDolar)
        self.__total=StringVar()


        #ENTRADA
        self.dolaresEntry=ttk.Entry(mainFrame,width=10, textvariable=self.__dolares)
        self.dolaresEntry.grid(row=1,column=2,sticky=(W,E))

        #PALABRAS
        ttk.Label(mainFrame,text='Dolares').grid(column=3,row=1,sticky=W)
        ttk.Label(mainFrame,text='Es equivalente a: $').grid(column=1,row=2,sticky=E)
        ttk.Label(mainFrame,text='Pesos').grid(column=3,row=2,sticky=W)

        #LABEL TOTAL
        ttk.Label(mainFrame,textvariable=self.__total).grid(column=2,row=2,sticky=(W,E))

        #BOTON SALIR
        ttk.Button(mainFrame,text='Salir',command=self.__ventana.destroy).grid(column=3,row=3,sticky=W)

        #PARA BUSCAR API
        self.__dolares.trace('r',self.setDolar)
        self.__response=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")

        self.__ventana.mainloop()


    #CALCULAR
    def setDolar(self,*args):
        precioDolar=float(self.__response.json()[0]["casa"]["venta"].replace(",","."))
        try:
            pesos="{:,.2f}".format(precioDolar*float(self.__dolares.get()))
            self.__total.set(pesos)
        except:
            self.__total.set(" ")