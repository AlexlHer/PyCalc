# -*- coding: utf-8 -*-
# Auteur : Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("PyCalc v2.0")
print("----------------------------------------------------------------------")
print("")

from tkinter import *
import math

calcul = 0
touche_1 = 0
touche_2 = 0

def erreur(a):
	fenetreer = Tk()
	fenetreer.title("Erreur")
	titre = Label(fenetreer, text="Erreur", height=1)
	erreur = Label(fenetreer, text=a, height=1)
	titre.config(font=('Arial', 16, 'bold'))
	erreur.config(font=('Arial', 13))
	titre.pack()
	erreur.pack()

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
	try:
		a = str(calcul.get())
		a = eval(a)
		calcul.set(a)
	except SyntaxError:
		e = "Calcul impossible à effectuer !"
		erreur(e)
	
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
	
def touche_pui():
	global calcul
	a = calcul.get()
	a += "**"
	calcul.set(a)
	
def touche_graph():
	global calcul
	a = calcul.get()
	e = "Option pas encore disponible !"
	erreur(e)
	
def secdeg():
	try:
		f = calcul.get()
		fm = f.replace('**2', "")
		fm = fm.split("x")
		a = int(fm[0])
		b = int(fm[1])
		c = int(fm[2])
		delta = (b*b) - (4*a*c)
		if delta < 0:
			p = "Pas de solutions"
		elif delta == 0:
			resu = (-b)/(2*a)
			p = "x = {}/2{} = {}".format(-b, a, resu)
		else:
			resu1 = (-b-math.sqrt(delta))/(2*a)
			resu2 = (-b+math.sqrt(delta))/(2*a)
			resu1 = float("{0:2.2f}".format(resu1))
			resu2 = float("{0:2.2f}".format(resu2))
			p = "x1 = ({}-√{})/2{} = {} et x2 = ({}+√{})/2{} = {}".format(-b, delta, a, resu1, -b, delta, a, resu2)
	
		a = "a = {}".format(a)
		b = "b = {}".format(b)
		c = "c = {}".format(c)
		delta = "Δ = {}".format(delta)
		fenetre3 = Tk()
		fenetre3.title("Second degré")
		
		titre = Label(fenetre3, text=f, height=1, relief=SUNKEN)
		scd_1 = Label(fenetre3, text=a, height=1)
		scd_2 = Label(fenetre3, text=b, height=1)
		scd_3 = Label(fenetre3, text=c, height=1)
		scd_4 = Label(fenetre3, text=delta, height=1)
		scd_5 = Label(fenetre3, text="Solution(s)", height=1)
		scd_6 = Label(fenetre3, text=p, height=1, relief=SUNKEN)
		
		titre.config(font=('Arial', 16, 'bold'))
		scd_1.config(font=('Arial', 14, 'bold'))
		scd_2.config(font=('Arial', 14, 'bold'))
		scd_3.config(font=('Arial', 14, 'bold'))
		scd_4.config(font=('Arial', 14, 'bold'))
		scd_5.config(font=('Arial', 14))
		scd_6.config(font=('Arial', 16, 'bold'))
		
		titre.pack()
		scd_1.pack()
		scd_2.pack()
		scd_3.pack()
		scd_4.pack()
		scd_5.pack()
		scd_6.pack()
	except IndexError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
	except ValueError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
	except ZeroDivisionError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
		
