# 🎨 Guide de l'Interface Moderne text2svg3d

## Vue d'ensemble

L'interface moderne de text2svg3d offre une expérience utilisateur professionnelle avec :

- 🌓 **Thème clair/sombre** avec basculement instantané
- 🎨 **Design system cohérent** avec palette de couleurs moderne
- 📦 **Architecture modulaire** pour maintenance facilitée
- ✨ **Animations fluides** et effets de survol
- 📱 **Interface responsive** avec cartes élégantes

## Architecture des Composants

### 1. Design System (`design_system.py`)

Le système de design centralise tous les tokens de design pour assurer la cohérence.

#### Palette de Couleurs

**Thème Clair :**
- Primary: `#2563EB` (Bleu vibrant)
- Secondary: `#8B5CF6` (Violet)
- Success: `#10B981` (Vert)
- Warning: `#F59E0B` (Orange)
- Error: `#EF4444` (Rouge)
- Background: `#F9FAFB` (Gris clair)
- Surface: `#FFFFFF` (Blanc)

**Thème Sombre :**
- Primary: `#3B82F6` (Bleu lumineux)
- Secondary: `#A78BFA` (Violet clair)
- Background: `#111827` (Sombre)
- Surface: `#1F2937` (Gris foncé)

#### Typographie

Basée sur **Segoe UI** pour un rendu professionnel cross-platform :

```python
FONTS = {
    "heading_large": ("Segoe UI", 24, "bold"),
    "heading_medium": ("Segoe UI", 18, "bold"),
    "heading_small": ("Segoe UI", 14, "bold"),
    "body_large": ("Segoe UI", 12),
    "body_medium": ("Segoe UI", 11),
    "body_small": ("Segoe UI", 10),
    "code": ("Consolas", 10),
    "button": ("Segoe UI", 11, "bold"),
}
```

#### Système d'Espacement

Basé sur une grille de **8px** pour cohérence :

```python
SPACING = {
    "xs": 4,   # 4px
    "sm": 8,   # 8px
    "md": 16,  # 16px
    "lg": 24,  # 24px
    "xl": 32,  # 32px
    "2xl": 48, # 48px
}
```

#### Bordures Arrondies

```python
RADIUS = {
    "sm": 4,    # Petit
    "md": 8,    # Moyen
    "lg": 12,   # Grand
    "xl": 16,   # Extra-large
    "full": 999,# Complètement arrondi
}
```

#### Icônes Unicode

Utilisation d'icônes Unicode pour éviter les dépendances externes :

```python
ICONS = {
    "text": "📝",
    "font": "🔤",
    "3d": "🎲",
    "generate": "⚡",
    "moon": "🌙",
    "sun": "☀️",
    # ... etc
}
```

### 2. Widgets Modernes (`modern_widgets.py`)

#### ModernButton

Bouton personnalisé avec effets visuels :

```python
button = ModernButton(
    parent,
    text="Générer",
    command=on_click,
    theme=theme,
    variant="primary"  # ou "secondary"
)
```

**Caractéristiques :**
- Basé sur Canvas pour rendu personnalisé
- Effet de survol avec changement de couleur
- Coins arrondis
- Support du thème clair/sombre
- Animation au clic

#### ModernCard

Conteneur de carte avec élévation :

```python
card = ModernCard(
    parent,
    theme=theme,
    title="Ma Section",
    padding=16
)
```

**Caractéristiques :**
- Bordures arrondies
- Ombre portée subtile
- Titre optionnel avec icône
- Adaptation automatique au thème

#### ThemeToggle

Commutateur de thème avec animation :

```python
toggle = ThemeToggle(parent, theme=theme)
```

**Caractéristiques :**
- Icône soleil/lune
- Animation de transition
- Callback automatique au thème
- Survol avec feedback visuel

#### ModernEntry

Champ de saisie avec label flottant :

