import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

# import Play

columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
filas = ["1", "2", "3", "4", "5", "6", "7", "8"]
colores = ["Blancas", "Negras"]
piezas = ["Peon", "Caballo", "Alfil", "Torre", "Reina", "Rey"]
equivalente = ["P", "N", "B", "R", "Q", "K"]
maxContador = [[8, 8], [2, 2], [1, 1]]
contadores = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
piezasGeneradas = []
global listoParaJugar


def obtenerEquivalente(nombre, pColor):
    for x in range(0, 8):
        if nombre == piezas[x]:
            if pColor == colores[0]:
                return equivalente[x].lower()
            else:
                return equivalente[x]


def readyToPlay():
    global listoParaJugar
    listoParaJugar = True
    playButon["state"] = "active"


def generarArchivo():
    print("Generar Archivo")
    try:
        encabezado = "#BEGIN \n#MAY-NEGRAS \n#MIN-BLANCAS \n# K-k : King \n# Q-q : Queen \n# N-n : Knight \n# B-b : " \
                     "Bishop \n# R-r : Rook \n# P-p : Pawn \n\n#-|A|B|C|D|E|F|G|H| \n#------------------\n"
        nuevoArchivo = open("BoardFiles/TableroDeJuego.cfl", 'w')
        nuevoArchivo.write(encabezado)
        for x in range(0, 8):
            linea = str(x + 1) + "-|"
            for y in range(0, 8):
                if piezasGeneradas[x][y] is None:
                    linea = linea + "-|"
                else:
                    linea = linea + obtenerEquivalente(piezasGeneradas[x][y][0], piezasGeneradas[x][y][1]) + "|"
            nuevoArchivo.write(linea + "\n")
        nuevoArchivo.write("\n#PLAYER TURN\n")
        if CheckVar1.get():
            nuevoArchivo.write("White\n\n#END")
        else:
            nuevoArchivo.write("Black\n\n#END")
        nuevoArchivo.close()
        readyToPlay()
    except:
        print("Error al generar")


def llenarMatriX(lista):
    for x in range(0, 8):
        listatemp = []
        for y in range(0, 8):
            listatemp.append(None)
        lista.append(listatemp)
    print(lista)


def callbackFunc(event):
    print(columnas[columna.current()])


def imprimirTablero(tablero):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for x in range(0, 8):
        print(tablero[x])


def clickedArchivo():
    generarArchivo()


def clickedJugador1():
    CheckVar2.set(not CheckVar2.get())


def clickedJugador2():
    CheckVar1.set(not CheckVar1.get())


def loadPieces(p):
    if p == 'K':
        return (piezas[5], colores[1])
    elif p == 'k':
        return (piezas[5], colores[0])
    elif (p == 'Q'):
        return (piezas[4], colores[1])
    elif (p == 'q'):
        return (piezas[4], colores[0])
    elif (p == 'N'):
        return (piezas[1], colores[1])
    elif (p == 'n'):
        return (piezas[1], colores[0])
    elif (p == 'B'):
        return (piezas[2], colores[1])
    elif (p == 'b'):
        return (piezas[2], colores[0])
    elif (p == 'R'):
        return (piezas[3], colores[1])
    elif (p == 'r'):
        return (piezas[3], colores[0])
    elif (p == 'P'):
        return (piezas[0], colores[1])
    elif (p == 'p'):
        return (piezas[0], colores[0])
    else:
        return None


def obtenerFile():
    file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(
                                          ("all files", "*.*"), ("games files", "*.cfl")))
    print(file)
    file1 = open(file, 'r')
    countx = -1
    county = 0
    while True:
        line = file1.readline()
        if not line:
            break
        if line[0] != '#':
            if line != '\n':
                if line[0] == 'W' or line[0] == 'B':
                    pass
                    print("jugador :" + line[0:5])
                else:
                    for x in range(2, 18):
                        if line[x] != '|':
                            countx += 1
                            print(county, countx, line[x])
                            piezasGeneradas[county][countx] = loadPieces(line[x])
                        if countx == 7:
                            countx = -1
                            county += 1
                        if county == 8:
                            county = 0

    file1.close()
    imprimirTablero(piezasGeneradas)
    readyToPlay()


def llamarJuego():
    print(listoParaJugar)
    if listoParaJugar:
        window.destroy()
        import Play
    # exec(open('Play.py').read())


