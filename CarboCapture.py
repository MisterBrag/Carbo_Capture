import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser

# Dictionnaire initial des types d'arbres et leur taux d'absorption de CO2 (en kg par an)
ARBRES = {
    'Chêne': 22.0,
    'Érable': 18.0,
    'Pin': 20.0,
    'Saule': 24.0,
    'Hêtre': 22.0,
    'Ficus': 17.0,
    'Palmier': 12.0,
    'Bambou': 15.0,
    'Aloe Vera': 10.0,
    'Plante Araignée': 11.0,
    'Lavande': 9.0,
    'Rosier': 10.0,
    'Hortensia': 8.0,
    'Buis': 9.0
}

class Jardin:
    def __init__(self):
        self.arbres = {}

    def ajouter_arbre(self, type_arbre):
        if type_arbre in self.arbres:
            self.arbres[type_arbre] += 1
        else:
            self.arbres[type_arbre] = 1

    def retirer_arbre(self, type_arbre):
        if type_arbre in self.arbres and self.arbres[type_arbre] > 0:
            self.arbres[type_arbre] -= 1

    def calculer_capture_totale(self):
        total = 0
        for type_arbre, nombre in self.arbres.items():
            total += nombre * ARBRES[type_arbre]
        return total

def ajouter():
    type_arbre = choix_arbre.get()
    jardin.ajouter_arbre(type_arbre)
    mettre_a_jour()

def retirer():
    type_arbre = choix_arbre.get()
    jardin.retirer_arbre(type_arbre)
    mettre_a_jour()

def calculer():
    capture = jardin.calculer_capture_totale()
    messagebox.showinfo("Capture Totale de Carbone", f"La capture totale de carbone par an est de {capture} Kg de CO2.")

def ajouter_nouvel_arbre():
    nouvel_arbre = simpledialog.askstring("Ajouter un nouvel arbre", "Nom de l'arbre:")
    taux_absorption = simpledialog.askfloat("Ajouter un nouvel arbre", "Taux d'absorption de CO2 (kg par an):")
    if nouvel_arbre and taux_absorption:
        ARBRES[nouvel_arbre] = taux_absorption
        menu['menu'].add_command(label=nouvel_arbre, command=tk._setit(choix_arbre, nouvel_arbre))
    mettre_a_jour()

def mettre_a_jour():
    texte_jardin.set(f"Jardin: {jardin.arbres}")

def ouvrir_url(event):
    webbrowser.open('https://www.youtube.com/@adnsauvage')

# Initialisation de l'objet jardin
jardin = Jardin()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculateur de Capture de Carbone")
fenetre.configure(bg='#e0f7fa')

# Liste déroulante pour choisir un type d'arbre
choix_arbre = tk.StringVar()
choix_arbre.set('Chêne')  # valeur par défaut
menu = tk.OptionMenu(fenetre, choix_arbre, *ARBRES.keys())
menu.pack(pady=10, fill='x')

# Boutons pour ajouter ou retirer des arbres
frame_boutons = tk.Frame(fenetre, bg='#e0f7fa')
frame_boutons.pack(pady=5, fill='x')
bouton_ajouter = tk.Button(frame_boutons, text="+", command=ajouter, bg='#00796b', fg='white', font=('Arial', 12))
bouton_ajouter.pack(side='left', padx=5, expand=True, fill='x')
bouton_retirer = tk.Button(frame_boutons, text="-", command=retirer, bg='#00796b', fg='white', font=('Arial', 12))
bouton_retirer.pack(side='right', padx=5, expand=True, fill='x')

# Affichage du jardin
texte_jardin = tk.StringVar()
texte_jardin.set("Jardin: {}")
label_jardin = tk.Label(fenetre, textvariable=texte_jardin, bg='#e0f7fa', font=('Arial', 12))
label_jardin.pack(pady=10, fill='x')

# Bouton pour calculer la capture totale de carbone
bouton_calculer = tk.Button(fenetre, text="Calculer la Capture de Carbone", command=calculer, bg='#00796b', fg='white', font=('Arial', 12))
bouton_calculer.pack(pady=10, fill='x')

# Bouton pour ajouter un nouvel arbre
bouton_nouvel_arbre = tk.Button(fenetre, text="Ajouter un nouvel arbre", command=ajouter_nouvel_arbre, bg='#004d40', fg='white', font=('Arial', 12))
bouton_nouvel_arbre.pack(pady=10, fill='x')

# Pied de page
label_footer = tk.Label(fenetre, text="By ADN Sauvage", font=('Arial', 10, 'italic'), bg='#e0f7fa', fg='#004d40', cursor="hand2")
label_footer.pack(side='bottom', pady=10, fill='x')
label_footer.bind("<Button-1>", ouvrir_url)

# Lancement de la boucle principale
fenetre.mainloop()
