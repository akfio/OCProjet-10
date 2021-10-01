Créez une API sécurisée RESTful en utilisant Django REST
----------------------------------------------------------------------------------------------

## Installation

Tout d'abord, créez un dossier via la commande mkdir (ici projet10) dans lequel se trouvera l'environnement virtuel et l'application. Puis y accéder via la commande cd.

```python
mkdir projet10
cd projet10
```
Placer le dossier softdesk dedans.

```python
gh repo clone akfio/OCProjet-10
```

créez un environnement virtuel dans le dossier projet10 (ici nommé env):
```python
python3 -m venv env
```
Puis activez l'environnement virtuel via :

```python
source env/bin/activate #MacOS ou Unix
ou
env/Scripts/activate.bat #Sur Windows
```

Importer les packages nécessaire avec la commande :

```python 
pip install -r requirements.txt
``` 

## Lancer le serveur de l'application
Dans le dossier du projet softdesk saisissez : 

```python
python3 manage.py runserver
```

Vous pouvez ensuite lancer le serveur via l'addresse affichée sur votre console 

