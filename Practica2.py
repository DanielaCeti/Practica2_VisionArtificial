from ast import Try
import cv2
import numpy as np
import PIL
from PIL import ImageTk
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter import ttk
import imutils
import keyboard
import math as ma

opc=0
#image = Non

def operaciones():
    
    img1 = cv2.imread('badbunny.jpg')
    img2 = cv2.imread('danielricciardo.jpg')
    #print (img1)
    #print("-------------------")
    #print (img2)
    #print("-------------------")
    global opc

    opc = opc+1
    print("Presionaste la d contador:",opc)
    if opc == 1:
        etiqueta_titular.configure(text="Suma por metodo de Open CV add")
        image=cv2.add(img1,img2)
        image = imutils.resize(image,height=350)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #print(image)
        im=PIL.Image.fromarray(image,'RGB')
        img3r=ImageTk.PhotoImage(image=im)
        resultadoImagen.config(image=img3r)
        resultadoImagen.image = img3r
    if opc == 2:
        etiqueta_titular.configure(text="Suma por metodo de Open CV addWeighted")
        image=cv2.addWeighted(img1,0.7,img2,0.3,0)
        image = imutils.resize(image,height=350)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #print(image)
        im=PIL.Image.fromarray(image,'RGB')
        img3r=ImageTk.PhotoImage(image=im)
        resultadoImagen.config(image=img3r)
        resultadoImagen.image = img3r

    
raiz = Tk()
raiz.title("Operaciones de imagenes") #Cambiar el nombre de la ventana 
raiz.geometry("1200x480") #Configurar tamaño
raiz.resizable(0,0)
etiqueta_titular = ttk.Label(text="Operaciones de imagenes")
img1vi=PhotoImage(file="badbunny.jpg")
widget=Label(raiz,text="Imagen 1",image=img1vi).place(x=50,y=50)
img2vi=PhotoImage(file="danielricciardo.jpg")
widget2=Label(raiz,text="imagen 2",image=img2vi).place(x=850,y=50)
etiqueta_titular.place(x=600, y=20)
resultadoImagen = Label(raiz,text="Resultado")
resultadoImagen.place(x=400,y=50)
keyboard.on_press_key("d", lambda _:operaciones())

raiz.mainloop() 