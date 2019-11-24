class Noeud():
    OBJECTIF = 34
    FEUILLES = []
    MAX_COURANT = 0

    def __init__(self, dico_objets_possible, contenu):
        self.possibilite = dico_objets_possible.copy()
        for i, elt in enumerate(self.possibilite):
            if elt[1] > self.OBJECTIF:
                del self.possibilite[i]
        self.contenu = contenu
        self.gauche = None
        self.droite = None
        self.genererer_enfants()

    def genererer_enfants(self):
        if sum([obj[1] for obj in self.contenu]) <= Noeud.OBJECTIF and len(self.possibilite) > 0 and sum([obj[2] for obj in self.contenu])+sum([obj[2] for obj in self.possibilite])>=Noeud.MAX_COURANT:
            if sum([obj[2] for obj in self.contenu]) > Noeud.MAX_COURANT:
                Noeud.MAX_COURANT = sum([obj[2] for obj in self.contenu])

            possibilite_suivante = self.possibilite.copy()
            ajout_droite = possibilite_suivante.pop(0)

            self.gauche = Noeud(possibilite_suivante, self.contenu)

            if sum([obj[1] for obj in self.contenu+[ajout_droite]])<=Noeud.OBJECTIF:
                self.droite = Noeud(possibilite_suivante, self.contenu+[ajout_droite])
            
            if len(self.gauche.possibilite) > 0:
                self.gauche.genererer_enfants()
            if self.droite is not None:
                if len(self.droite.possibilite) > 0:
                    self.droite.genererer_enfants()
    
    def get_feuilles(self):
        if self.gauche != None:
            self.gauche.get_feuilles()
        if self.droite != None:
            self.droite.get_feuilles()
        if self.gauche == None and self.droite == None:
            Noeud.FEUILLES.append(self.contenu)
        return Noeud.FEUILLES

    def get_best_feuilles(self):
        Noeud.FEUILLES.sort(key=lambda tab: sum([obj[2] for obj in tab]), reverse=True)
        return Noeud.FEUILLES[0][1:]


"dico : (nom, contrainte, a_opti)"
dico = [
    ("obj1", 5, 10),
    ("obj2", 4, 40),
    ("obj3", 6, 30),
    ("obj4", 3, 50),
    ("obj5", 2, 2),
    ("obj6", 7, 11),
    ("obj8", 6, 28),
    ("obj9", 13, 50),
    ("obj10", 12, 2),
    ("obj11", 51, 12),
    ("obj20", 41, 42),
    ("obj30", 61, 32),
    ("obj31", 6, 30),
    ("obj41", 3, 50),
    ("obj51", 2, 2),
    ("obj61", 7, 11),
    ("obj81", 6, 28),
    ("obj91", 13, 50),
    
]
racine = Noeud(dico, [("{}", 0, 1)])
#print(racine.droite.droite.contenu)
print("{} feuilles calculé sur {}".format(len(racine.get_feuilles()), 2**len(dico)))
print(racine.get_best_feuilles())
