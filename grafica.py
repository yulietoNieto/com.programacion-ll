import tkinter

ventana = tkinter.Tk() #contenedor de graficos 
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text = "hola mundo", bg= "green") # bg color del recuadro
etiqueta.pack(fill=tkinter.X) # mostrar la etiqueta, colocar el labe1 en la ventana 

cajaNumero1 = tkinter.Entry(ventana, font= "helvetica 20")
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font= "helvetica 20")
cajaNumero2.pack()

def numeroDeLaCaja():
    numero1= int(cajaNumero1.get())
    numero2= int(cajaNumero2.get())
    resulMultiplicacion= numero1*numero2
    etiquetaResult ["text"] = resulMultiplicacion
    #print("el resultado de la multiplicacion = ",resupuesta)

    

boton = tkinter.Button(ventana,text="presionar", command=numeroDeLaCaja)
boton.pack()

etiquetaResult = tkinter.Label(ventana,text="",bg="pink",font="Helvetica 20")
etiquetaResult.pack(fill=tkinter.X) #Colocar el label en la pantalla



ventana.mainloop()