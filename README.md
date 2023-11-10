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

## *L'importance des bases mathématiques pour l'apprentissage de la DataScience*
Il est important de connaitre les bases des mathématiques pour l'apprentissage de la Data Science car ce sont les mathématiques qui vont nous permettre de manipuler, analyser et comparer un grand nombre de données.

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
P(X=x)= $p^x$ x (1−p)$^(1−x)$

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
- S'il tire une Figure, je lui donne 2€
- S'il tire une tout autre carte, il me donne 1.50€

Pour savoir si le jeu est a son avantage, mon ami devra calculer l'espérnce mathématique du jeu. Pour ce faire, il doit décomposer le probème de la manière suivante:  

- Le jeu contient 4 As sur 52 cartes, la probabilité de piocher un As est de $\frac{4}{52}$, soit $\frac{1}{13}$.  
Il a donc 1 chance sur 13 de gagner 5€  

- Le jeu contient 12 figures, la probabilité de piocher une Figure est de $\frac{12}{52}$, soit $\frac{3}{13}$. 
Il a donc 3 chances sur 13 de gagner 2€  

- Il reste 36 cartes qui ne sont ni des As ni des Figures, la probabilité de tirer une de ces cartes est de $\frac{36}{52}$, soit $\frac{9}{13}$. 
Il a donc 9 chances sur 13 de perdre 1.50€.  

Avec ces données on peut maintenant calculer l'espérance:  
E = $\frac{1}{13}$ x 5 + $\frac{3}{13}$ x 2 + $\frac{9}{13}$ x -1.50  
E = $\frac{5}{13}$ + $\frac{6}{13}$ - $\frac{13,5}{13}$  
E = $\frac{2,5}{13}$  
E $\approx{-0.19}$

On constace que E < 0 donc le jeu est désavantageux pour mon ami. Je n'ai donc plus qu'a espérer qu'il soit nul en mathématiques afin d'empocher son argent ! 


*Utilisation:*  
En python, les espérances sont utilisées pour quantifier la notion de valeur attendue, notamment en statistiques où en analyse de décision par exemple. Elles permettent de prendre en compte l'incertitude et de calculer des estimations de résultats attendus. 

### **Les variances**
*Définition:*  
La variance est utilisée en tant que mesure servant à caractériser la dispersion d’une distribution ou d’un échantillon. Il est possible de l’interpréter comme la dispersion des valeurs par rapport à la moyenne.
La variance est définie comme la **moyenne des carrés des écarts de la moyenne**.  

*Exemple:*  
La formule de calcul de la variance est:  
V = ( Σ (x-μ)² ) / N

*Utilisation:*  
En pyton, la variance est utilisée notamment en statistiques ou en apprentissage automatique par exemple. 

### **Les écarts types**
*Définition:*  
L'écart-type est une mesure de la dispersion des valeurs d'un échantillon statistique ou d'une distribution de probabilité. Il est défini comme la racine carréé de la **variance** vue juste au dessus. 

*Exemple:*  
La formule de calcul de l'écart-type est:  
s = $\sqrt{V}$

Ou V est la variance. 

### **Les corrélations linéaires**
*Définition:*  
​Le coefficient de corrélation linéaire​, généralement noté "r", quantifie la force du lien linéaire entre les deux caractères d’une distribution. Pour le déterminer, on peut procéder par estimation de son allure graphique ou utiliser une formule mathématique.  
Le coefficient de corrélation aura toujours une valeur qui se situe dans l'intervalle [-1, 1]. 

*Utilisation:*  
En pyton, la corrélation linéaire est utilisée pour mesurer la relation linéaire entre deux variables numériques, principalement pour déterminer si deux variables sont corrélées de manière positive ou négative (si le mouvement d'une variable entraine le mouvement de l'autre dans le même sens).

### **Les moyennes**
*Définition:*  
La moyenne est une mesure de tendance centrale qui représente le centre d'équilibre d'une distribution.  
Il existe deux types de moyennes:  
- La moyenne arithmétique.
- La moyenne pondérée.

*Exemples:*  
La moyenne arithmétique est égale a la somme de toutes les données divisée par le nombre de données.
La moyenne pondérée est égale a la somme des produits des valeurs par leur pondération.

*Utilisation:*  
En pyton, les moyennes sont utilisées pour présenter la tendance centrale des données. 