def clicked():
    # lbl.configure(text="Button was clicked !!")
    correcto = False
    print(contadores)
    if piezasGeneradas[fila.current()][columna.current()] is None:
        if nombrePieza.current() == 0:
            if contadores[nombrePieza.current()][colorPiezas.current()] < maxContador[0][
                colorPiezas.current()]:  # Peones
                contadores[nombrePieza.current()][colorPiezas.current()] = contadores[nombrePieza.current()][
                                                                               colorPiezas.current()] + 1
                correcto = True
        elif nombrePieza.current() > 3:
            if contadores[nombrePieza.current()][colorPiezas.current()] < maxContador[2][
                colorPiezas.current()]:  # reina y rey
                contadores[nombrePieza.current()][colorPiezas.current()] = contadores[nombrePieza.current()][
                                                                               colorPiezas.current()] + 1
                correcto = True
        else:
            if contadores[nombrePieza.current()][colorPiezas.current()] < maxContador[1][
                colorPiezas.current()]:  # Demas piezas
                contadores[nombrePieza.current()][colorPiezas.current()] = contadores[nombrePieza.current()][
                                                                               colorPiezas.current()] + 1
                correcto = True
        if correcto:
            texto.insert(END,
                         "Insercion " + piezas[nombrePieza.current()] + " " + colores[colorPiezas.current()] + "-" +
                         columnas[columna.current()] + filas[fila.current()] + "\n")
    else:

        texto.insert(END, "Reemplazo " + piezas[nombrePieza.current()] + " " + colores[colorPiezas.current()] + "-" +
                     columnas[columna.current()] + filas[fila.current()] + "\n")

    if correcto:
        piezasGeneradas[fila.current()][columna.current()] = (
            piezas[nombrePieza.current()], colores[colorPiezas.current()])

    # print(piezasGeneradas).
    imprimirTablero(piezasGeneradas)
    print(contadores)


##Inicio de declaraciones y de programa
listoParaJugar = False
llenarMatriX(piezasGeneradas)
window = Tk()

window.title("Ajedrez IA")

window.geometry('1000x800')

# Declaracion de los componentes
texto = Text(window, width=40)
n = StringVar()
nn = StringVar()
cp = StringVar()
pn = StringVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
columna = Combobox(window, width=27, textvariable=n)
fila = Combobox(window, width=27, textvariable=nn)
colorPiezas = Combobox(window, width=27, textvariable=cp)
nombrePieza = Combobox(window, width=27, textvariable=pn)
columna['values'] = columnas
fila['values'] = filas
colorPiezas['values'] = colores
nombrePieza['values'] = piezas
lbl = Label(window, text="Eventos de Configuración")
btn = Button(window, text="Agregar Pieza", command=clicked)
btn2 = Button(window, text="Grabar archivo", command=clickedArchivo)
C1 = Checkbutton(window, text="Inicia jugador Blanco", variable=CheckVar1, onvalue=True, offvalue=False, height=5,
                 width=20, command=clickedJugador1)
C2 = Checkbutton(window, text="Inicia jugador Negro", variable=CheckVar2,
                 onvalue=True, offvalue=False, height=5,
                 width=20, command=clickedJugador2)
botonFile = Button(window, text="Cargar tablero de archivo", command=obtenerFile)
playButon = Button(window, text="A jugar", command=llamarJuego)
# ubicacion de los componentes
lbl.pack(padx=0, pady=0)
texto.pack(side=LEFT, fill=Y, padx=20, pady=10)
C1.pack()
C2.pack()
columna.pack(padx=40, pady=10)
fila.pack(padx=40, pady=10)
colorPiezas.pack(padx=40, pady=10)
nombrePieza.pack(padx=40, pady=10)
texto.pack(padx=40, pady=10)
btn.pack(padx=40, pady=10)
btn2.pack(padx=40, pady=10)
CheckVar1.set(True)
botonFile.pack(padx=40, pady=10)
playButon.pack(padx=40, pady=10)
playButon["state"] = "disabled"
'''
columna.grid(column=3, row=15)
fila.grid(column=3, row=25)
colorPiezas.grid(column=3, row=35)
nombrePieza.grid(column=3, row=45)
texto.grid(column=0, row=15)'''
# Set Values
columna.current(0)
fila.current(0)
colorPiezas.current(0)
nombrePieza.current(0)
columna.bind("<<ComboboxSelected>>", callbackFunc)

window.mainloop()
