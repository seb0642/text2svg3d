# Raccourci Bureau pour text2svg3d

## ✅ Raccourci Créé !

Un raccourci a été créé sur votre bureau : **text2svg3d.desktop**

### 🚀 Comment l'utiliser

**Double-cliquez** sur l'icône "text2svg3d" sur votre bureau pour lancer l'application !

Si c'est la première fois, votre système pourrait afficher un avertissement :
- Cliquez sur "Marquer comme fiable" ou "Autoriser le lancement"
- Ou faites un clic droit → "Autoriser le lancement"

### 📍 Emplacement

Le raccourci se trouve ici :
```
/home/seb/Bureau/text2svg3d.desktop
```

### 🔧 Personnalisation de l'Icône

Si vous voulez changer l'icône :

1. **Trouvez une icône** (format .png, .svg, etc.)
2. **Modifiez le fichier** :
   ```bash
   nano ~/Bureau/text2svg3d.desktop
   ```
3. **Changez la ligne** :
   ```
   Icon=text-editor
   ```
   Par le chemin de votre icône :
   ```
   Icon=/chemin/vers/votre/icone.png
   ```

### 🎨 Icônes Système Disponibles

Vous pouvez utiliser ces noms d'icônes système :
- `text-editor` (icône par défaut)
- `applications-graphics`
- `accessories-text-editor`
- `document-new`
- `application-x-executable`

### 🛠️ Dépannage

#### Le raccourci ne s'affiche pas correctement
```bash
# Actualiser le bureau
killall nautilus
nautilus --no-desktop &
```

#### Le raccourci ne lance pas l'application
```bash
# Vérifier les permissions
chmod +x ~/Bureau/text2svg3d.desktop

# Marquer comme fiable
gio set ~/Bureau/text2svg3d.desktop metadata::trusted true
```

#### Voir les erreurs de lancement
Modifiez le raccourci pour afficher le terminal :
```bash
nano ~/Bureau/text2svg3d.desktop
```
Changez :
```
Terminal=false
```
En :
```
Terminal=true
```

### 📝 Contenu du Raccourci

Le raccourci contient ces informations :
```desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=text2svg3d
Comment=Convertir du texte en SVG pour impression 3D
Exec=bash -c 'cd "/home/seb/projet/fonts to svg/text2svg3d" && ./LANCER-GUI.sh'
Icon=text-editor
Terminal=false
Categories=Graphics;3DGraphics;Utility;
StartupNotify=true
```

### ⭐ Créer une Copie dans le Menu Applications

Pour ajouter l'application au menu de votre système :

```bash
# Copier dans le répertoire des applications
cp ~/Bureau/text2svg3d.desktop ~/.local/share/applications/

# Actualiser le cache
update-desktop-database ~/.local/share/applications/
```

Maintenant l'application apparaîtra aussi dans votre menu d'applications !

### 🗑️ Supprimer le Raccourci

Si vous voulez le retirer du bureau :
```bash
rm ~/Bureau/text2svg3d.desktop
```

Pour le retirer du menu :
```bash
rm ~/.local/share/applications/text2svg3d.desktop
update-desktop-database ~/.local/share/applications/
```

---

## 🎉 Utilisation Rapide

1. **Double-clic** sur l'icône "text2svg3d" sur votre bureau
2. L'interface graphique s'ouvre
3. Tapez votre texte, choisissez une police
4. Cliquez "Generate SVG"
5. Le fichier est créé dans `~/Bureau/ready to blender/` ! 🚀

**C'est aussi simple que ça !**
