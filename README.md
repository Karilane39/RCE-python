
# Remote Command Execution and Shell Management

Ce projet implémente un serveur et un client de communication socket pour l'exécution à distance de commandes système via un canal réseau. Le serveur écoute sur un port spécifique et permet l'exécution de commandes, ainsi que le lancement de processus via un client connecté. Le client peut interagir avec le serveur pour envoyer des commandes et recevoir les résultats.

## Fonctionnalités

- Le **serveur** écoute les connexions entrantes sur un port défini (`6666` par défaut).
- Il permet l'exécution de commandes système (comme `ls`, `pwd`, etc.) envoyées par le client.
- Il gère une commande spéciale `bomb`, qui tente de lancer un fork (processus parallèle) sur le serveur. Ce processus peut entraîner des erreurs selon l'environnement d'exécution.
- Le serveur renvoie les résultats ou les erreurs au client.

## Prérequis

- Python 3.x
- Accès au réseau pour que le serveur et le client puissent se connecter.

## Installation

1. Clonez ou téléchargez le dépôt contenant les fichiers `server.py` et `client.py`.

2. Assurez-vous que vous avez Python 3 installé sur votre machine.

## Exécution

### Serveur

Pour démarrer le serveur, exécutez le fichier `server.py` :

```bash
python3 server.py
```

Le serveur attendra des connexions sur le port `6666`. Il peut être configuré pour écouter sur un autre port en modifiant la variable `evil_socket_port`.

### Client

Le client devra se connecter au serveur en utilisant l'adresse IP et le port du serveur. Exécutez le fichier `client.py` et entrez l'adresse IP du serveur lorsque cela vous est demandé.

```bash
python3 client.py
```

Après la connexion, vous pourrez envoyer des commandes système au serveur. Tapez les commandes et appuyez sur **Entrée** pour les envoyer. Si vous souhaitez quitter, tapez `exit`.

### Commandes

- `bomb` : Lance un processus fork. Cette commande peut entraîner une erreur selon l'environnement.
- Toute autre commande : Les commandes système valides seront exécutées, et la sortie sera renvoyée au client.

### Exemple d'utilisation

1. Exécutez le serveur sur une machine avec `python3 server.py`.
2. Exécutez le client sur une autre machine avec `python3 client.py`.
3. Connectez-vous au serveur en entrant l'adresse IP.
4. Envoyez des commandes via le client. Par exemple, tapez `ls` pour afficher les fichiers du répertoire courant.

---

## Sécurité

**Avertissement** : Ce projet est un simple exercice de démonstration et **ne doit pas être utilisé en production**. L'exécution de commandes arbitraires via des sockets peut présenter des risques de sécurité importants. Veuillez ne pas utiliser ce code dans des environnements non contrôlés ou accessibles au public.

---

## Développement

### Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer le projet, veuillez forker le dépôt, créer une branche, et soumettre une pull request.
