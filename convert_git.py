import tkinter as tk
from tkinter import ttk, messagebox

def convertir():
    try:
        montant = float(entree_montant.get())
        taux = float(entree_taux.get())
        de_devise = combo_from.get()
        a_devise = combo_to.get()
        
        if de_devise == 'Euro' and a_devise == 'Dollar':
            montant_converti = montant * taux
        elif de_devise == 'Dollar' and a_devise == 'Euro':
            montant_converti = montant / taux
        else:
            montant_converti = montant  #pas de conversion si c'est la même devise selectionnée
        
        montant_converti = round(montant_converti, 2)
        label_resultat.config(text=f"Montant converti: {montant_converti} {a_devise}")
    except ValueError:
        messagebox.showerror("Erreur", " Veuillez saisir un montant ou un taux valide ")
         

# création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur devise")
root.geometry("400x250")   

#   création de cadre(Frame) pour les inputs
frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.pack(fill=tk.BOTH, expand=True)

# Champ d'entrée et label
ttk.Label(frame_inputs, text="Montant:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entree_montant = ttk.Entry(frame_inputs)
entree_montant.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Taux d'échange (Euro à Dollar):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entree_taux = ttk.Entry(frame_inputs)
entree_taux.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="De:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
devise = ['Euro', 'Dollar']
combo_from = ttk.Combobox(frame_inputs, values=devise)
combo_from.set('Euro')
combo_from.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="A:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
combo_to = ttk.Combobox(frame_inputs, values=devise)
combo_to.set('Dollar')
combo_to.grid(row=3, column=1, padx=5, pady=5)

# bouton convertir
convert_button = ttk.Button(frame_inputs, text="Convertir", command=convertir)
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

 
label_resultat = ttk.Label(frame_inputs, text="Montant converti: ")
label_resultat.grid(row=5, column=0, columnspan=2, pady=5)

 
root.mainloop()