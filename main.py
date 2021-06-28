import tkinter as tk
import math
from tkinter import *
from math import *

raiz = tk.Tk()
raiz.title("Calculadora A&B 2021")
raiz.resizable(height=False, width=False)

operacion = ""

resultado = 0


def iniciar():
    global operacion
    operacion = ""
    global modo
    modo = False


# ----------------------------Cambiar de modo---------------------

def cambiarModo(mod):
    global modo
    if mod == 1:
        planoCar()
        reset()
        modo = True
        botonX["state"] = "normal"
        botonFX["state"] = "normal"
        botonIgu["state"] = "disable"
    else:
        modo = False
        frameGrafico.delete("all")
        planoCar()
        reset()
        botonX["state"] = "disable"
        botonFX["state"] = "disable"
        botonIgu["state"] = "normal"
# ---------------------------Agregar números a la pantalla--------


def agregarElemento(elemento):
    global operacion
    global numeroPantalla
    operacion += str(elemento)
    numeroPantalla.set(operacion)

# ------------------------def evaluar ----------------------------


def evaluar(x="operacion"):
    global operacion
    resultado = operacion
    if x != "operacion":
        resultado = operacion.replace("x", "("+str(x)+")")

    resultado = compile(resultado, "<string>", "eval")
    try:
        resultado = eval(resultado)
    except:
        resultado = 9999999999999999999999999999999999999999999999

    return resultado


def igual():
    global operacion
    global numeroPantalla
    r = evaluar()
    if r == 9999999999999999999999999999999999999999999999:
        numeroPantalla.set("Error matemático")
    else:
        numeroPantalla.set(evaluar())
    operacion = numeroPantalla.get()
# ---------------------Reset--------------------------------------


def reset():
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
def convertirPunto(x, y):
    Punto = []
    Punto.append(x*30+150)
    Punto.append(150-y*30)
    return Punto


def graficar():
    global modo
    if modo:
        puntosX = []
        puntosY = []

        puntosX.append(-5)
        puntosY.append(evaluar(-5))

        for i in range(1, 101):
            puntosX.append(puntosX[i-1]+0.1)
            puntosY.append(evaluar(puntosX[i]))
            punto1 = convertirPunto(puntosX[i-1], puntosY[i-1])
            punto2 = convertirPunto(puntosX[i], puntosY[i])
            frameGrafico.create_line(
                punto1[0], punto1[1], punto2[0], punto2[1])

#----------------------------Plano Cartesiano-------------------

def planoCar ():
    frameGrafico.create_line(150, 0, 150, 300)
    frameGrafico.create_line(0, 150, 300, 150)
    #positivasY
    frameGrafico.create_line(140,120,160,120)
    frameGrafico.create_line(140,90,160,90)
    frameGrafico.create_line(140,60,160,60)
    frameGrafico.create_line(140,30,160,30)
    #negativasY
    frameGrafico.create_line(140,180,160,180)
    frameGrafico.create_line(140,210,160,210)
    frameGrafico.create_line(140,240,160,240)
    frameGrafico.create_line(140,270,160,270)
    #positivasX
    frameGrafico.create_line(180,140,180,160)
    frameGrafico.create_line(210,140,210,160)
    frameGrafico.create_line(240,140,240,160)
    frameGrafico.create_line(270,140,270,160)
    #negativasX
    frameGrafico.create_line(120,140,120,160)
    frameGrafico.create_line(90,140,90,160)
    frameGrafico.create_line(60,140,60,160)
    frameGrafico.create_line(30,140,30,160)

# ----------------------------Primera fila de botones-----------
botonX = Button(frameCalculadora, text=" x", width=6,
                command=lambda: agregarElemento("x"))
botonX.grid(row=2, column=1, padx=5, pady=5)
botonRaiz = Button(frameCalculadora, text="√¯¯", width=6,
                   command=lambda: agregarElemento("sqrt("))
botonRaiz.grid(row=2, column=2, padx=5, pady=5)
botonDel = Button(frameCalculadora, text="Del",
                  width=6, command=lambda: reset())
botonDel.grid(row=2, column=3, padx=5, pady=5)
botonDiv = Button(frameCalculadora, text="/", width=6,
                  command=lambda: agregarElemento(" / "))
botonDiv.grid(row=2, column=4, padx=5, pady=5)

# ---------------------------Segunda fila de botones------------
boton7 = Button(frameCalculadora, text="7", width=6,
                command=lambda: agregarElemento(7))
boton7.grid(row=3, column=1, padx=5, pady=5)
boton8 = Button(frameCalculadora, text="8", width=6,
                command=lambda: agregarElemento(8))
