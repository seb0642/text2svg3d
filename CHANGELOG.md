# Changelog - text2svg3d

## Version 1.1.0 - Améliorations Interface Graphique

### ✨ Nouveautés

#### 1. Aperçu Visuel de la Police
- **Nouvelle zone d'aperçu** : Un canvas affiche votre texte avec la police sélectionnée
- **Mise à jour en temps réel** : L'aperçu se met à jour automatiquement quand vous :
  - Changez le texte
  - Changez la police
  - Ajustez la taille
- **Affichage centré** : Le texte est affiché au centre avec une taille proportionnelle
- **Messages informatifs** :
  - "Entrez du texte pour voir l'aperçu..." quand le champ est vide
  - "Sélectionnez une police..." si aucune police n'est choisie
  - Note si l'aperçu est approximatif (police non disponible dans tkinter)

#### 2. Chemin de Sortie Personnalisé
- **Nouveau répertoire par défaut** : `/home/seb/Bureau/ready to blender`
- **Création automatique** : Le répertoire est créé automatiquement s'il n'existe pas
- **Dialogue Browse amélioré** : S'ouvre directement dans le bon répertoire
- **Fallback intelligent** : Si le répertoire ne peut pas être créé, utilise le répertoire courant

### 🎨 Interface

#### Avant :
```
┌─────────────────────────────┐
│ Text: [HELLO___]            │
├─────────────────────────────┤
│ Font Selection              │
│ Font: [DejaVu Sans ▼]      │
├─────────────────────────────┤
│ Preview                     │
│ Text: "HELLO"               │
│ Dimensions: 85.50mm × 20mm  │
└─────────────────────────────┘
```

#### Après :
```
┌─────────────────────────────┐
│ Text: [HELLO___]            │
├─────────────────────────────┤
│ Aperçu Visuel               │
│ ┌───────────────────────┐   │
│ │      HELLO            │   │ ← Rendu avec la police
│ └───────────────────────┘   │
├─────────────────────────────┤
│ Font Selection              │
│ Font: [DejaVu Sans ▼]      │
├─────────────────────────────┤
│ Preview                     │
│ Text: "HELLO"               │
│ Dimensions: 85.50mm × 20mm  │
└─────────────────────────────┘
```

### 📁 Fichiers Modifiés

1. **text2svg3d/config.py**
   - Ajout de `DEFAULT_OUTPUT_DIR`
   - Modification de `DEFAULT_OUTPUT_FILE` pour utiliser le nouveau chemin

2. **text2svg3d/gui.py**
   - Ajout de l'import `font as tkfont`
   - Nouvelle méthode `_update_visual_preview()`
   - Nouvelle méthode `_ensure_output_directory()`
   - Modification de `_browse_output()` pour initialdir
   - Ajout du canvas d'aperçu visuel
   - Augmentation de la fenêtre : 700x600 → 750x700

### 🔧 Détails Techniques

#### Aperçu Visuel
- Utilise `tkinter.Canvas` pour le rendu
- Essaie de matcher la police système avec les polices tkinter disponibles
- Algorithme de matching :
  1. Recherche exacte du nom
  2. Recherche partielle (nom de base)
  3. Fallback sur police par défaut
- Taille d'affichage : `max(12, min(48, size_mm * 1.5))`

#### Gestion du Répertoire
- Création avec `Path.mkdir(parents=True, exist_ok=True)`
- Gestion des erreurs avec fallback sur répertoire courant
- Vérification de l'existence avant utilisation dans Browse

### 📝 Notes d'Utilisation

**Chemin de sortie :**
- Par défaut : `~/Bureau/ready to blender/output.svg`
- Modifiable via le bouton "Browse..."
- Le répertoire est créé automatiquement au lancement

**Aperçu :**
- Montre le rendu approximatif de la police
- Si la police n'est pas disponible dans tkinter, affiche un message
- Le SVG final utilisera toujours la police correcte (FreeType)

---

## Version 1.0.0 - Version Initiale

### Fonctionnalités
- Interface graphique complète avec tkinter
- Sélection de polices système
- Filtrage de polices par regex
- Paramètres ajustables (taille, espacement, épaisseur)
- Génération SVG optimisée pour impression 3D
- Aperçu des dimensions
- Interface en ligne de commande (CLI)

### Documentation
- README.md complet
- Guide d'installation (INSTALL.md)
- Guide de démarrage rapide (QUICKSTART.md)
- Guide de l'interface graphique (GUI_GUIDE.md)
- Structure du projet (PROJECT_STRUCTURE.md)