```python
entry = ModernEntry(
    parent,
    label="Texte",
    variable=text_var,
    theme=theme
)
```

**Caractéristiques :**
- Label flottant animé
- États focus/blur
- Bordure colorée au focus
- Validation visuelle

#### ProgressIndicator

Indicateur de progression circulaire :

```python
progress = ProgressIndicator(parent, theme=theme)
progress.start()  # Démarre l'animation
progress.stop()   # Arrête l'animation
```

**Caractéristiques :**
- Animation fluide
- Couleur adaptée au thème
- Démarrage/arrêt contrôlable

### 3. Fenêtre Moderne (`modern_window.py`)

#### Architecture

```
ModernText2SVG3DWindow
├── Header (logo + thème toggle)
├── ScrollableFrame
│   ├── TextInputCard
│   ├── PreviewCard
│   │   ├── VisualPreview (canvas)
│   │   └── DimensionsPreview
│   ├── FontSelectionCard
│   │   ├── Recherche
│   │   └── Liste déroulante
│   ├── ParametersCard
│   │   ├── Largeur (slider)
│   │   ├── Espacement (slider)
│   │   └── Épaisseur contour (slider)
│   ├── OptionsCard
│   │   ├── Checkbox contour
│   │   └── Checkbox lettres séparées
│   └── OutputCard
│       ├── Bouton générer
│       ├── Indicateur de progression
│       └── Zone de résultats
└── StatusBar
```

#### Système de Thème Réactif

Le système de thème utilise un **pattern observer** :

```python
class Theme:
    def __init__(self, mode: str = "light"):
        self.mode = mode
        self._listeners = []

    def toggle(self) -> str:
        self.mode = "dark" if self.mode == "light" else "light"
        self._notify_listeners()
        return self.mode

    def add_listener(self, callback) -> None:
        self._listeners.append(callback)

    def _notify_listeners(self) -> None:
        for callback in self._listeners:
            callback(self.mode)
```

**Tous les widgets s'abonnent au thème** et se mettent à jour automatiquement :

```python
self.theme.add_listener(self._on_theme_change)

def _on_theme_change(self, new_mode: str) -> None:
    # Mise à jour des couleurs
    self.configure(bg=self.theme.get_color("background"))
    # ... autres mises à jour
```

## Utilisation

### Lancement de l'Interface Moderne

```bash
python -m text2svg3d
```

L'interface moderne est utilisée par défaut depuis `gui/__init__.py`.

### Basculer le Thème

Cliquez sur l'icône ☀️/🌙 en haut à droite pour basculer entre thème clair et sombre.

### Workflow d'Utilisation

1. **Entrer le texte** dans le champ de saisie
2. **Sélectionner une police** (utilisez la recherche pour filtrer)
3. **Ajuster les paramètres** avec les sliders :
   - Largeur finale
   - Espacement entre lettres
   - Épaisseur du contour (si activé)
4. **Voir l'aperçu** en temps réel
5. **Activer les options** si nécessaire :
   - Générer contour
   - Séparer les lettres
6. **Générer** le/les fichier(s) SVG

### Aperçu en Temps Réel

L'aperçu se met à jour automatiquement quand vous :
- Modifiez le texte
- Changez la police
- Ajustez la largeur
- Modifiez l'espacement

**Indicateurs visuels :**
- Texte centré avec la police sélectionnée
- Lignes pointillées bleues pour l'espacement (si > 0)
- Dimensions calculées affichées en dessous

## Avantages de la Nouvelle Interface

### 🎨 Design Moderne

- Palette de couleurs professionnelle inspirée de Tailwind CSS
- Espacement cohérent basé sur une grille de 8px
- Typographie harmonieuse avec Segoe UI
- Bordures arrondies et ombres subtiles

### 🌓 Thème Clair/Sombre

- Basculement instantané sans redémarrage
- Toutes les couleurs adaptées aux deux modes
- Meilleur confort visuel selon préférence utilisateur
- Couleurs optimisées pour lisibilité dans chaque mode