boton8.grid(row=3, column=2, padx=5, pady=5)
boton9 = Button(frameCalculadora, text="9", width=6,
                command=lambda: agregarElemento(9))
boton9.grid(row=3, column=3, padx=5, pady=5)
botonMult = Button(frameCalculadora, text="*", width=6,
                   command=lambda: agregarElemento(" * "))
botonMult.grid(row=3, column=4, padx=5, pady=5)

# -------------------------Tercera fila de botones--------------
boton4 = Button(frameCalculadora, text="4", width=6,
                command=lambda: agregarElemento(4))
boton4.grid(row=4, column=1, padx=5, pady=5)
boton5 = Button(frameCalculadora, text="5", width=6,
                command=lambda: agregarElemento(5))
boton5.grid(row=4, column=2, padx=5, pady=5)
boton6 = Button(frameCalculadora, text="6", width=6,
                command=lambda: agregarElemento(6))
boton6.grid(row=4, column=3, padx=5, pady=5)
botonRest = Button(frameCalculadora, text="-", width=6,
                   command=lambda: agregarElemento("- "))
botonRest.grid(row=4, column=4, padx=5, pady=5)

# -------------------------Cuarta fila de botones--------------
boton1 = Button(frameCalculadora, text="1", width=6,
                command=lambda: agregarElemento(1))
boton1.grid(row=5, column=1, padx=5, pady=5)
boton2 = Button(frameCalculadora, text="2", width=6,
                command=lambda: agregarElemento(2))
boton2.grid(row=5, column=2, padx=5, pady=5)
boton3 = Button(frameCalculadora, text="3", width=6,
                command=lambda: agregarElemento(3))
boton3.grid(row=5, column=3, padx=5, pady=5)
botonSum = Button(frameCalculadora, text="+", width=6,
                  command=lambda: agregarElemento("+ "))
botonSum.grid(row=5, column=4, padx=5, pady=5)

# -------------------------Quinta fila de botones--------------
botonPote = Button(frameCalculadora, text="**", width=6,
                   command=lambda: agregarElemento(" ** "))
botonPote.grid(row=6, column=1, padx=5, pady=5)
boton0 = Button(frameCalculadora, text="0", width=6,
                command=lambda: agregarElemento(0))
boton0.grid(row=6, column=2, padx=5, pady=5)
botonComa = Button(frameCalculadora, text=".", width=6,
                   command=lambda: agregarElemento("."))
botonComa.grid(row=6, column=3, padx=5, pady=5)
botonIgu = Button(frameCalculadora, text="=",
                  width=6, command=lambda: igual())
botonIgu.grid(row=6, column=4, padx=5, pady=5)

# -------------------------Sexta fila de botones--------------
botonPeDE = Button(frameCalculadora, text="(", width=6,
                   command=lambda: agregarElemento("("))
botonPeDE.grid(row=7, column=1, padx=5, pady=5)
botonPeIZ = Button(frameCalculadora, text=")", width=6,
                   command=lambda: agregarElemento(")"))
botonPeIZ.grid(row=7, column=2, padx=5, pady=5)
botonSen = Button(frameCalculadora, text="Sen", width=6,
                  command=lambda: agregarElemento("sin("))
botonSen.grid(row=7, column=3, padx=5, pady=5)
botonCos = Button(frameCalculadora, text="Cos", width=6,
                  command=lambda: agregarElemento("cos("))
botonCos.grid(row=7, column=4, padx=5, pady=5)

# -------------------------Septima fila de botones--------------
botonFX = Button(frameCalculadora, text="f(x)",
                 width=6, command=lambda: graficar())
botonFX.grid(row=8, column=1, padx=5, pady=5)
botonLog = Button(frameCalculadora, text="Ln", width=6,
                  command=lambda: agregarElemento("log("))
botonLog.grid(row=8, column=2, padx=5, pady=5)
botonTan = Button(frameCalculadora, text="Tan", width=6,
                  command=lambda: agregarElemento("tan("))
botonTan.grid(row=8, column=3, padx=5, pady=5)
botonGraf = Button(frameCalculadora, text="GRAF", width=6,
                   command=lambda: cambiarModo(1))
botonGraf.grid(row=8, column=4, padx=5, pady=5)

# -------------------------Octaba fila de botones--------------
botonAC = Button(frameCalculadora, text="AC", width=18,
                 command=lambda: cambiarModo(0))
botonAC.grid(row=9, column=1, padx=5, pady=5, columnspan=4)

# ---------------------Loop principal------------------------

iniciar()
raiz.mainloop()