def canonic():
	try:
		f = calcul.get()
		fm = f.replace('**2', "")
		fm = fm.split("x")
		a = int(fm[0])
		b = int(fm[1])
		c = int(fm[2])
		alpha = (-b)/(2*a)
		beta = a*alpha*alpha+b*alpha+c
		alpha1 = "α = {}".format(alpha)
		beta1 = "β = {}".format(beta)
		if alpha < 0:
			alpha = "+{}".format(-alpha)
		elif alpha >= 0:
			alpha = "-{}".format(alpha)
		if beta >= 0:
			beta = "+{}".format(beta)
		p = "{}*(x{})²{}".format(a, alpha, beta)
		a = "a = {}".format(a)
		b = "b = {}".format(b)
		c = "c = {}".format(c)
		fenetre4 = Tk()
		fenetre4.title("Forme canonique")
		
		titre = Label(fenetre4, text="Forme normale", height=1)
		titre_1 = Label(fenetre4, text=f, height=1, relief=SUNKEN)
		scd_1 = Label(fenetre4, text=a, height=1)
		scd_2 = Label(fenetre4, text=b, height=1)
		scd_3 = Label(fenetre4, text=c, height=1)
		scd_4 = Label(fenetre4, text=alpha1, height=1)
		scd_5 = Label(fenetre4, text=beta1, height=1)
		scd_6 = Label(fenetre4, text="Forme canonique", height=1)
		scd_7 = Label(fenetre4, text=p, height=1, relief=SUNKEN)
		
		titre.config(font=('Arial', 14))
		titre_1.config(font=('Arial', 16, 'bold'))
		scd_1.config(font=('Arial', 14, 'bold'))
		scd_2.config(font=('Arial', 14, 'bold'))
		scd_3.config(font=('Arial', 14, 'bold'))
		scd_4.config(font=('Arial', 14, 'bold'))
		scd_5.config(font=('Arial', 14, 'bold'))
		scd_6.config(font=('Arial', 14))
		scd_7.config(font=('Arial', 16, 'bold'))
		
		titre.pack()
		titre_1.pack()
		scd_1.pack()
		scd_2.pack()
		scd_3.pack()
		scd_4.pack()
		scd_5.pack()
		scd_6.pack()
		scd_7.pack()
	except IndexError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
	except ValueError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
	except ZeroDivisionError:
		e = "La formule entrée n'est pas valide !"
		erreur(e)
	
def touche_oth():
	a = calcul.get()		
	fenetre2 = Tk()
	fenetre2.title("Autres options")
	
	titre = Label(fenetre2, text="A résoudre", height=1)
	titre1 = Label(fenetre2, text=a, height=1, relief=SUNKEN)
	other_1 = Button(fenetre2, text = "Calcul de l'équation du second degré (ax**2+bx+c)", command = secdeg)
	other_2 = Button(fenetre2, text = "Calcul de la forme canonique (ax**2+bx+c)", command = canonic)
	
	titre.config(font=('Arial', 14))
	titre1.config(font=('Arial', 16, 'bold'))
	other_1.config(font=('Arial', 12, 'bold'))
	other_2.config(font=('Arial', 12, 'bold'))
	
	titre.pack()
	titre1.pack()
	other_1.pack()
	other_2.pack()
	
fenetre1 = Tk()
fenetre1.title("PyCalc v2.0")

calcul = StringVar()
v = IntVar()

entree = Entry(fenetre1, textvariable=calcul, width=17, borderwidth=10)
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
touche_graph = Button(fenetre1, text = "f(x)", width=3, command = touche_graph)
touche_eff = Button(fenetre1, text = "←", width=3, command = touche_eff)
touche_x = Button(fenetre1, text = "x", width=3, command = touche_x)
touche_pi = Button(fenetre1, text = "π", width=3, command = touche_pi)
touche_sin = Button(fenetre1, text = "sin", width=3, command = touche_sin)
touche_cos = Button(fenetre1, text = "cos", width=3, command = touche_cos)
touche_tan = Button(fenetre1, text = "tan", width=3, command = touche_tan)
touche_pui = Button(fenetre1, text = "^", width=3, command = touche_pui)
touche_oth = Button(fenetre1, text = "Plus", width=3, command = touche_oth)

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
touche_pui.config(font=('Arial', 16, 'bold'))
touche_oth.config(font=('Arial', 16, 'bold'))

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
touche_res.grid(row=5, column=6)
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
touche_pui.grid(row=4, column=6)
touche_oth.grid(row=5, column=1)

fenetre1.bind("<Return>", touche_res1)

fenetre1.mainloop()

"""
Changelog :
v2.0 :
Ajout du calcul de la forme canonique.

v1.2 :
Ajout de messages d'erreurs.

v1.1 :
Mise en place d'une fonction d'erreur.

v1.0 :
Version final de PyCalc.
Ajout d'un calcul auto d'équation du second degré.

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
