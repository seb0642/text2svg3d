# Interface Graphique text2svg3d

Guide d'utilisation de l'interface graphique pour convertir du texte en SVG pour l'impression 3D.

## 🚀 Lancement Rapide (SANS Installation)

```bash
# Installer uniquement les dépendances Python nécessaires
pip3 install --user fonttools freetype-py svgwrite

# Lancer l'interface graphique
cd ~/projet/fonts\ to\ svg/text2svg3d
python3 text2svg3d-gui.py
```

C'est tout ! L'interface graphique s'ouvre directement.

## 📦 Installation Complète (avec environnement virtuel)

Si vous préférez une installation propre :

```bash
cd ~/projet/fonts\ to\ svg/text2svg3d

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate

# Installer l'application
pip install -e .

# Lancer l'interface graphique
text2svg3d-gui

# Ou directement
python3 text2svg3d-gui.py
```

## 🖥️ Utilisation de l'Interface

### 1. Fenêtre Principale

L'interface contient :

```
┌─────────────────────────────────────────┐
│   Text to SVG Converter for 3D Printing │
├─────────────────────────────────────────┤
│ Text to convert:                        │
│ [HELLO________________________]         │
├─────────────────────────────────────────┤
│ Font Selection                          │
│ Filter: [____________]                  │
│ Font:   [DejaVu Sans ▼]                │
├─────────────────────────────────────────┤
│ Parameters                              │
│ Size (mm):         [====o======] 20.0   │
│ Letter Spacing:    [o===========] 0.0   │
│ Thickness (mm):    [==o=========] 2.0   │
├─────────────────────────────────────────┤
│ Output file: [output.svg] [Browse...]   │
├─────────────────────────────────────────┤
│ Preview                                 │
│ Text: "HELLO"                           │
│ Font: DejaVu Sans                       │
│ Dimensions: 85.50mm × 20.00mm          │
├─────────────────────────────────────────┤
│        [Generate SVG]                   │
├─────────────────────────────────────────┤
│ Status: Ready                           │
└─────────────────────────────────────────┘
```

### 2. Étapes pour Créer un SVG

#### Étape 1 : Entrer le texte
- Tapez votre texte dans le champ "Text to convert"
- Exemple : `HELLO`, `LOGO`, `ABC123`

#### Étape 2 : Choisir une police
- **Filtrer** : Tapez dans "Filter" pour chercher (ex: "Arial", "Bold")
- **Sélectionner** : Choisissez dans la liste déroulante
- Les polices recommandées pour l'impression 3D :
  - DejaVu Sans
  - DejaVu Sans Bold
  - Liberation Sans
  - Arial (si disponible)

#### Étape 3 : Ajuster les paramètres
- **Size** (5-100mm) : Hauteur du texte
  - Petit (10-15mm) : Étiquettes
  - Moyen (20-30mm) : Usage général
  - Grand (40-60mm) : Logos

- **Letter Spacing** (0-10mm) : Espacement entre lettres
  - 0mm : Lettres collées
  - 2-3mm : Bon espacement
  - 5mm+ : Très espacé

- **Thickness** (1-10mm) : Épaisseur suggérée pour l'extrusion 3D
  - 2mm : Standard
  - 3-4mm : Plus robuste

#### Étape 4 : Vérifier l'aperçu
L'aperçu affiche automatiquement :
- Le texte à convertir
- La police sélectionnée
- Les dimensions finales (largeur × hauteur)
- Le nombre de caractères

#### Étape 5 : Choisir le fichier de sortie
- Cliquez sur **Browse...** pour choisir l'emplacement
- Ou laissez `output.svg` par défaut
- Le fichier sera créé dans le répertoire courant

#### Étape 6 : Générer !
- Cliquez sur **Generate SVG**
- Une fenêtre de confirmation s'affiche avec les dimensions
- Le fichier SVG est créé et prêt à être importé dans votre slicer 3D

### 3. Conseils d'Utilisation

#### Recherche Rapide de Police
```
Filter: "bold"    → Affiche toutes les polices en gras
Filter: "sans"    → Affiche les polices sans-serif
Filter: "mono"    → Affiche les polices monospace
```

#### Paramètres Recommandés

**Pour un logo :**
```
Text: LOGO
Font: Liberation Sans Bold
Size: 40mm
Letter Spacing: 3mm
Thickness: 4mm
```

