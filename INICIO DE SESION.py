#Brayan Salinas y Yulieth Santana

import tkinter


nombre_usuario = "Pato"
contraseña = "123456"

def iniciarSesion():
    usuario_ingresado = entrada_usuario.get()
    contraseña_ingresada = entrada_contraseña.get()

    if usuario_ingresado == nombre_usuario and contraseña_ingresada == contraseña:
        mostrar_exito()
    else:
        mostrar_error()


ventana = tkinter.Tk() 
ventana.title("Inicio de Sesión")
ventana.geometry("350x350")


etiqueta_usuario = tkinter.Label(ventana, text="Nombre de Usuario:", bg = "gray") #Etiquetas de texto
etiqueta_usuario.pack()
entrada_usuario = tkinter.Entry(ventana, font = "Arial 12") # etiquetas de entrada
entrada_usuario.pack()

etiqueta_contraseña = tkinter.Label(ventana, text="Contraseña:", bg = "gray")
etiqueta_contraseña.pack()
entrada_contraseña = tkinter.Entry(ventana, font = "Arial 12")
entrada_contraseña.pack()

boton_inicio_sesion = tkinter.Button(ventana, text="Iniciar Sesión", command=iniciarSesion)
boton_inicio_sesion.pack()


def mostrar_exito():
    ventana_exito = tkinter.Tk()
    ventana_exito.geometry("200x200")
    ventana_exito.title("Éxito")
    etiqueta_exito = tkinter.Label(ventana_exito, text="Inicio de sesión correcto")
    etiqueta_exito.pack()


def mostrar_error():
    ventana_error = tkinter.Toplevel(ventana)
    ventana_error.title("Error")
    ventana_error.geometry("200x200")
    etiqueta_error = tkinter.Label(ventana_error, text="Usuario o contraseña incorrectos")
    etiqueta_error.pack()

ventana.mainloop()
