#todo:Creacion del entorno grafico:
#importamos el modulo tkinter
from tkinter import*

#todo:ventana principal
root= Tk()
#asignamos titulo a la ventana:
root.title('Login de usuario')
root.geometry("500x350")

#todo subventana o frame de la app que va a contenr todos los elementos 
mainframe= Frame(root)
mainframe.grid(row=0,column=0)
mainframe.config(width=480, height=320,bg="blue")

#todo: Atributos de mi 
titulo= Label(mainframe, text="login de usuario", font=("Arial",24))
titulo.grid(column=0,row=0)

#todo:elementos label de usuario y contraseña
#usuario
nombreLabel=Label(mainframe,text="Usuario: ")
nombreLabel.grid(column=0, row=1)

#contraseña
contrañaLabel=Label(mainframe, text="contraseña: ")
contrañaLabel.grid(column=0, row=2)
root.mainloop()