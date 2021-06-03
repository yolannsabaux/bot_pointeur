# bot_pointeur

## Merci à Joffrey (https://github.com/Joffreybvn)
Ce code est uniquement du code écrit par Joffrey et arrangé par moi-même.

## Tuto

Pour faire fonctionner ce code, différentes variables doivent être modifiées pour contenir vos informations.

### 0) Modification du fichier contenant vos variables d'identification
Modifier le fichier `variables_template.py` dans le dossier `utils` en `variables.py`

### 1) Initialiser Token Becode
Dans le fichier [``variables.py``](https://github.com/yolannos/bot_pointeur/blob/main/utils/variables_template.py) vous devez changer la valeur de `token` par votre token BeCode que vous pouvez vous procurer:

- soit en le générant à l'adresse `https://my.becode.org/profile/junior/prénom-nom/token` 
- soit en inspectant votre navigateur (Chrome only) > application > local storage > my.becode.org > jwt-token
![Philadelphia's Magic Gardens. This place was so cool!](./assets/token.png "Philadelphia's Magic Gardens")


### 2) Changer paramètres Envoi de mail
Dans le fichier [``variables.py``](https://github.com/yolannos/bot_pointeur/blob/main/utils/variables_template.py) vous devez changer le:

- `sender_email`: l'adresse avec laquelle vous souhaitez envoyer le mail de confirmation
- `receiver_email`: l'adresse à laquelle vous voulez envoyer le mail de confirmation
- `password`: avec Gmail, il est nécessaire d'utiliser un App Passwords que vous pouvez générer en suivant le tuto [ici](https://support.google.com/accounts/answer/185833?hl=en).

## TODO
- ~~beginner level: Créer une condition pour initialiser la variable période en fonction de l'heure~~
- ~~intermediate level: Créer un cron qui exécute le script~~
- expert level: créer un serveur qui exécute le script 4 fois par jour