### **Les médianes**
*Définition:*  
La médiane est la mesure de la tendance centrale qui indique le centre de la série de données. Elle correspond à la valeur qui sépare une distribution ordonnée en deux groupes contenant le même nombre de données. 

*Exemple:*  
La méthode pour déterminer la médiane varie en fonction de la façon dont les données sont représentées:  
- Données énumérées
- Données condensées
- Données groupées en classes

Dans tous les cas, il faut d'abord calculer le rang de la médiane. 

Rang = $\fact{n + 1}{2}$

Ou n = nombre de données.

*Utilisation:*  
En pyton, un peu comme la moyenne, la médiane est utilisée pour représenter une mesure de la tendance centrale.

### **Les minimums & maximums**
*Définition:*  
Les extremums (minimum & maximum absolus) sont les plus petites et plus grandes valeurs d'une fonction.

*Exemple:*  
Pour trouver le **maximum** ou le **minimum** d'une fonction f(x) sur un intervalle ]a,b[, il faut:  
- Déterminer la dérivée de la fonction f'(x).
- Résoudre l'équation f'(x) = 0.
- Vérifier qu'il s'agit d'un maximum ou d'un minimum testant d'autres valeurs de la fonction ou en utilisant la dérivée seconde. 

*Utilisation:*  
En pyton, les extremums sont utilisés pour identifier, résumer, comparer et prendre des décisions basées sur les extrêmes dans les données.

### **Les quartiles**
*Définition:*  
Dans une distribution de données placées en ordre croissant, les **quarts** correspondent a quatre sous-groupes de la distribution qui contiennent le même nombre de données.
Dans une distribution de données placées en ordre croissant, les **quartiles** correspondent aux 3 valeurs qui séparent la distribution en 4 quarts égaux.

- Le premeer quartile, Q1, est la valeur qui sépare le premier quart du reste de la distribution.
- Le deuxième quartile, Q2, est la valeur qui sépare la distribution en deux parties égales. Soit la médiane.
- Le troisième quartile, Q3, est la valeur qui sépare le dernier quart du reste de la distribution. 

*Exemple:*  
Afin de déterminer les quartiles d'une distribution de données il faut:  
- Placer les données par ordre croissant.
- Séparer la distribution de données en quatre quarts égaux.
- Déterminer la valeur des quartiles.

*Utilisation:*  
En pyton, les quartiles sont des outils statistiques essentiels pour la répartition des données. Ils peuvent détecter des valeurs aberrantes exemple.

### **Boxplot**
*Définition:*  
La boxplot, ou encore boite à moustache, est une représentation graphique d'une série statistique qui fait apparaitre bon nombre de certaines des notions que nous venons de voir comme par exemple le **minimum**, le **premier quartile**, la **médiane**, le **troisième quartile** et le **maximum**.  

*Utilisation:*  
En python, elles permettent d'explorer, visualiser et analyser facilement des données et fournissent des informations importantes sur celles-ci.

### **Histogramme**
*Définition:*  
C'est un diagramme servant à représenter par des bandes juxtaposées une distribution d’une statistique sur des données.

*Utilisation:*  
En python, on se sert des histogrammes afin représenter une distribution de données numériques. 

### ** Théorème Central Limite**  
*Définition:*  
Le théorème central limite établit la convergence d’une suite de variables définies sur le même espace vers une loi normale centrée réduite. Plus on additionne de variables aléatoires indépendantes et identiquement distribuées, plus la distribution de probabilité de la nouvelle variable sera proche d’une distribution normale.

### **Les dérivée**
*Définition:*  
La dérivée d'une fonction est le moyen de déterminer combien cette fonction varie quand la quantité dont elle dépend change. Plus précisément, une dérivée est une expression (numérique ou algébrique) donnant le rapport entre les variations infinitésimales de la fonction et les variations infinitésimales de son argument.

*Utilisation:*
En python, il permet d'approximer la distribution moyenne d'échantillon et facilite les analyses statistiques.

*Exemple:*  
Afin de déterminer les quartiles d'une distribution de données il faut:  
- Placer les données par ordre croissant.
- Séparer la distribution de données en quatre quarts égaux.
- Déterminer la valeur des quartiles.

*Utilisation:*  
En pyton, elles permettent de mesurer la variation d'une fonction en rapport à une variable indépendante et donc, de déterminer la pente, le taux de changement et la convexité des fonctions.