# -*- coding: utf-8 -*-
# Auteurs : Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("PyCalc v5.0")
print("----------------------------------------------------------------------")
print("")

# Importation des modules nécessaires.
from tkinter import *
from Add_PyCalc_32_fx import *
from Add_PyCalc_11_suite import *
import math

def erreur(a):
	"""
	Fonction qui permet d'afficher une fenètre d'erreur avec un texte
	explicatif.
	"""
	# Début : fenetreer.
	# On crée la fenetre.
	fenetreer = Tk()

	# On lui donne un titre.
	fenetreer.title("Erreur")

	# On crée les éléments...
	titre = Label(fenetreer, text="Erreur", height=1)
	erreur = Label(fenetreer, text=a, height=1)

	# ...on leurs donnent les caractèristiques sur leurs polices...
	titre.config(font=('Arial', 16, 'bold'))
	erreur.config(font=('Arial', 13))

	# ...et on les placent dans la fenètre.
	titre.pack()
	erreur.pack()

	# Fin : fenetreer.

def touche_1():
	"""
	Fonction qui permet d'ajouter un 1 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 1.
	a += "1"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_2():
	"""
	Fonction qui permet d'ajouter un 2 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 2.
	a += "2"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_3():
	"""
	Fonction qui permet d'ajouter un 3 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 3.
	a += "3"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_4():
	"""
	Fonction qui permet d'ajouter un 4 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 4.
	a += "4"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_5():
	"""
	Fonction qui permet d'ajouter un 5 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 5.
	a += "5"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_6():
	"""
	Fonction qui permet d'ajouter un 6 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 6.
	a += "6"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_7():
	"""
	Fonction qui permet d'ajouter un 7 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 7.
	a += "7"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_8():
	"""
	Fonction qui permet d'ajouter un 8 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 8.
	a += "8"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_9():
	"""
	Fonction qui permet d'ajouter un 9 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 9.
	a += "9"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_0():
	"""
	Fonction qui permet d'ajouter un 0 à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un 0.
	a += "0"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_c():
	"""
	Fonction qui permet d'effacer le contenu de calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# On enleve ce qu'il y a dans calcul.
	calcul.set("")

def touche_div():
	"""
	Fonction qui permet d'ajouter un / à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un /.
	a += "/"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_mul():
	"""
	Fonction qui permet d'ajouter un * à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un *.
	a += "*"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_sou():
	"""
	Fonction qui permet d'ajouter un - à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un -.
	a += "-"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_plu():
	"""
	Fonction qui permet d'ajouter un + à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un +.
	a += "+"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_res():
	"""
	Fonction qui permet d'afficher le résultat du calcul avec la fonction
	eval.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	try:
		a = str(calcul.get())
		a = eval(a)
		calcul.set(a)
	except SyntaxError:
		e = "Calcul impossible à effectuer !"
		erreur(e)

