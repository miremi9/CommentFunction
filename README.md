Ce code permet de generer des blocs commentaires pour les fonctions C++
utilisation : 
python main -re 
```
void GRAremoveSommet(unsigned int uiIdSommet);
    definition  : [la definition de la fonction]
    <Paramtre demandé> = [votre texte]
```
exemple d'utilisation : 
  
>python main.py
```
definition : void GRAremoveSommet(unsigned int uiIdSommet)
precondition : uiIdSommet is an existing Sommet in graph
Postcon : the Sommet is removed


/************************************************************************
 **** GRAremoveSommet                                                ****
 ************************************************************************
 **** Input : unsigned int uiIdSommet                                ****
 **** precondtion : uiIdSommet is an existing Sommet in graph        ****
 **** Output : None                                                  ****
 **** Postcondition : the Sommet is removed                          ****
 ************************************************************************/
 
 definition : 
 ```
 le programme se stop quand definition est vide / ne recoit pas une fonction
 
 option d'appel : 
 `main.py -re` pour l'exemple precedant et par defaut
 `main.py -start` pour une definition manuel de chaque partie
 
 Automatisation :
 le programme deconnait les constructeurs par default, de confort, et recopie ainsi que les destructeur, limitant les elements a saisir
 
 
 
