Ce projet est un jeu de Snake simple implémenté en Python en utilisant la bibliothèque `pygame-ce`. Le jeu présente un
système basé sur une grille où le serpent se déplace et grandit en consommant des fruits qui apparaissent à des
positions aléatoires. Les positions des fruits sont contraintes à être des multiples de la taille des cellules de la
grille, assurant ainsi un alignement parfait avec la grille. Le projet inclut également des couleurs personnalisables, y
compris un fond bleu foncé pour un effet de mode nuit. Le projet est conçu pour fonctionner de manière fluide avec un
taux de rafraîchissement constant et inclut des contrôles de base pour démarrer et arrêter le jeu.

### Instructions pour exécuter le projet

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/LeSurvivant9/python-snake.git
   cd python-snake
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Exécuter le jeu** :
   ```bash
   python main.py
   ```

Ces commandes vous permettront de configurer et d'exécuter le projet sur une machine vierge. Assurez-vous d'avoir Python
et `pip` installés sur votre machine avant de commencer.