def touche_res1(Return):
	"""
	Fonction qui permet d'afficher le résultat du calcul avec la fonction
	eval lors de l'appui sur la touche entrer.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	a = str(calcul.get())
	a = eval(a)
	calcul.set(a)

def touche_vir():
	"""
	Fonction qui permet d'ajouter un . à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un ..
	a += "."

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_pa1():
	"""
	Fonction qui permet d'ajouter un ( à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un (.
	a += "("

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_pa2():
	"""
	Fonction qui permet d'ajouter un ) à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un ).
	a += ")"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_eff():
	"""
	Fonction qui permet d'effacer le dernier caractère à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On enleve le dernier caractère de a.
	a = a[:-1]

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_x():
	"""
	Fonction qui permet d'ajouter un x à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un x.
	a += "x"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_pi():
	"""
	Fonction qui permet d'ajouter math.pi à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute math.pi.
	a += "math.pi"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_sin():
	"""
	Fonction qui permet d'ajouter math.sin( à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute math.sin(.
	a += "math.sin("

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_cos():
	"""
	Fonction qui permet d'ajouter math.cos( à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute math.cos(.
	a += "math.cos("

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_tan():
	"""
	Fonction qui permet d'ajouter math.tan( à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute math.tan(.
	a += "math.tan("

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_pui():
	"""
	Fonction qui permet d'ajouter un ** à calcul.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On ajoute un **.
	a += "**"

	# On remet le contenu de a dans calcul.
	calcul.set(a)

def touche_graph():
	"""
	Fonction qui permet d'executer la fonction mainfx après avoir fermer
	la fenetre1.
	"""
	# Import de fenetre1 pour pouvoir la fermer.
	global fenetre1

	# Import de la variable calcul créée par main().
	global calcul

	# La variable a prend la valeur de calcul.
	a = calcul.get()

	# On détruit la fenetre1 (sinon bug).
	fenetre1.destroy()

	# Exécution du module f(x).
	mainfx(a)

def suite():
	"""
	Fonction qui permet d'executer la fonction mainsuite après avoir fermer
	la fenetre1.
	"""
	# Import de fenetre1 pour pouvoir la fermer.
	global fenetre1

	# Import de fenetre2 pour pouvoir la fermer.
	global fenetre2

	# On détruit la fenetre2 (sinon bug).
	fenetre2.destroy()

	# On détruit la fenetre1 (sinon bug).
	fenetre1.destroy()

	# Exécution du module suite.
	mainsuite()

def secdeg():
	"""
	Fonction qui permet de calculer les solutions de l'équation du 2nd degré.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# En cas d'erreur...
	try:
		# f prend la chaine de caractère de calcul.
		f = calcul.get()

		# On remplace le **2 contenu dans f par vide et on met le résultat
		# dans fm.
		fm = f.replace('**2', "")

		# On crée une liste avec les éléments entre les x.
		fm = fm.split("x")

		# On met chaque éléments de la liste dans les variables a b c.
		a = int(fm[0])
		b = int(fm[1])
		c = int(fm[2])

		# On calcul le delta.
		delta = (b*b) - (4*a*c)

		# Tests pour sortir, si il y en a, le(s) solution(s).
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

		# Dans les variables a b c delta, on met les "phrases de réponses"
		# à afficher.
		a = "a = {}".format(a)
		b = "b = {}".format(b)
		c = "c = {}".format(c)
		delta = "Δ = {}".format(delta)

		# Début : fenetre3.
		# On crée la fenetre.
		fenetre3 = Tk()

		# On lui donne un titre.
		fenetre3.title("Second degré")

		# On crée les éléments...
		titre = Label(fenetre3, text=f, height=1, relief=SUNKEN)
		scd_1 = Label(fenetre3, text=a, height=1)
		scd_2 = Label(fenetre3, text=b, height=1)
		scd_3 = Label(fenetre3, text=c, height=1)
		scd_4 = Label(fenetre3, text=delta, height=1)
		scd_5 = Label(fenetre3, text="Solution(s)", height=1)
		scd_6 = Label(fenetre3, text=p, height=1, relief=SUNKEN)

		# ...on leurs donnent les caractèristiques sur leurs polices...
		titre.config(font=('Arial', 16, 'bold'))
		scd_1.config(font=('Arial', 14, 'bold'))
		scd_2.config(font=('Arial', 14, 'bold'))
		scd_3.config(font=('Arial', 14, 'bold'))
		scd_4.config(font=('Arial', 14, 'bold'))
		scd_5.config(font=('Arial', 14))
		scd_6.config(font=('Arial', 16, 'bold'))

		# ...et on les placent dans la fenètre.
		titre.pack()
		scd_1.pack()
		scd_2.pack()
		scd_3.pack()
		scd_4.pack()
		scd_5.pack()
		scd_6.pack()

		# Fin : fenetre3.
	# ... , afficher une fenètre d'erreur.
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
	"""
	Fonction qui permet de calculer la forme canonique.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# En cas d'erreur...
	try:
		# f prend la chaine de caractère de calcul.
		f = calcul.get()

		# On remplace le **2 contenu dans f par vide et on met le résultat
		# dans fm.
		fm = f.replace('**2', "")

		# On crée une liste avec les éléments entre les x.
		fm = fm.split("x")

		# On met chaque éléments de la liste dans les variables a b c.
		a = int(fm[0])
		b = int(fm[1])
		c = int(fm[2])

		# On calcul l'alpha et le beta
		alpha = (-b)/(2*a)
		beta = a*alpha*alpha+b*alpha+c

		# "Phrases de réponses" pour la fin.
		alpha1 = "α = {}".format(alpha)
		beta1 = "β = {}".format(beta)

		# Tests pour déterminer la "phrase de réponse" dans le calcul
		# de alpha et de beta.
		if alpha < 0:
			alpha = "+{}".format(-alpha)
		elif alpha >= 0:
			alpha = "-{}".format(alpha)
		if beta >= 0:
			beta = "+{}".format(beta)

		# "Phrases réponse" pour le calcul, a, b et c.
		p = "{}*(x{})²{}".format(a, alpha, beta)
		a = "a = {}".format(a)
		b = "b = {}".format(b)
		c = "c = {}".format(c)

		# Début : fenetre4.
		# On crée la fenetre.
		fenetre4 = Tk()

		# On lui donne un titre.
		fenetre4.title("Forme canonique")

		# On crée les éléments...
		titre = Label(fenetre4, text="Forme normale", height=1)
		titre_1 = Label(fenetre4, text=f, height=1, relief=SUNKEN)
		scd_1 = Label(fenetre4, text=a, height=1)
		scd_2 = Label(fenetre4, text=b, height=1)
		scd_3 = Label(fenetre4, text=c, height=1)
		scd_4 = Label(fenetre4, text=alpha1, height=1)
		scd_5 = Label(fenetre4, text=beta1, height=1)
		scd_6 = Label(fenetre4, text="Forme canonique", height=1)
		scd_7 = Label(fenetre4, text=p, height=1, relief=SUNKEN)

		# ...on leurs donnent les caractèristiques sur leurs polices...
		titre.config(font=('Arial', 14))
		titre_1.config(font=('Arial', 16, 'bold'))
		scd_1.config(font=('Arial', 14, 'bold'))
		scd_2.config(font=('Arial', 14, 'bold'))
		scd_3.config(font=('Arial', 14, 'bold'))
		scd_4.config(font=('Arial', 14, 'bold'))
		scd_5.config(font=('Arial', 14, 'bold'))
		scd_6.config(font=('Arial', 14))
		scd_7.config(font=('Arial', 16, 'bold'))

		# ...et on les placent dans la fenètre.
		titre.pack()
		titre_1.pack()
		scd_1.pack()
		scd_2.pack()
		scd_3.pack()
		scd_4.pack()
		scd_5.pack()
		scd_6.pack()
		scd_7.pack()

		# Fin : fenetre4.

	# ... , afficher une fenètre d'erreur.
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
	"""
	Fonction qui permet d'afficher une fenètre avec plusieurs fonctions.
	"""
	# Import de la variable calcul créée par main().
	global calcul

	# Import de fenetre2 (pour la fermer plus tard si nécessaire).
	global fenetre2

	# a prend la chaine de caractère de calcul.
	a = calcul.get()

	# Début : fenetre3.
	# On crée la fenetre.
	fenetre2 = Tk()

	# On lui donne un titre.
	fenetre2.title("Autres options")

	# On crée les éléments...
	titre = Label(fenetre2, text="A résoudre", height=1)
	titre1 = Label(fenetre2, text=a, height=1, relief=SUNKEN)
	other_1 = Button(fenetre2, text = "Calcul de l'équation du second degré (ax**2+bx+c)", command = secdeg)
	other_2 = Button(fenetre2, text = "Calcul de la forme canonique (ax**2+bx+c)", command = canonic)
	other_3 = Button(fenetre2, text = "Suite", command = suite)

	# ...on leurs donnent les caractèristiques sur leurs polices...
	titre.config(font=('Arial', 14))
	titre1.config(font=('Arial', 16, 'bold'))
	other_1.config(font=('Arial', 12, 'bold'))
	other_2.config(font=('Arial', 12, 'bold'))
	other_3.config(font=('Arial', 12, 'bold'))

	# ...et on les placent dans la fenètre.
	titre.pack()
	titre1.pack()
	other_1.pack()
	other_2.pack()
	other_3.pack()

	# Fin : fenetre3.

def main():
	"""
	Fonction principal
	"""
	# calcul devient une variable global.
	global calcul

	# Pour pouvoir fermer la fenetre1.
	global fenetre1

	# Début : fenetre1.
	# On crée la fenetre.
	fenetre1 = Tk()

	# On lui donne un titre.
	fenetre1.title("PyCalc v5.0")

	# Calcul prend StringVar().
	calcul = StringVar()

	# On crée les éléments...
	entree = Entry(fenetre1, textvariable=calcul, width=17, borderwidth=10)
	ttouche_1 = Button(fenetre1, text = "1", width=3, relief=FLAT, command = touche_1)
	ttouche_2 = Button(fenetre1, text = "2", width=3, relief=FLAT, command = touche_2)
	ttouche_3 = Button(fenetre1, text = "3", width=3, relief=FLAT, command = touche_3)
	ttouche_4 = Button(fenetre1, text = "4", width=3, relief=FLAT, command = touche_4)
	ttouche_5 = Button(fenetre1, text = "5", width=3, command = touche_5)
	ttouche_6 = Button(fenetre1, text = "6", width=3, relief=FLAT, command = touche_6)
	ttouche_7 = Button(fenetre1, text = "7", width=3, relief=FLAT, command = touche_7)
	ttouche_8 = Button(fenetre1, text = "8", width=3, relief=FLAT, command = touche_8)
	ttouche_9 = Button(fenetre1, text = "9", width=3, relief=FLAT, command = touche_9)
	ttouche_0 = Button(fenetre1, text = "0", width=3, relief=FLAT, command = touche_0)
	ttouche_c = Button(fenetre1, text = "C", width=3, command = touche_c)
	ttouche_div = Button(fenetre1, text = "/", width=3, command = touche_div)
	ttouche_mul = Button(fenetre1, text = "*", width=3, command = touche_mul)
	ttouche_sou = Button(fenetre1, text = "-", width=3, command = touche_sou)
	ttouche_plu = Button(fenetre1, text = "+", width=3, command = touche_plu)
	ttouche_res = Button(fenetre1, text = "=", width=3, relief=SUNKEN, command = touche_res)
	ttouche_vir = Button(fenetre1, text = ",", width=3, command = touche_vir)
	ttouche_pa1 = Button(fenetre1, text = "(", width=3, command = touche_pa1)
	ttouche_pa2 = Button(fenetre1, text = ")", width=3, command = touche_pa2)
	ttouche_graph = Button(fenetre1, text = "f(x)", width=3, command = touche_graph)
	ttouche_eff = Button(fenetre1, text = "←", width=3, command = touche_eff)
	ttouche_x = Button(fenetre1, text = "x", width=3, command = touche_x)
	ttouche_pi = Button(fenetre1, text = "π", width=3, command = touche_pi)
	ttouche_sin = Button(fenetre1, text = "sin", width=3, command = touche_sin)
	ttouche_cos = Button(fenetre1, text = "cos", width=3, command = touche_cos)
	ttouche_tan = Button(fenetre1, text = "tan", width=3, command = touche_tan)
	ttouche_pui = Button(fenetre1, text = "^", width=3, command = touche_pui)
	ttouche_oth = Button(fenetre1, text = "Plus", width=3, command = touche_oth)

	# ...on leurs donnent les caractèristiques sur leurs polices...
	entree.config(font=('Arial', 20, 'bold'))
	ttouche_1.config(font=('Arial', 16, 'bold'))
	ttouche_2.config(font=('Arial', 16, 'bold'))
	ttouche_3.config(font=('Arial', 16, 'bold'))
	ttouche_4.config(font=('Arial', 16, 'bold'))
	ttouche_5.config(font=('Arial', 16, 'bold'))
	ttouche_6.config(font=('Arial', 16, 'bold'))
	ttouche_7.config(font=('Arial', 16, 'bold'))
	ttouche_8.config(font=('Arial', 16, 'bold'))
	ttouche_9.config(font=('Arial', 16, 'bold'))
	ttouche_0.config(font=('Arial', 16, 'bold'))
	ttouche_c.config(font=('Arial', 16, 'bold'))
	ttouche_div.config(font=('Arial', 16, 'bold'))
	ttouche_mul.config(font=('Arial', 16, 'bold'))
	ttouche_sou.config(font=('Arial', 16, 'bold'))
	ttouche_plu.config(font=('Arial', 16, 'bold'))
	ttouche_res.config(font=('Arial', 16, 'bold'))
	ttouche_vir.config(font=('Arial', 16, 'bold'))
	ttouche_pa1.config(font=('Arial', 16, 'bold'))
	ttouche_pa2.config(font=('Arial', 16, 'bold'))
	ttouche_graph.config(font=('Arial', 16, 'bold'))
	ttouche_eff.config(font=('Arial', 16, 'bold'))
	ttouche_x.config(font=('Arial', 16, 'bold'))
	ttouche_pi.config(font=('Arial', 16, 'bold'))
	ttouche_sin.config(font=('Arial', 16, 'bold'))
	ttouche_cos.config(font=('Arial', 16, 'bold'))
	ttouche_tan.config(font=('Arial', 16, 'bold'))
	ttouche_pui.config(font=('Arial', 16, 'bold'))
	ttouche_oth.config(font=('Arial', 16, 'bold'))

	# ...et on les placent dans la fenètre.
	entree.grid(row=1, column=2, columnspan=5)
	ttouche_1.grid(row=4, column=3)
	ttouche_1.grid(row=4, column=3)
	ttouche_2.grid(row=4, column=4)
	ttouche_3.grid(row=4, column=5)
	ttouche_4.grid(row=3, column=3)
	ttouche_5.grid(row=3, column=4)
	ttouche_6.grid(row=3, column=5)
	ttouche_7.grid(row=2, column=3)
	ttouche_8.grid(row=2, column=4)
	ttouche_9.grid(row=2, column=5)
	ttouche_0.grid(row=5, column=4)
	ttouche_c.grid(row=5, column=2)
	ttouche_div.grid(row=3, column=6)
	ttouche_mul.grid(row=2, column=6)
	ttouche_sou.grid(row=3, column=2)
	ttouche_plu.grid(row=2, column=2)
	ttouche_res.grid(row=5, column=6)
	ttouche_vir.grid(row=4, column=2)
	ttouche_pa1.grid(row=5, column=3)
	ttouche_pa2.grid(row=5, column=5)
	ttouche_graph.grid(row=1, column=1)
	ttouche_eff.grid(row=1, column=7)
	ttouche_x.grid(row=2, column=1)
	ttouche_pi.grid(row=2, column=7)
	ttouche_sin.grid(row=3, column=7)
	ttouche_cos.grid(row=4, column=7)
	ttouche_tan.grid(row=5, column=7)
	ttouche_pui.grid(row=4, column=6)
	ttouche_oth.grid(row=5, column=1)

	# Pour que la touche Entrer donne le résultat.
	fenetre1.bind("<Return>", touche_res1)

	# Mainloop pour que la fenètre reste ouverte.
	fenetre1.mainloop()

	# Fin : fenetre1.

# Exécution de la fonction principal.
main()

"""
Changelog :
v5.0 :
Ajout de tous les commentaires pour une meilleure compréhension du programme.
Ajout de la fonction main() avec, en contre-partie, ajout de variables global.
(Module f(x) v3.2) et (Module suite v1.1) :
Ajout de commentaires pour la partie fenètre.

v4.0 :
(Module f(x) v3.1) :
Plusieurs améliorations du module f(x) comme la possibilité de mettre une
formule directement depuis l'écran de la calculette.
(Module suite v1.0) :
Ajout du module suite (par Ricardo)

v3.2 :
(Module f(x) v3.0) :
Mise à jour module f(x).

v3.1 :
(Module f(x) v2.0) :
Mise à jour module f(x).

v3.0 :
(Module f(x) v1.0) :
Integration des courbes de fonctions (par Ricardo).

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

v0.3 :
Interface rendu plus lisible.

v0.2 :
Fonction de base assurées.

v0.1 :
Version beta de PyCalc.
Création de l'interface.
"""