**Pour une étiquette :**
```
Text: ON/OFF
Font: DejaVu Sans
Size: 15mm
Letter Spacing: 1mm
Thickness: 2mm
```

**Pour un numéro de maison :**
```
Text: 123
Font: DejaVu Sans Bold
Size: 60mm
Letter Spacing: 2mm
Thickness: 5mm
```

### 4. Messages et Erreurs

#### Messages de Statut
- **"Ready"** : Prêt à générer
- **"Loading fonts..."** : Chargement des polices
- **"Loaded X fonts"** : X polices disponibles
- **"Showing X fonts"** : X polices après filtrage
- **"SVG created: ..."** : Succès !

#### Erreurs Courantes

**"Please enter text to convert"**
→ Vous avez oublié d'entrer du texte

**"Please select a font"**
→ Sélectionnez une police dans la liste

**"No characters could be converted"**
→ La police ne supporte pas ces caractères, essayez une autre police

**"Font not found"**
→ Sélectionnez à nouveau la police dans la liste

## 🎨 Workflow Complet

1. **Créer le SVG**
   ```bash
   python3 text2svg3d-gui.py
   ```

2. **Configurer**
   - Entrer : "HELLO"
   - Police : DejaVu Sans Bold
   - Taille : 30mm
   - Générer

3. **Importer dans le Slicer**
   - PrusaSlicer : File → Import → Import SVG
   - Cura : Extensions → SVG Import
   - Sélectionner le fichier créé

4. **Configurer l'extrusion**
   - Profondeur : 2-3mm (utilisez la valeur "Thickness")
   - Matériau : PLA/PETG/ABS selon préférence

5. **Slicer et Imprimer !**

## 🔧 Dépannage

### L'interface ne se lance pas

**Erreur : No module named 'tkinter'**
```bash
# Installer tkinter
sudo apt install python3-tk
```

**Erreur : No module named 'freetype'**
```bash
# Installer les dépendances
pip3 install --user fonttools freetype-py svgwrite
```

### Aucune police n'apparaît

```bash
# Vérifier les polices installées
fc-list | grep -i ttf | head

# Installer des polices de base
sudo apt install fonts-dejavu fonts-liberation
```

### Le SVG ne s'affiche pas correctement

- Ouvrez le fichier `.svg` dans un navigateur web pour vérifier
- Importez dans Inkscape pour éditer si nécessaire
- Assurez-vous que votre slicer supporte les SVG

## 🚀 Astuces Pro

### Créer Plusieurs Fichiers Rapidement
1. Générez le premier SVG
2. Changez le texte
3. Cliquez sur Browse... pour changer le nom
4. Générez à nouveau

### Tester Différentes Tailles
1. Utilisez le slider "Size" pour tester
2. Regardez l'aperçu des dimensions
3. Trouvez la taille parfaite avant de générer

### Comparer des Polices
1. Gardez le même texte et les mêmes paramètres
2. Changez uniquement la police
3. Comparez les dimensions dans l'aperçu

## 📝 Raccourci Desktop (Optionnel)

Pour lancer l'interface directement depuis votre bureau :

```bash
# Créer un lanceur
cat > ~/.local/share/applications/text2svg3d.desktop <<EOF
[Desktop Entry]
Type=Application
Name=text2svg3d GUI
Comment=Convert text to SVG for 3D printing
Exec=python3 "$HOME/projet/fonts to svg/text2svg3d/text2svg3d-gui.py"
Icon=text-editor
Terminal=false
Categories=Graphics;3DGraphics;
EOF

# Rendre exécutable
chmod +x ~/.local/share/applications/text2svg3d.desktop
```

Maintenant vous pouvez lancer l'application depuis le menu de votre système !

## 🎯 Résumé Ultra-Rapide

```bash
# 1. Installer les dépendances (une fois)
pip3 install --user fonttools freetype-py svgwrite

# 2. Lancer
python3 ~/projet/fonts\ to\ svg/text2svg3d/text2svg3d-gui.py

# 3. Dans l'interface :
#    - Entrer le texte
#    - Choisir la police
#    - Ajuster la taille
#    - Cliquer "Generate SVG"
#
# 4. Importer le SVG dans votre slicer 3D
#
# 5. Imprimer ! 🎉
```

Bon amusement avec vos impressions 3D ! 🚀
