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
-----------------------------------------------------------------------------------

#Todo: ejemplo de consulta API  
#Generalmente hoy en dia la forma de comunicar una 
#aplicacion con otra es a traves de la API(EPIA) 
#TODO: API: Es una pieza codigo que permite a diferentes aplicaciones 
#comunicarse entre si y compartir informacion y funcionalidades. 
#TODO: JSON: Es un formato (JavaScript Object Nata)
#https://random-data-api.com/api/commerce/random_commerce?size=100

#utilizaremos dos librerias de python: urllib.request-JSON

#importamos librerias
from urllib.request import urlopen
import json

url = "https://random-data-api.com/api/commerce/random_commerce?size=100"

response = urlopen(url)
#print(response) #Esto nos devuelve un objeto (atributo y metodos)
#Metodo para leer 
#print(response.read())

#Usando el modulo JSON para formatear los datos.
data= json.loads(response.read())
#print(data)

#recorro la lista
#for i in data:
#    print(i)
#    break

#recorro la lista para obtener solo el color
#for i in data:
#    print(i)
#    print(i["color"])
#    break

#Guardar todos los colores en una lista
colores=[]
for i in data:
    if i["color"]not in colores:
        colores.append(i["color"])

print(colores)
