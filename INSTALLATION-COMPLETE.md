# Installation Complète - text2svg3d avec Interface Graphique

Guide d'installation pas à pas pour utiliser text2svg3d avec son interface graphique.

## 📋 Étape 1 : Installer les Dépendances Système

Ces commandes installent tous les paquets nécessaires pour faire fonctionner l'application.

```bash
# Mise à jour de la liste des paquets
sudo apt update

# Installation de Python, pip, tkinter et les bibliothèques de développement
sudo apt install python3-tk python3-pip python3-dev libfreetype6-dev

# Installation de polices de base (si vous n'en avez pas)
sudo apt install fonts-dejavu fonts-liberation fonts-freefont-ttf
```

**Explications :**
- `python3-tk` : Interface graphique tkinter
- `python3-pip` : Gestionnaire de paquets Python
- `python3-dev` : Fichiers de développement Python
- `libfreetype6-dev` : Bibliothèque pour le rendu des polices
- `fonts-*` : Polices TrueType pour l'impression 3D

## 📦 Étape 2 : Installer les Dépendances Python

```bash
# Installer les bibliothèques Python nécessaires
pip3 install --user fonttools freetype-py svgwrite
```

**Note :** Le flag `--user` installe les paquets pour votre utilisateur uniquement, sans nécessiter les droits root.

## ✅ Étape 3 : Vérifier l'Installation

```bash
# Vérifier que tkinter fonctionne
python3 -c "import tkinter; print('✅ tkinter OK')"

# Vérifier que les dépendances Python sont installées
python3 -c "import freetype; import fontTools; import svgwrite; print('✅ Dépendances Python OK')"

# Vérifier les polices disponibles
fc-list | grep -i ttf | wc -l
```

Si toutes les commandes s'exécutent sans erreur, vous êtes prêt !

## 🚀 Étape 4 : Lancer l'Interface Graphique

```bash
# Se déplacer dans le répertoire du projet
cd ~/projet/fonts\ to\ svg/text2svg3d

# Lancer l'interface graphique
./LANCER-GUI.sh
```

Ou directement :

```bash
python3 ~/projet/fonts\ to\ svg/text2svg3d/text2svg3d-gui.py
```

## 🎯 Alternative : Installation avec Environnement Virtuel

Si vous préférez une installation plus isolée :

```bash
cd ~/projet/fonts\ to\ svg/text2svg3d

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer l'application
pip install -e .

# Lancer l'interface graphique
text2svg3d-gui

# Ou la ligne de commande
text2svg3d --list-fonts
```

**Pour les prochaines utilisations :**
```bash
cd ~/projet/fonts\ to\ svg/text2svg3d
source venv/bin/activate
text2svg3d-gui
```

## 🔧 Résolution des Problèmes Courants

### Problème 1 : "pip3: command not found"

```bash
sudo apt install python3-pip
```

### Problème 2 : "No module named 'tkinter'"

```bash
sudo apt install python3-tk
```

### Problème 3 : "externally-managed-environment"

C'est normal sur les systèmes récents. Utilisez l'une de ces solutions :

**Solution A (Recommandée) :** Installer avec `--user`
```bash
pip3 install --user fonttools freetype-py svgwrite
```

**Solution B :** Utiliser un environnement virtuel (voir section ci-dessus)

### Problème 4 : "No fonts found"

```bash
# Installer des polices de base
sudo apt install fonts-dejavu fonts-liberation

# Vérifier les polices installées
fc-list | grep -i ttf
```

### Problème 5 : Erreur lors de la compilation de freetype-py

```bash
# Installer les dépendances de développement
sudo apt install python3-dev libfreetype6-dev
```

## 📝 Résumé Ultra-Court

```bash
# 1. Tout installer (une seule fois)
sudo apt update && sudo apt install python3-tk python3-pip python3-dev libfreetype6-dev fonts-dejavu
pip3 install --user fonttools freetype-py svgwrite

# 2. Lancer (à chaque fois)
cd ~/projet/fonts\ to\ svg/text2svg3d
./LANCER-GUI.sh
```

## 🎨 Première Utilisation

Une fois l'interface ouverte :

1. **Entrez du texte** : Par exemple "HELLO"
2. **Choisissez une police** : Par exemple "DejaVu Sans"
3. **Ajustez la taille** : Par exemple 30mm
4. **Cliquez sur "Generate SVG"**
5. **Le fichier est créé !** → Importez-le dans votre slicer 3D

Consultez le **[Guide de l'Interface Graphique](GUI_GUIDE.md)** pour plus de détails.

## 📱 Créer un Raccourci Bureau (Optionnel)

Pour lancer l'application depuis votre menu :

```bash
# Créer le fichier de raccourci
cat > ~/.local/share/applications/text2svg3d.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=text2svg3d GUI
Comment=Convert text to SVG for 3D printing
Exec=python3 /home/$USER/projet/fonts to svg/text2svg3d/text2svg3d-gui.py
Icon=text-editor
Terminal=false
Categories=Graphics;3DGraphics;
EOF

# Rendre le fichier exécutable
chmod +x ~/.local/share/applications/text2svg3d.desktop

# Actualiser le cache des applications
update-desktop-database ~/.local/share/applications/
```

Maintenant cherchez "text2svg3d" dans votre menu d'applications !

## ✨ C'est Tout !

Vous êtes maintenant prêt à créer des textes SVG pour vos impressions 3D avec une interface graphique simple et intuitive.

**Bon amusement ! 🚀**

---

## 🆘 Besoin d'Aide ?

- **Interface Graphique :** Voir [GUI_GUIDE.md](GUI_GUIDE.md)
- **Ligne de commande :** Voir [README.md](README.md)
- **Installation :** Relire ce fichier
- **Démarrage rapide :** Voir [QUICKSTART.md](QUICKSTART.md)
