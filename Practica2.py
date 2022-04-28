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