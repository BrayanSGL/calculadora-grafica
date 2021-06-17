import tkinter as tk
import math
from tkinter import *
from math import *

raiz = tk.Tk()
raiz.title("Calculadora")
raiz.resizable(height=False, width=False)

operacion= ""

resultado=0


def iniciar():
    global operacion
    operacion = ""

#---------------------------Agregar números a la pantalla--------

def agregarElemento(elemento):
    global operacion
    global numeroPantalla
    operacion += str(elemento)
    numeroPantalla.set(operacion)   

#------------------------def evaluar ----------------------------

def evaluar():
    global operacion
    global numeroPantalla

    resultado = eval(numeroPantalla.get())
    numeroPantalla.set(resultado)
    operacion = str(resultado)

#---------------------Reset--------------------------------------

def reset ():
    global operacion
    global numeroPantalla
    operacion = ""
    numeroPantalla.set("")
# ------------------------Configuracion inicial de frames -------
frameGrafico = tk.Canvas(raiz, width=300, height=300, bg="Gray")
frameGrafico.grid(row=0, column=1)
frameCalculadora = tk.Canvas(raiz, width=300, height=400, bg="#8C9288")
frameCalculadora.grid(row=0, column=0, rowspan=2)

# ----------------------------Pantalla de función---------------
numeroPantalla = StringVar()
pantallafuncion = Entry(
    frameCalculadora, textvariable=numeroPantalla, width="40")
pantallafuncion.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantallafuncion.config(background="black", fg="#24F40B", justify="right")


# ------------------------------ Graficarrrrr ------------------

frameGrafico.create_line(150, 0, 150, 301)
frameGrafico.create_line(0, 150, 301, 150)

puntosX = []
puntosY = []

for i in range(300):
    puntosX.append(i+150)

for i in range(300):
    puntosY.append(i**2+150)


def dibujarPositivo(pant, x1, y1, x2, y2):
    pant.create_line(x1, y1, x2, y2)


for i in range(299):
    dibujarPositivo(frameGrafico, puntosX[i],
                    puntosY[i], puntosX[i+1], puntosY[i+1])

# ----------------------------Primera fila de botones-----------
botonX = Button(frameCalculadora, text="X", width=6, command=lambda: agregarElemento("X"))
botonX.grid(row=2, column=1, padx=5, pady=5)
botonRaiz = Button(frameCalculadora, text="√¯¯", width=6, command=lambda: agregarElemento("sqrt("))
botonRaiz.grid(row=2, column=2, padx=5, pady=5)
botonDel = Button(frameCalculadora, text="Del", width=6, command=lambda: reset())
botonDel.grid(row=2, column=3, padx=5, pady=5)
botonDiv = Button(frameCalculadora, text="/", width=6, command=lambda: agregarElemento(" / "))
botonDiv.grid(row=2, column=4, padx=5, pady=5)

# ---------------------------Segunda fila de botones------------
boton7 = Button(frameCalculadora, text="7", width=6, command=lambda: agregarElemento(7))
boton7.grid(row=3, column=1, padx=5, pady=5)
boton8 = Button(frameCalculadora, text="8", width=6, command=lambda: agregarElemento(8))
boton8.grid(row=3, column=2, padx=5, pady=5)
boton9 = Button(frameCalculadora, text="9", width=6, command=lambda: agregarElemento(9))
boton9.grid(row=3, column=3, padx=5, pady=5)
botonMult = Button(frameCalculadora, text="*", width=6, command=lambda: agregarElemento(" * "))
botonMult.grid(row=3, column=4, padx=5, pady=5)

# -------------------------Tercera fila de botones--------------
boton4 = Button(frameCalculadora, text="4", width=6, command=lambda: agregarElemento(4))
boton4.grid(row=4, column=1, padx=5, pady=5)
boton5 = Button(frameCalculadora, text="5", width=6, command=lambda: agregarElemento(5))
boton5.grid(row=4, column=2, padx=5, pady=5)
boton6 = Button(frameCalculadora, text="6", width=6, command=lambda: agregarElemento(6))
boton6.grid(row=4, column=3, padx=5, pady=5)
botonRest = Button(frameCalculadora, text="-", width=6, command=lambda: agregarElemento(" - "))
botonRest.grid(row=4, column=4, padx=5, pady=5)

# -------------------------Cuarta fila de botones--------------
boton1 = Button(frameCalculadora, text="1", width=6, command=lambda: agregarElemento(1))
boton1.grid(row=5, column=1, padx=5, pady=5)
boton2 = Button(frameCalculadora, text="2", width=6, command=lambda: agregarElemento(2))
boton2.grid(row=5, column=2, padx=5, pady=5)
boton3 = Button(frameCalculadora, text="3", width=6, command=lambda: agregarElemento(3))
boton3.grid(row=5, column=3, padx=5, pady=5)
botonSum = Button(frameCalculadora, text="+", width=6, command=lambda: agregarElemento(" + "))
botonSum.grid(row=5, column=4, padx=5, pady=5)

# -------------------------Quinta fila de botones--------------
botonPote = Button(frameCalculadora, text="**", width=6, command=lambda: agregarElemento(" ** "))
botonPote.grid(row=6, column=1, padx=5, pady=5)
boton0 = Button(frameCalculadora, text="0", width=6, command=lambda: agregarElemento(0))
boton0.grid(row=6, column=2, padx=5, pady=5)
botonComa = Button(frameCalculadora, text=".", width=6, command=lambda: agregarElemento("."))
botonComa.grid(row=6, column=3, padx=5, pady=5)
botonIgu = Button(frameCalculadora, text="=", width=6, command=lambda: evaluar())
botonIgu.grid(row=6, column=4, padx=5, pady=5)

# -------------------------Sexta fila de botones--------------
botonPeDE = Button(frameCalculadora, text="(", width=6, command=lambda: agregarElemento("("))
botonPeDE.grid(row=7, column=1, padx=5, pady=5)
botonPeIZ = Button(frameCalculadora, text=")", width=6, command=lambda: agregarElemento(")"))
botonPeIZ.grid(row=7, column=2, padx=5, pady=5)
botonCos = Button(frameCalculadora, text="Cos", width=6)
botonCos.grid(row=7, column=3, padx=5, pady=5)
botonTan = Button(frameCalculadora, text="Tan", width=6)
botonTan.grid(row=7, column=4, padx=5, pady=5)


# ---------------------------------------------------------------

iniciar()
raiz.mainloop()
