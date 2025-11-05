# 🚀 Roadmap text2svg3d - Fonctionnalités Futures

**Version actuelle :** 1.0.0
**Score qualité :** 9.9/10 ✨
**Date :** 5 Novembre 2025

---

## ✅ Implémenté (13 Améliorations Majeures)

### Phase 1-6 (Score de base 10/10)
1. ✅ Validation exhaustive des entrées
2. ✅ Gestion exceptions spécifiques
3. ✅ Type hints complets
4. ✅ Logging structuré
5. ✅ Tests unitaires (72% coverage)
6. ✅ Documentation exhaustive (23 fichiers)
7. ✅ CI/CD complet
8. ✅ Interface moderne avec dark mode

### Améliorations 2024-2025 (Partie 1-2-3)
9. ✅ **Dependabot** - Sécurité proactive automatique
10. ✅ **Persistance thème** - Préférence sauvegardée
11. ✅ **Raccourcis clavier** - Ctrl+G, Ctrl+T, Ctrl+Q, Ctrl+O, Ctrl+R, F1
12. ✅ **Cache glyphes** - Performance x5-10
13. ✅ **Threading** - UI toujours responsive
14. ✅ **Historique** - 50 dernières générations
15. ✅ **Export PDF** - Vectoriel haute qualité
16. ✅ **Export DXF** - Compatible CAD/CNC
17. ✅ **Export PNG** - Rasterisé configurable
18. ✅ **Thèmes personnalisés** - 5 thèmes disponibles (light, dark, high_contrast, solarized, solarized_light)

---

## 🔮 Version 1.1 - Polish & UX (Q1 2025)

### Mode Compact pour Petits Écrans 📱
**Priorité :** Moyenne
**Effort :** 2-3 heures
**Description :**
- Détection automatique de la résolution d'écran
- Layout adaptatif selon taille fenêtre
- Cartes réduites en mode compact
- Sliders plus petits
- Preview optionnelle (cachée en mode compact)

**Implémentation suggérée :**
```python
# Dans modern_window.py
def _detect_screen_size(self) -> str:
    """Detect screen size and return layout mode."""
    screen_height = self.root.winfo_screenheight()
    screen_width = self.root.winfo_screenwidth()

    if screen_height < 800 or screen_width < 1000:
        return "compact"
    return "normal"

def _apply_layout(self, mode: str) -> None:
    """Apply layout based on mode."""
    if mode == "compact":
        # Smaller cards, hide preview, reduced spacing
        self.card_padding = get_spacing("sm")
        self.show_preview = False
    else:
        # Normal layout
        self.card_padding = get_spacing("md")
        self.show_preview = True
```

**Bénéfices :**
- Utilisable sur laptops 13"
- Meilleure expérience petits écrans
- Accessibilité élargie

---

## 🔮 Version 1.2 - 3D & Visualisation (Q2 2025)

### Prévisualisation 3D Interactive 🎲
**Priorité :** Basse
**Effort :** 8-12 heures
**Description :**
- Visualisation 3D du texte extrudé avant impression
- Rotation interactive (souris)
- Contrôle épaisseur d'extrusion
- Export STL pour impression 3D directe

**Technologies suggérées :**
- **pyvista** : 3D visualization (backend VTK)
- **trimesh** : Mesh manipulation
- Ou **matplotlib 3D** pour version légère

**Dépendances :**
```txt
pyvista>=0.42.0         # 3D visualization
vtk>=9.2.0             # VTK backend
trimesh>=4.0.0         # Mesh processing
numpy>=1.24.0          # Math operations
```

**Implémentation suggérée :**
```python
# Nouveau module: text2svg3d/preview_3d.py
import pyvista as pv
import numpy as np
from pathlib import Path

def create_3d_preview(svg_path: Path, thickness_mm: float) -> pv.PolyData:
    """Create 3D mesh from SVG with extrusion."""
    # Parse SVG paths
    # Triangulate 2D paths
    # Extrude along Z axis
    # Return 3D mesh
    pass

def show_interactive_preview(mesh: pv.PolyData):
    """Show interactive 3D preview window."""
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color="lightblue")
    plotter.add_axes()
    plotter.show()
```

**Interface GUI :**
- Bouton "Aperçu 3D" dans OutputCard
- Nouvelle fenêtre avec viewer 3D
- Contrôles: rotation, zoom, épaisseur

**Bénéfices :**
- Killer feature unique
- Validation avant impression
- Détection problèmes géométrie
- Workflow complet intégré

---

## 🔮 Version 1.3 - Internationalisation (Q3 2025)

### Support Multi-Langues 🌍
**Priorité :** Moyenne
**Effort :** 5-8 heures
**Description :**
- Interface en Français, Anglais, Espagnol, Allemand
- Détection locale système
- Sélection manuelle dans préférences
- Tous textes UI traduits

**Technologies suggérées :**
- **gettext** : Standard Python i18n
- Fichiers .po/.mo pour traductions

