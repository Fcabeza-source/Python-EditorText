from tkinter import *
from tkinter import filedialog as FileDialog

ruta=""# ruta de un fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0,"end")
    root.title("Mi editor")
def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = FileDialog.askopenfilename(initialdir='.',
                                      filetype=(("Ficheros de texto","*.txt"),),
                                      title="Abrir un fichero")

    if ruta != "":
        fichero = open(ruta,"r")
        contenido = fichero.read()
        texto.delete(1.0,"end")
        texto.insert('insert',contenido)
        fichero.close()
        root.title(ruta + "- Mi editor" )

def guardar():
    mensaje.set("Guardar Fichero")
    if ruta !="":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Se ha Guardado un  Fichero")
    else:
        guardar_como()
def guardar_como():
    global ruta
    mensaje.set("Guardar Fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w",  defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""


#Configuracion Raiz
root = Tk()

#Menu superior
menubar = Menu(root)
archivomenu = Menu(menubar , tearoff=0)
archivomenu.add_command(label = "Nuevo" , command=nuevo)
archivomenu.add_command(label = "Abrir", command=abrir)
archivomenu.add_command(label = "Guardar", command = guardar)
archivomenu.add_command(label = "Guardar como", command = guardar_como)
archivomenu.add_separator()
archivomenu.add_command(label = "Salir" , command = root.quit)
menubar.add_cascade(menu = archivomenu , label = "Archivo")

#Caja de texto
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Arial",12))


#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje , justify="left")
monitor.pack(side = "left")


root.config(menu=menubar)
#Bucle de la aplicacion
root.mainloop()
