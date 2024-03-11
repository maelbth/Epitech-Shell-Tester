# Projet Epitech | Tester de l'interpréteur de commandes

Vous trouverez ici un petit tutoriel pour utiliser le script.

## Pré-requis

Cette étape est importante, vous devez la suivre strictement.

### Installation

Vous devez copier l'intégralité du dépôt dans un dossier nommer `tests`, là
où se trouve l'executable de l'interpréteur de commandes.

```bash
.
├── mysh
└── tests
    └── tester
        ├── compare.py
        ├── files
        │   └── segv.sh
        ├── tester.py
        └── tests.json
```

## Démarrage

Pour executer le test vous devez utiliser la commande suivante :
```
python ./tests/tester/tester.py
```

## Comprendre les résultats

* Lorsque le mot clé `matching` est donnée, le test vérifie que les arguments
sont présents dans le résultat du test.

* Lorsque le mot clé `mismatching` est donnée, le test vérifie que les
arguments __ne sont pas__ présents dans le résultat du test.

* Autrement, le test vérifie que le résultat est identique.

> Si le test échoue, l'erreur associée est affichée.

## Aller plus loin !

Vous pouvez créer vos propres tests en les ajoutant [ici](./tests.json).
Attention à la syntaxe.

* Création d'un test simple

Les commandes lister sont executer à la suite.

```json
{
    "name":"Nom du test",
    "command":[
        "Les",
        "Commandes",
        "À",
        "Executer"
    ]
}
```

* Modification des variables d'environement

L'interpréteur de commandes utilisera les variables d'environement données.

```json
{
    "env":{
        "SCHOOL":"EPITECH",
        "USER":"STUDENT"
    }
}
```

* Trouver une correspondance

Le test cherche les variables données.

```json
{
    "matching":[
        "Hello"
    ],
    "mismatching":[
        "World"
    ]
}
```

## Auteur

**Maël Bertocchi** [@Github](https://github.com/maelbth) → Merci de me
contacter si vous rencontrez un problème.
