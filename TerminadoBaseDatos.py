import pymysql
import sys
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

#FUNCIONES
def conexionBBDD():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
	cursor=conexion.cursor()

	try:

		cursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER VARCHAR(50),
			NOMBRE VARCHAR (50),
			APELLIDO VARCHAR(50),
			FISICA VARCHAR(2),
			MATEMATICA VARCHAR(2),
			SOCIALES VARCHAR(2),
			LENGUAJE VARCHAR(2))
			''')
	
		messagebox.showinfo("BBDD","BBDD CREADA CON EXITO")

	except:

		messagebox.showwarning("¡ATENCION!","LA BASE YA EXISTE")




def salirAplicacion():
	 valor=messagebox.askquestion("salir","Deseas salir de la aplicacion")
	 if valor=="yes":
	 	ventana.destroy()


def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miFisica.set("")
	miMatematica.set("")
	miSociales.set("")
	miLenguaje.set("")


def crearNuevo():
	
	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
	cursor=conexion.cursor()

	
	cursor.execute("INSERT INTO nuevabase VALUES('"+miId.get() +
		"','"+miNombre.get() +
		"','"+miApellido.get() +
		"','"+miFisica.get() +
		"','"+miMatematica.get() +
		"','"+miSociales.get() +
		"','"+miLenguaje.get() +"')")



	conexion.commit()

	messagebox.showinfo("BBDD","REGISTRO INSERTADO CON EXITO")

def leer():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
	cursor=conexion.cursor()

	cursor.execute("SELECT * FROM nuevabase WHERE ID ="+miId.get())

	elUsuario=cursor.fetchall()

	for usuario in elUsuario:

		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miApellido.set(usuario[2])
		miFisica.set(usuario[3])
		miMatematica.set(usuario[4])
		miSociales.set(usuario[5])
		miLenguaje.set(usuario[6])

	conexion.commit()	

def actualizar():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
	cursor=conexion.cursor()

	cursor.execute("UPDATE nuevabase SET nombre ='"+miNombre.get() +
		"',apellido ='"+miApellido.get() +
		"',fisica ='"+miFisica.get() +
		"',matematica ='"+miMatematica.get() +
		"', sociales ='"+miSociales.get() +
		"',lenguaje ='"+miLenguaje.get() +
		"' WHERE Id = "+miId.get())
	
	conexion.commit()
	messagebox.showinfo("BBDD","REGISTRO INSERTADO CON EXITO")	

def eliminar():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
	cursor=conexion.cursor()

	cursor.execute("DELETE FROM nuevabase WHERE Id = "+ miId.get())
	conexion.commit()

	messagebox.showinfo("BBDD", "REGISTRO BORRADO CON EXITOS")



#INTERDAZ GRAFICA
ventana= Tk()

barraMenu = Menu(ventana)
ventana.config(menu=barraMenu, width=800, height=800)

#MENUS ADICIONALES
bbddMenu=Menu(barraMenu,tearoff=0) #TEAROFF UTILIZACION PARA ELEMINAR LA ESTETICA
bbddMenu.add_command(label="Conectar", command=conexionBBDD) #CONECTAR BASE DE DATOS 
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0) 
borrarMenu.add_command(label="Borrar Campos", command = limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0) 
crudMenu.add_command(label="Crear", command = crearNuevo)
crudMenu.add_command(label="leer", command = leer)
crudMenu.add_command(label="actualizar", command = actualizar)
crudMenu.add_command(label="Borrar", command = eliminar)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

#-------COMIENZO DE CAMPOS---------

miFrame=Frame(ventana)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miFisica=StringVar()
miMatematica=StringVar()
miSociales=StringVar()
miLenguaje=StringVar()


cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10, pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2,column=1,padx=10, pady=10)

cuadroFisica=Entry(miFrame, textvariable=miFisica)
cuadroFisica.grid(row=3,column=1,padx=10, pady=10)

cuadroMatematica=Entry(miFrame,textvariable=miMatematica)
cuadroMatematica.grid(row=4,column=1,padx=10, pady=10)

cuadroSociales=Entry(miFrame,textvariable=miSociales)
cuadroSociales.grid(row=5,column=1,padx=10, pady=10)

cuadroLenguaje=Entry(miFrame,textvariable=miLenguaje)
cuadroLenguaje.grid(row=6,column=1,padx=10, pady=10)



#COMENZAMOS A ETIQUETAR

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0,column=0,sticky="e",padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10, pady=10)

fisicaLabel=Label(miFrame, text="Fisica:")
fisicaLabel.grid(row=3,column=0,sticky="e",padx=10, pady=10)

matematicaLabel=Label(miFrame, text="Matematica:")
matematicaLabel.grid(row=4,column=0,sticky="e",padx=10, pady=10)

socialesLabel=Label(miFrame, text="Sociales:")
socialesLabel.grid(row=5,column=0,sticky="e",padx=10, pady=10)

lenguajeLabel=Label(miFrame, text="Lenguaje:")
lenguajeLabel.grid(row=6,column=0,sticky="e",padx=10, pady=10)



#CREACION DE BOTONES

miFrame2=Frame()
miFrame2.pack()

botonCrear=Button(miFrame2,text="Nuevo", command = crearNuevo)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer", command = leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar", command = actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Borrar", command =eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)








ventana.mainloop()