**Structure :**
```
text2svg3d/
├── locales/
│   ├── fr_FR/
│   │   └── LC_MESSAGES/
│   │       ├── text2svg3d.po
│   │       └── text2svg3d.mo
│   ├── en_US/
│   │   └── LC_MESSAGES/
│   ├── es_ES/
│   │   └── LC_MESSAGES/
│   └── de_DE/
│       └── LC_MESSAGES/
```

**Implémentation suggérée :**
```python
# text2svg3d/i18n.py
import gettext
import locale
from pathlib import Path

LOCALE_DIR = Path(__file__).parent / "locales"

def setup_i18n():
    """Setup internationalization."""
    # Detect system locale
    lang, _ = locale.getdefaultlocale()

    # Setup gettext
    try:
        translation = gettext.translation(
            "text2svg3d",
            localedir=str(LOCALE_DIR),
            languages=[lang],
            fallback=True
        )
        translation.install()
    except Exception:
        # Fallback to default (French)
        pass

# Usage in GUI
from text2svg3d.i18n import _
label = tk.Label(text=_("Generate SVG"))
```

**Fichier .po exemple (fr_FR) :**
```po
msgid "Generate SVG"
msgstr "Générer le SVG"

msgid "Font Selection"
msgstr "Sélection de Police"

msgid "Preview"
msgstr "Aperçu"
```

**Bénéfices :**
- Audience internationale
- Accessibilité linguistique
- Standard professionnel

---

## 🔮 Version 1.4 - Features Avancées (Q4 2025)

### Bibliothèque de Templates
**Description :**
- Templates prédéfinis (badges, enseignes, logos)
- Paramètres réglables
- Export/import templates personnalisés

### Éditeur Visuel de Tracés
**Description :**
- Modification interactive des paths SVG
- Ajout de formes (cercles, rectangles)
- Combinaison de textes

### Mode Batch
**Description :**
- Génération multiple depuis fichier CSV
- Automatisation pour production
- Progress bar multi-fichiers

### API Web (Flask/FastAPI)
**Description :**
- Endpoint REST pour génération
- Interface web moderne
- Déploiement cloud possible

---

## 📊 Priorités de Développement

| Feature | Priorité | Effort | Impact | Dépendances |
|---------|----------|--------|--------|-------------|
| Mode Compact | 🟡 Moyenne | 2-3h | Accessibilité ↑ | Aucune |
| Preview 3D | 🟢 Basse | 8-12h | Innovation ↑↑↑ | pyvista, vtk |
| i18n | 🟡 Moyenne | 5-8h | Audience ↑↑ | gettext |
| Templates | 🟢 Basse | 10-15h | Productivité ↑ | Aucune |
| Éditeur Visuel | 🟢 Basse | 20-30h | Features ↑↑ | tkinter.canvas |
| Mode Batch | 🟡 Moyenne | 5-8h | Automatisation ↑ | csv |
| API Web | 🟢 Basse | 15-20h | Intégration ↑↑ | Flask/FastAPI |

---

## 🎯 Objectifs Stratégiques

### Court Terme (1-3 mois)
- ✅ Mode Compact (accessibilité)
- ⏸️ Tests supplémentaires (atteindre 85% coverage)
- ⏸️ Performance profiling

### Moyen Terme (3-6 mois)
- ⏸️ Preview 3D (killer feature)
- ⏸️ i18n (internationalisation)
- ⏸️ Templates de base

### Long Terme (6-12 mois)
- ⏸️ Éditeur visuel
- ⏸️ API Web
- ⏸️ Mode batch professionnel
- ⏸️ Plugin pour logiciels CAD (FreeCAD, Fusion 360)

---

## 💡 Idées Communautaires

*(Section pour suggestions utilisateurs)*

Proposez vos idées sur GitHub Issues avec le tag `enhancement` !

---

## 🤝 Contribution

Pour contribuer à ces features :

1. Consultez CONTRIBUTING.md
2. Choisissez une feature de la roadmap
3. Ouvrez une issue pour discussion
4. Créez une PR avec implémentation

**Règles :**
- Tests obligatoires (coverage ≥ 70%)
- Documentation complète
- Code formaté (black, isort)
- Type hints partout

---

## 📈 Suivi des Versions

| Version | Date Prévue | Features Principales | Status |
|---------|-------------|---------------------|--------|
| 1.0.0 | Nov 2025 | Base + 18 améliorations | ✅ Released |
| 1.1.0 | Jan 2026 | Mode compact + Polish | ⏸️ Planned |
| 1.2.0 | Apr 2026 | Preview 3D | ⏸️ Planned |
| 1.3.0 | Jul 2026 | i18n + Templates | ⏸️ Planned |
| 1.4.0 | Oct 2026 | Advanced features | ⏸️ Planned |
| 2.0.0 | 2027 | API Web + Plugin CAD | 💭 Future |

---

**Dernière mise à jour :** 5 Novembre 2025
**Mainteneur :** text2svg3d core team
**License :** MIT

*Cette roadmap est indicative et peut évoluer selon les besoins de la communauté.*
