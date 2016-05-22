# -*- coding: utf-8 -*-
# Auteurs : Ricardo Ramos et Alexandre l'Heritier
# 2eme fichier pour le fonctionnement de PyCalc.

from tkinter import *
import turtle
import math

def erreur(e, a):
	fenetreer = Tk()
	fenetreer.title(e)
	titre = Label(fenetreer, text=e, height=1)
	erreur = Label(fenetreer, text=a, height=1)
	titre.config(font=('Arial', 16, 'bold'))
	erreur.config(font=('Arial', 13))
	titre.pack()
	erreur.pack()

def repère(t):
	t.width(3)
	t.setposition(-300,0)
	t.fd(600)
	t.right(90)
	t.fd(5)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(5)
	t.penup()
	t.setposition(0, -300)
	t.pendown()
	t.setheading(90)
	t.fd(600)
	t.right(90)
	t.fd(5)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(5)
	t.color('grey')
	t.width(1)
	
	
	for i in range(1, 20):
		if i == 10:
			continue
		t.penup()
		t.setposition(-300, i*30-300)
		t.pendown()
		t.setheading(0)
		t.fd(600)
		
		
	for i in range(1, 20):
		if i ==10:
			continue
		t.penup()
		t.setposition(i*30-300, -300)
		t.pendown()
		t.setheading(90)
		t.fd(600)
		
		
	t.penup()
	t.setposition(0,0)
	t.pendown()
	t.color('black')

def convertion_u(u):
	if 'U(n-1)' in u:
		u = u.replace('U(n-1)','U(u, n-1, U_0, n_0 = 0)')
	return u   
	
	
	
	   
def U(u:str, n:int, U_0:float, n_0 = 0):
	if n == n_0:
		res = U_0
	elif n > n_0:
		res = eval(u)
	else:
		res = "L'indice n'est pas valide."
	return res
	
	
	
		
def repU(t, u, U_0, n_0 = 0, c = 'black'):
	t.color(c)
	for i in range(11):
		x = i*30+n_0*30
		y = U(u, i, U_0)*30
		if x > 300:
			break
		t.penup()
		t.setposition(x, y)
		t.pendown()
		t.width(5)
		t.circle(1)
	t.width(1)
	   
def dessine(liste):
	t = turtle.Turtle()
	t.hideturtle()
	t.speed(0)
	turtle.setup(width=650,height=650)
	repère(t)
	u = liste[0]
	U_0 = liste[2]
	u = convertion_u(u)
	res = U(u, liste[1], U_0, liste[3])
	ti = "Résultat"
	erreur(ti, res)
	repU(t, u, U_0, 3)
	turtle.mainloop()

def fenetre():
	fenetre6 = Tk()
	v_1 = StringVar()
	v_2 = StringVar()
	v_3 = StringVar()
	v_4 = StringVar()
	fenetre6.title("Suite")
	titre = Label(fenetre6, text="Suite")
	y_1_1 = Label(fenetre6, text="Formule :")
	y_1_2 = Entry(fenetre6, textvariable = v_1)
	y_2_1 = Label(fenetre6, text="Indice :")
	y_2_2 = Entry(fenetre6, textvariable = v_2)
	y_3_1 = Label(fenetre6, text="1er terme :")
	y_3_2 = Entry(fenetre6, textvariable = v_3)
	y_4_1 = Label(fenetre6, text="Indice du 1er terme :")
	y_4_2 = Entry(fenetre6, textvariable = v_4)
	bouton = Button(fenetre6, text="Ok", command=fenetre6.destroy)
	
	titre.config(font=('Arial', 14))
	y_1_1.config(font=('Arial', 14, 'bold'))
	y_1_2.config(font=('Arial', 14, 'bold'))
	y_2_1.config(font=('Arial', 14, 'bold'))
	y_2_2.config(font=('Arial', 14, 'bold'))
	y_3_1.config(font=('Arial', 14, 'bold'))
	y_3_2.config(font=('Arial', 14, 'bold'))
	y_4_1.config(font=('Arial', 14, 'bold'))
	y_4_2.config(font=('Arial', 14, 'bold'))
	bouton.config(font=('Arial', 14, 'bold'))
	
	titre.grid(row=1, column=1, columnspan=3)
	y_1_1.grid(row=2, column=1)
	y_1_2.grid(row=2, column=2)
	y_2_1.grid(row=3, column=1)
	y_2_2.grid(row=3, column=2)
	y_3_1.grid(row=4, column=1)
	y_3_2.grid(row=4, column=2)
	y_4_1.grid(row=5, column=1)
	y_4_2.grid(row=5, column=2)
	bouton.grid(row=6, column=1, columnspan=2)
	
	fenetre6.mainloop()
	
	v_1 = v_1.get()
	v_2 = v_2.get()
	v_3 = v_3.get()
	v_4 = v_4.get()
	try:
		liste = [v_1, int(v_2), float(v_3), int(v_4)]
	except ValueError:
		t = "Erreur"
		e = "Impossible de calculer !"
		erreur(t, e)
	return liste
	
def mainsuite():
	a = fenetre()
	#print(a)
	dessine(a)