![https://azatys.fr](https://uploads-ssl.webflow.com/60abe8f483ffe0cbac324bec/61602a6438c8815d4b8c375e_Logo%20_%20transparent.png)
# Test Technique de recrutement

Test réalisable dans un delai de **24h** qui s'appui sur un API REST en Flask (Python).

## Objectif

L'objectif de ce test est de tester votre capacité à résoudre des réels problèmes via des algorithmes basés sur des structures de données et l'application de certains paradigmes pour organiser et optimiser votre code.

## Prérequis

- Faite un **Fork** de ce repo.

- Installer [python3](https://www.python.org/downloads/release/python-3915)
- Installer pipenv et ajouter le à votre variable d'environnement
```
  pip install pipenv
```

Cette version de python doit être au minimum la 3.9 indiqué dans le fichier Pipfile. Vérifier aussi que vous avez git sur votre poste([Cliquez pour optenir Git](https://git-scm.com/downloads)).

- Télécharger le fichier [ici](https://www.dropbox.com/s/duv704waqjp3tu1/hn_logs.tsv.gz?dl=0), extraire le fichier **hn_logs.tsv** et mettez le à la racine du projet.

- Installer les dépendences
```
  pipenv install
```

- Activer l'environnement virtuel crée
```
  pipenv shell
```
 
Pour lancer l'API (port par defaut: 8000):
```
  python app.py
```
 
Pour lancer les tests :
```
  python unitest.py
```

**NB: Vous n'avez pas besoin de lancer l'API avant de lancer les tests.**


## Enoncé 1

On dispose d'un fichier de log des recherches faite sur un site, dans un fichier .tsv (tabulation separated values)
Chaque ligne se présente sous la forme :
```<Date>\t<Request>\n```

le fichier est disponible [ici](https://www.dropbox.com/s/duv704waqjp3tu1/hn_logs.tsv.gz?dl=0).

L'objectif est de réaliser une API qui exploite les données contenu dans le fichier .tsv, et qui propose 2 endpoints :
- /1/queries/count/<date_prefix>
- /1/queries/popular/<date_prefix>

Conseil :
Au lancement de l'API, il faut lire et charger en mémoire les données du fichier, et ranger les informations dans une structure de donnée qui rendra simple et rapide la récupération des informations demandées.

## Enoncé 2
Vous avez un troixième endpoint `/break_links` qui doit retourner le nombre de liens cassés trouver dans un site web. Pour ce faire, la fonction `count_break_links` doit vérifier que chaque lien est bien fonctionnel sinon le compte comme lien cassé.

L'objectif est que cette route puisse répondre en moins d'une minute peut importe le site à scanner.

*NB: Un lien cassé est un lien non fonctionnel (dont le status code HTTP est >= 400).*

## Règles

Vous ne devez surtout pas modifier les fichiers suivants: 
- `unitest.py`
- `data_test.py`

Vous ne devez pas renommer le nom les fichiers existants.

## À savoir

Vous pourez créer autant de fichier que vous voulez pour organiser votre code.

## Rendu

Après avoir réaliser le test et tester que votre solution est valide avec la commande des tests (cf. Prérequis), vous devez pousser votre solution sur votre repo (celui forké) et faire un mail au recruteur avec le lien de votre repo.

## Auteur
Jordan KAGMENI (Torador)

## Licence
Azatys Licence