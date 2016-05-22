# -*- coding: utf-8 -*-
# Auteur : Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("Projet calcul v0.4")
print("----------------------------------------------------------------------")
print("")

from tkinter import *
import math

calcul = 0
touche_1 = 0
touche_2 = 0

def touche_1():
	global calcul
	a = calcul.get()
	a += "1"
	calcul.set(a)
	
def touche_2():
	global calcul
	a = calcul.get()
	a += "2"
	calcul.set(a)
	
def touche_3():
	global calcul
	a = calcul.get()
	a += "3"
	calcul.set(a)
	
def touche_4():
	global calcul
	a = calcul.get()
	a += "4"
	calcul.set(a)
	
def touche_5():
	global calcul
	a = calcul.get()
	a += "5"
	calcul.set(a)
	
def touche_6():
	global calcul
	a = calcul.get()
	a += "6"
	calcul.set(a)
	
def touche_7():
	global calcul
	a = calcul.get()
	a += "7"
	calcul.set(a)
	
def touche_8():
	global calcul
	a = calcul.get()
	a += "8"
	calcul.set(a)
	
def touche_9():
	global calcul
	a = calcul.get()
	a += "9"
	calcul.set(a)
	
def touche_0():
	global calcul
	a = calcul.get()
	a += "0"
	calcul.set(a)
	
def touche_c():
	global calcul
	calcul.set("")
	
def touche_div():
	global calcul
	a = calcul.get()
	a += "/"
	calcul.set(a)
	
def touche_mul():
	global calcul
	a = calcul.get()
	a += "*"
	calcul.set(a)
	
def touche_sou():
	global calcul
	a = calcul.get()
	a += "-"
	calcul.set(a)
	
def touche_plu():
	global calcul
	a = calcul.get()
	a += "+"
	calcul.set(a)
	
def touche_res():
	global calcul
	a = str(calcul.get())
	a = eval(a)
	calcul.set(a)
	
def touche_res1(Return):
	global calcul
	a = str(calcul.get())
	a = eval(a)
	calcul.set(a)
	
def touche_vir():
	global calcul
	a = calcul.get()
	a += "."
	calcul.set(a)
	
def touche_pa1():
	global calcul
	a = calcul.get()
	a += "("
	calcul.set(a)
	
def touche_pa2():
	global calcul
	a = calcul.get()
	a += ")"
	calcul.set(a)
	
def touche_eff():
	global calcul
	a = calcul.get()
	a = a[:-1]
	calcul.set(a)
	
def touche_x():
	global calcul
	a = calcul.get()
	a += "x"
	calcul.set(a)
	
def touche_pi():
	global calcul
	a = calcul.get()
	a += "math.pi"
	calcul.set(a)
	
def touche_sin():
	global calcul
	a = calcul.get()
	a += "math.sin("
	calcul.set(a)
	
def touche_cos():
	global calcul
	a = calcul.get()
	a += "math.cos("
	calcul.set(a)
	
def touche_tan():
	global calcul
	a = calcul.get()
	a += "math.tan("
	calcul.set(a)
	
fenetre1 = Tk()
fenetre1.title("Calculatrice v0.4")

calcul = StringVar()
v = IntVar()

entree = Entry(fenetre1, textvariable=calcul, width=16, borderwidth=10)
touche_1 = Button(fenetre1, text = "1", width=3, relief=FLAT, command = touche_1)
touche_2 = Button(fenetre1, text = "2", width=3, relief=FLAT, command = touche_2)
touche_3 = Button(fenetre1, text = "3", width=3, relief=FLAT, command = touche_3)
touche_4 = Button(fenetre1, text = "4", width=3, relief=FLAT, command = touche_4)
touche_5 = Button(fenetre1, text = "5", width=3, command = touche_5)
touche_6 = Button(fenetre1, text = "6", width=3, relief=FLAT, command = touche_6)
touche_7 = Button(fenetre1, text = "7", width=3, relief=FLAT, command = touche_7)
touche_8 = Button(fenetre1, text = "8", width=3, relief=FLAT, command = touche_8)
touche_9 = Button(fenetre1, text = "9", width=3, relief=FLAT, command = touche_9)
touche_0 = Button(fenetre1, text = "0", width=3, relief=FLAT, command = touche_0)
touche_c = Button(fenetre1, text = "C", width=3, command = touche_c)
touche_div = Button(fenetre1, text = "/", width=3, command = touche_div)
touche_mul = Button(fenetre1, text = "*", width=3, command = touche_mul)
touche_sou = Button(fenetre1, text = "-", width=3, command = touche_sou)
touche_plu = Button(fenetre1, text = "+", width=3, command = touche_plu)
touche_res = Button(fenetre1, text = "=", width=3, relief=SUNKEN, command = touche_res)
touche_vir = Button(fenetre1, text = ",", width=3, command = touche_vir)
touche_pa1 = Button(fenetre1, text = "(", width=3, command = touche_pa1)
touche_pa2 = Button(fenetre1, text = ")", width=3, command = touche_pa2)
touche_graph = Button(fenetre1, text = "f(x)", width=3, command = touche_pa2)
touche_eff = Button(fenetre1, text = "←", width=3, command = touche_eff)
touche_x = Button(fenetre1, text = "X", width=3, command = touche_x)
touche_pi = Button(fenetre1, text = "π", width=3, command = touche_pi)
touche_sin = Button(fenetre1, text = "sin", width=3, command = touche_sin)
touche_cos = Button(fenetre1, text = "cos", width=3, command = touche_cos)
touche_tan = Button(fenetre1, text = "tan", width=3, command = touche_tan)

