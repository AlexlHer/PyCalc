# -*- coding: utf-8 -*-

# Auteurs : Ricardo Ramos (traitement et affichage de la courbe) et
#           Alexandre l'Heritier (fenètre de configuration et d'erreur).

# 3eme fichier pour le fonctionnement de PyCalc.

# Importation des modules nécessaires.
from tkinter import *
import turtle
import math

def erreur(e, a):
	"""
	Fonction qui permet d'afficher une erreur et/ou la solution.
	"""
	# Début : fenetreer.
	# On crée la fenetre.
	fenetreer = Tk()

	# On lui donne un titre.
	fenetreer.title(e)

	# On crée les éléments...
	titre = Label(fenetreer, text=e, height=1)
	erreur = Label(fenetreer, text=a, height=1)

	# ...on leurs donnent les caractèristiques sur leurs polices...
	titre.config(font=('Arial', 16, 'bold'))
	erreur.config(font=('Arial', 13))

	# ...et on les placent dans la fenètre.
	titre.pack()
	erreur.pack()

	# Fin : fenetreer.

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
	# Création de la fenètre turtle.
	t = turtle.Turtle()

	# On cache la tortue.
	t.hideturtle()

	# On met la vitesse max.
	t.speed(0)

	# On configure la taille de la fenètre.
	turtle.setup(width=650,height=650)

	# Création du repère.
	repère(t)

	# u prend la chaine de caractère du premier élément de la liste.
	u = liste[0]

	# n prend la chaine de caractère du deuxième élément de la liste.
	n = liste[1]

	# U_0 prend la chaine de caractère du troisième élément de la liste.
	U_0 = liste[2]

	# n_0 prend la chaine de caractère du quatrième élément de la liste.
	n_0 = liste[3]

	# On converti u (si besoin, sinon u sera renvoyer telle qu'elle).
	u = convertion_u(u)

	# On cherche le résultat.
	res = U(u, n, U_0, n_0)

	# On affiche le résultat avec la fonction erreur.
	ti = "Résultat"
	erreur(ti, res)

	# On dessine le résultat.
	repU(t, u, U_0, n_0)

	# Mainloop pour que la fenètre reste.
	turtle.mainloop()

def fenetre():
	# Début : fenetre6.
	# On crée la fenetre.
	fenetre6 = Tk()

	# On lui donne un titre.
	fenetre6.title("Suite")

	# On initialise les variables.
	v_1 = StringVar()
	v_2 = StringVar()
	v_3 = StringVar()
	v_4 = StringVar()

	# On crée les éléments...
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

	# ...on leurs donnent les caractèristiques sur leurs polices...
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

	# ...et on les placent dans la fenètre.
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

	# Mainloop pour que la fenètre reste ouverte.
	fenetre6.mainloop()

	# Récuperation des valeurs pour les remettrent dans leurs variables
	# associées.
	v_1 = v_1.get()
	v_2 = v_2.get()
	v_3 = v_3.get()
	v_4 = v_4.get()

	# En cas d'erreur...
	try:
		liste = [v_1, int(v_2), float(v_3), int(v_4)]

	# ... , afficher une fenètre d'erreur.
	except ValueError:
		t = "Erreur"
		e = "Impossible de calculer !"
		erreur(t, e)

	# On retourne la liste.
	return liste

def mainsuite():
	"""
	Fonction principal.
	"""
	a = fenetre()
	#print(a)
	dessine(a)
