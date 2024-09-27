"""Module pour le traitement de listes et la lecture de données à partir d'un fichier CSV."""

import csv

def read_data(filename):
    """Fonction pour lire le contenu du fichier CSV"""
    l = []
    with open(filename, 'r', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=';')
        for element in r:
            c=[]
            for i in element :
                c.append(int(i))
            l.append(c)
    return l

def get_list_k(data, k):
    """Retourne la kième liste de la liste de listes donnée."""
    if k < 0 or k >= len(data):
        return None
    return data[k]


def get_first(l) :
    """Retourne le premier élément de la liste donnée."""
    if l:  # Vérifie si la liste n'est pas vide
        return l[0]  # Retourne le premier élément
    return None  # Retourne None si la liste est vide

def get_last(l) :
    """Retourne le dernier élément de la liste donnée."""
    if l:  # Vérifie si la liste n'est pas vide
        return l[-1]  # Retourne le premier élément
    return None  # Retourne None si la liste est vide

def get_max(l) :
    """Retourne le maximum de la liste donnée."""
    if l:  # Vérifie si la liste n'est pas vide
        return max(l)  # Retourne le maximum de la liste
    return None  # Retourne None si la liste est vide

def get_min(l) :
    """Retourne le minimum de la liste donnée."""
    if l:  # Vérifie si la liste n'est pas vide
        return min(l)  # Retourne le maximum de la liste
    return None  # Retourne None si la liste est vide

def get_sum(l) :
    """Retourne la somme des éléments de la liste donnée."""
    if l:  # Vérifie si la liste n'est pas vide
        return sum(l)  # Retourne le maximum de la liste
    return 0  # Retourne None si la liste est vide

#### Fonction principale
def main() :
    """Lecture des données à partir du fichier"""
    filename = 'listes.cvs'
    data = read_data(filename)
    print("Données lues depuis le fichier :", data)

   # Tests des autres fonctions
    print("Liste à l'indice 0 :", get_list_k(data, 0))
    print("Premier élément de la première liste :", get_first(data[0]))
    print("Dernier élément de la première liste :", get_last(data[0]))
    print("Maximum de la première liste :", get_max(data[0]))
    print("Minimum de la première liste :", get_min(data[0]))
    print("Somme de la première liste :", get_sum(data[0]))

if __name__ == "__main__":
    main()