entree.config(font=('Arial', 20, 'bold'))
touche_1.config(font=('Arial', 16, 'bold'))
touche_2.config(font=('Arial', 16, 'bold'))
touche_3.config(font=('Arial', 16, 'bold'))
touche_4.config(font=('Arial', 16, 'bold'))
touche_5.config(font=('Arial', 16, 'bold'))
touche_6.config(font=('Arial', 16, 'bold'))
touche_7.config(font=('Arial', 16, 'bold'))
touche_8.config(font=('Arial', 16, 'bold'))
touche_9.config(font=('Arial', 16, 'bold'))
touche_0.config(font=('Arial', 16, 'bold'))
touche_c.config(font=('Arial', 16, 'bold'))
touche_div.config(font=('Arial', 16, 'bold'))
touche_mul.config(font=('Arial', 16, 'bold'))
touche_sou.config(font=('Arial', 16, 'bold'))
touche_plu.config(font=('Arial', 16, 'bold'))
touche_res.config(font=('Arial', 16, 'bold'))
touche_vir.config(font=('Arial', 16, 'bold'))
touche_pa1.config(font=('Arial', 16, 'bold'))
touche_pa2.config(font=('Arial', 16, 'bold'))
touche_graph.config(font=('Arial', 16, 'bold'))
touche_eff.config(font=('Arial', 16, 'bold'))
touche_x.config(font=('Arial', 16, 'bold'))
touche_pi.config(font=('Arial', 16, 'bold'))
touche_sin.config(font=('Arial', 16, 'bold'))
touche_cos.config(font=('Arial', 16, 'bold'))
touche_tan.config(font=('Arial', 16, 'bold'))

entree.grid(row=1, column=2, columnspan=5)
touche_1.grid(row=4, column=3)
touche_1.grid(row=4, column=3)
touche_2.grid(row=4, column=4)
touche_3.grid(row=4, column=5)
touche_4.grid(row=3, column=3)
touche_5.grid(row=3, column=4)
touche_6.grid(row=3, column=5)
touche_7.grid(row=2, column=3)
touche_8.grid(row=2, column=4)
touche_9.grid(row=2, column=5)
touche_0.grid(row=5, column=4)
touche_c.grid(row=5, column=2)
touche_div.grid(row=3, column=6)
touche_mul.grid(row=2, column=6)
touche_sou.grid(row=3, column=2)
touche_plu.grid(row=2, column=2)
touche_res.grid(row=4, column=6, rowspan=2)
touche_vir.grid(row=4, column=2)
touche_pa1.grid(row=5, column=3)
touche_pa2.grid(row=5, column=5)
touche_graph.grid(row=1, column=1)
touche_eff.grid(row=1, column=7)
touche_x.grid(row=2, column=1)
touche_pi.grid(row=2, column=7)
touche_sin.grid(row=3, column=7)
touche_cos.grid(row=4, column=7)
touche_tan.grid(row=5, column=7)

fenetre1.bind("<Return>", touche_res1)

fenetre1.mainloop()

"""
Changelog :
v0.4 :
Ajout de fonctions "scientifique".
Ajout d'un deuxième fichier contenant les fonctions nécessaire.
v0.3 :
Interface rendu plus lisible.
v0.2 :
Fonction de base assurées.
v0.1 :
Création de l'interface.
"""
