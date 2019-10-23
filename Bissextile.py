import os 
# Programme permettant de savoir si une anne saisi par l'utilisateur est oui ou non bissextile
annee = input ("saissisez une annee") #lutilisateur doit saisir une annee
annee = int(annee) #l'annee doit etre un nombre entier
if annee % 400 == 0:
	bissextile = True
elif annee % 100 == 0:
	bissextile = False
elif annee % 4 == 0:
	bissextile = True
else: 
	bissextile = False	
if bissextile: # Si l'annee est bissextile
	print ("Cette annee est bissextile.")
else : # sinon 
	print ("Cette annee n'est pas bissextile.")
os.system ("Pause")