### 📦 Architecture Modulaire

- **design_system.py** : Tous les tokens de design centralisés
- **modern_widgets.py** : Composants réutilisables
- **modern_window.py** : Assemblage de l'interface
- Facile à maintenir et étendre

### ✨ Expérience Utilisateur Améliorée

- Feedback visuel sur toutes les interactions
- Animations fluides (hover, focus, loading)
- Organisation claire en cartes thématiques
- Sliders avec affichage en temps réel des valeurs
- Messages de succès/erreur clairs et formatés

### 🚀 Performance

- Widgets basés sur Canvas pour rendu optimisé
- Pas de dépendances externes (icônes Unicode)
- Mise à jour réactive du thème sans rechargement complet
- Prévisualisation rapide

## Personnalisation

### Ajouter une Nouvelle Couleur

Dans `design_system.py` :

```python
COLORS = {
    "light": {
        "ma_couleur": "#HEXCODE",
        # ...
    },
    "dark": {
        "ma_couleur": "#HEXCODE",
        # ...
    }
}
```

Puis utiliser :

```python
color = theme.get_color("ma_couleur")
```

### Créer un Nouveau Widget

```python
from .design_system import Theme, get_spacing, get_radius

class MonWidget(tk.Frame):
    def __init__(self, parent, theme: Theme, **kwargs):
        super().__init__(parent, **kwargs)
        self.theme = theme

        # S'abonner aux changements de thème
        self.theme.add_listener(self._on_theme_change)

        # Appliquer le thème initial
        self._apply_theme()

    def _apply_theme(self) -> None:
        self.configure(
            bg=self.theme.get_color("surface"),
            # ...
        )

    def _on_theme_change(self, new_mode: str) -> None:
        self._apply_theme()
```

### Modifier les Espacements

Ajustez les valeurs dans `SPACING` pour changer l'espacement global :

```python
SPACING = {
    "xs": 2,   # Plus compact
    "sm": 4,   # Plus compact
    # ...
}
```

## Compatibilité

- ✅ **Python 3.10+**
- ✅ **Windows** (Segoe UI natif)
- ✅ **macOS** (Segoe UI ou fallback)
- ✅ **Linux** (Segoe UI ou fallback)
- ✅ **Tkinter 8.6+** (inclus dans Python)

## Migration depuis l'Ancienne Interface

L'ancienne interface classique est toujours disponible dans `main_window.py`.

Pour revenir à l'interface classique, modifiez `gui/__init__.py` :

```python
# Interface classique
from .main_window import main

# Interface moderne
# from .modern_window import main
```

## Tests

Les widgets modernes sont testés dans `tests/test_gui_components.py` :

```bash
python -m unittest tests.test_gui_components
```

## Feuille de Route Future

### Version 1.1
- [ ] Persistance de la préférence de thème
- [ ] Thèmes personnalisés
- [ ] Raccourcis clavier
- [ ] Mode compact/étendu

### Version 1.2
- [ ] Historique des générations
- [ ] Favoris de polices
- [ ] Prévisualisations 3D
- [ ] Export vers formats multiples

### Version 2.0
- [ ] Éditeur visuel de tracés
- [ ] Bibliothèque de templates
- [ ] Mode batch
- [ ] API web

## Références

- **Design inspiré par** : Tailwind CSS, Material Design 3
- **Icônes** : Unicode Emoji (natif)
- **Fonts** : Segoe UI (Windows), San Francisco (macOS), Fallback (Linux)
- **Pattern** : Observer pattern pour thèmes réactifs

## Support

Pour toute question ou suggestion sur l'interface moderne :

1. Consultez d'abord ce guide
2. Vérifiez les exemples dans `modern_widgets.py`
3. Ouvrez une issue sur GitHub avec le tag `ui/ux`

---

**Créé avec ❤️ pour une expérience utilisateur exceptionnelle**
