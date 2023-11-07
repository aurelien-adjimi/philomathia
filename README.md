# Philomathia
 
## *Description du projet*
Ce projet a pour but de nous faire manipuler des concepts mathématiques essentiels dans le monde de l'intelligence artificielle.
Pour ce faire nous devons utiliser les Notebooks Python qui nous permettent d'écrire et exécuter du code Python et même ajouter textes, images, graphiques et équations. 
Avant de commencer les Jobs que vous pouvez voir dans ce Repository, nous avons eu a effectuer une veille sur quelques notions de mathématiques, à savoir: 
- [ ] Les vecteurs
- [ ] Les matrices
- [ ] Les probabilités
- [ ] Les variables indépendantes
- [ ] Les espérances
- [ ] Les variances
- [ ] Les écarts types
- [ ] Les corrélation linéaires
- [ ] Les moyennes
- [ ] Les médianes
- [ ] Les maximum & minimum
- [ ] Les quartiles
- [ ] Boxplot
- [ ] Les histogrammes
- [ ] Le théorème Centrale Limit
- [ ] Les dérivées

Vous retrouverez dans la partie suivante les définitions accompagnées de quelques exemples pour chacune de ces notions mathématiques.

## *Veille sur les notions mathématiques du projet*

### **Les vecteurs**
*Définition:*  
Un vecteur est un objet mathématique représenté graphiquement sous forme d'une flèche. Il est définit par sa longueur, sa direction et son sens. 

*Exemple:*  
Si nous connaissons le point de départ, ici A et le point d'arrivée, ici B, alors on note le vecteur: $\overrightarrow{AB}$

*Utilisation:*  
En python, les vecteurs sont utilisés pour représenter et manipuler des données structurées.

### **Les matrices**
*Définition:*  
Une matrice est un tableau à deux dimensions formés de lignes et de colonnes. 

*Exemple:*  
Prenons la matrice M de dimension (2, 3):  

$$ M =  \begin{pmatrix}
1 & 2 & 3 \\
a & b & c \\
\end{pmatrix} $$

*Utilisation:*  
En python, les matrices sont utilisées pour stocker et manipuler des données tabulaires sous forme de tableaux bidimensionnels. 

### **Les probabilités**
*Définition:*  
La probabilité est une évaluation du caractère probable d'un évènement. Elle est un nombre réél entre 0 et 1.

*Exemple:*  
- Si la probabilité d'un évènement est de 0.6, cela revient à dire que l'évènement a 6 chances sur 10, ou 60% de chance de se produire.  
- Si la probabilité d'un évènement est de 0, cela veut dire que l'évènement est **impossible**  
- Si la probabilité d'un évènement est de 1, cela veut dire que l'évènement est **certain**.

*Utilisation:*  
En python, les probabilités sont utilisées pour effectuer de nombreuses choses comme par exemple modéliser l'incertitude, simuler des phénomènes aléatoires, résoudre des problèmes d'optimisation ou modéliser l'incertitude. 

*Loi de probabilité:*  
Une des lois de probabilités les plus connues est la Loi de Bernouilli. Elle désigne la loi de probabilité d'une variable aléatoire discrète qui prend la valeur 1 avec la probabilité p et 0 avec la probabilité q = 1 - p.  
Elle peut être utilisée par exemple pour le pile ou face et calculer la probabilité que la pièce retombe sur une des deux faces. 
Le calcul serait défini ainsi:  
P(X=x)= p$^x$ ∗ (1−p)$^(1−x)$

### **Les variables indépendantes**
*Définition:*  
Une variable indépendante est une variable qui varie sans être influencée par les autres paramètres du problème. Généralement, une variable indépendante est représentée par "x".  
Elles font opposition aux variables dépendantes qui elles, varient sous l'influence de la variable indépendante. Elle est généralement représentée par "y".  
Le lien entre une variable dépendante et indépendante est appelé relation.

*Exemple:*  
Dans un graphique par exemple, "y" serait l'axe des ordonnées et "x" l'axe des abscisses. 

*Utilisation:*  
En python, les variables indépendantes sont utilisées afin d'analyser et comprendre des phénomènes et des relations de données. Ce qui joue un rôle essentiel pour la construction de modèles où l'exploration de données par exemple. 

### **Les espérances**
*Définition:*  
L'espérance mathématique est étroitement liée aux probabilités.  
Une espérance est la somme des produits des valeurs d'une variable aléatoire par leur probabilité. Cela correspond a une **moyenne pondérée** des résultats d'une expérience aléatoire. Elle est symbolisée par "E".

*Exemple:*  
On se sert souvent de l'espérance dans les jeux de hasards:  
- Si E = 0, alors le jeu est équitable.
- Si E < 0, alors le jeu est désavantageux pour le joueur
- Si E > 0, alors le jeu est avantageux pour le joueur.

Si je propose a un ami de piocher aléatoirement une carte dans un paquet de 52 cartes et que les règles sont les suivantes:
- S'il tire un As, je lui donne 5€
- S'il tire une figure, je lui donne 2€
- S'il tire une tout autre carte, il me donne 1.50€

Pour savoir si le jeu est a son avantage, mon ami devra calculer l'espérnce mathématique du jeu. Pour ce faire, il doit décomposer le probème de la manière suivante:  
- Le jeu contient 4 As sur 52 cartes, la probabilité de piocher un As est de $\frac{4}{52}$


*Utilisation:*  
En python, les variables indépendantes sont utilisées afin d'analyser et comprendre des phénomènes et des relations de données. Ce qui joue un rôle essentiel pour la construction de modèles où l'exploration de données par exemple. 