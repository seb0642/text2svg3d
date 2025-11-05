# 👋 Bienvenue dans text2svg3d !

Créez facilement des fichiers SVG à partir de texte pour vos impressions 3D.

## 🎯 Par Où Commencer ?

### Option 1 : Interface Graphique (RECOMMANDÉ - Plus Facile)

**Pour ceux qui préfèrent cliquer plutôt que taper des commandes.**

1. **Installation :**
   ```bash
   sudo apt update
   sudo apt install python3-tk python3-pip python3-dev libfreetype6-dev fonts-dejavu
   pip3 install --user fonttools freetype-py svgwrite
   ```

2. **Lancement :**
   ```bash
   cd ~/projet/fonts\ to\ svg/text2svg3d
   ./LANCER-GUI.sh
   ```

3. **Documentation complète :**
   - 📖 **[INSTALLATION-COMPLETE.md](INSTALLATION-COMPLETE.md)** - Installation pas à pas
   - 🖥️ **[GUI_GUIDE.md](GUI_GUIDE.md)** - Utilisation de l'interface graphique

---

### Option 2 : Ligne de Commande (Pour les Utilisateurs Avancés)

**Pour ceux qui préfèrent utiliser le terminal.**

1. **Installation :**
   ```bash
   cd ~/projet/fonts\ to\ svg/text2svg3d
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

2. **Utilisation :**
   ```bash
   text2svg3d --list-fonts
   text2svg3d "HELLO"
   text2svg3d -f "Arial" -s 30 "LOGO"
   ```

3. **Documentation :**
   - 📖 **[README.md](README.md)** - Documentation complète
   - 🚀 **[QUICKSTART.md](QUICKSTART.md)** - Guide de démarrage rapide

---

## 🎨 Utilisation Typique

### Avec l'Interface Graphique

```
1. Lancer : ./LANCER-GUI.sh
2. Entrer le texte : "HELLO"
3. Choisir une police : "DejaVu Sans"
4. Ajuster la taille : 30mm
5. Cliquer "Generate SVG"
6. Importer dans votre slicer 3D
7. Imprimer ! 🎉
```

### Avec la Ligne de Commande

```bash
# Lister les polices
text2svg3d --list-fonts

# Créer un SVG
text2svg3d -f "DejaVu Sans" -s 30 -o hello.svg "HELLO"

# Importer hello.svg dans votre slicer 3D
# Imprimer ! 🎉
```

---

## 📚 Documentation Disponible

| Fichier | Description | Pour qui ? |
|---------|-------------|------------|
| **[INSTALLATION-COMPLETE.md](INSTALLATION-COMPLETE.md)** | Installation pas à pas avec GUI | Débutants |
| **[GUI_GUIDE.md](GUI_GUIDE.md)** | Guide complet de l'interface graphique | Utilisateurs GUI |
| **[QUICKSTART.md](QUICKSTART.md)** | Démarrage rapide en ligne de commande | Utilisateurs CLI |
| **[README.md](README.md)** | Documentation complète | Tous |
| **[INSTALL.md](INSTALL.md)** | Instructions d'installation détaillées | Problèmes d'installation |
| **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** | Architecture du projet | Développeurs |

---

## 🆘 Problèmes Fréquents

### "No module named 'tkinter'"
```bash
sudo apt install python3-tk
```

### "pip3: command not found"
```bash
sudo apt install python3-pip
```

### "No fonts found"
```bash
sudo apt install fonts-dejavu fonts-liberation
```

### "externally-managed-environment"
```bash
pip3 install --user fonttools freetype-py svgwrite
# ou utilisez un environnement virtuel (voir INSTALLATION-COMPLETE.md)
```

---

## ⚡ Commande Magique (Installation Rapide)

**Pour installer tout d'un coup :**

```bash
# Installation complète en une commande
sudo apt update && \
sudo apt install -y python3-tk python3-pip python3-dev libfreetype6-dev fonts-dejavu fonts-liberation && \
pip3 install --user fonttools freetype-py svgwrite && \
echo "✅ Installation terminée ! Lancez maintenant :" && \
echo "   cd ~/projet/fonts\ to\ svg/text2svg3d && ./LANCER-GUI.sh"
```

---

## 🎯 Workflow Recommandé

```
┌──────────────────┐
│  text2svg3d GUI  │
└────────┬─────────┘
         │
         ▼
   ┌───────────┐
   │ Texte SVG │
   └─────┬─────┘
         │
         ▼
   ┌───────────┐
   │   Slicer  │ (PrusaSlicer, Cura, etc.)
   └─────┬─────┘
         │
         ▼
   ┌───────────┐
   │ Fichier   │
   │   STL     │
   └─────┬─────┘
         │
         ▼
   ┌───────────┐
   │ Imprimante│
   │     3D    │
   └─────┬─────┘
         │
         ▼
    🎉 Succès !
```

---

## 💡 Conseils pour Débuter

1. **Commencez simple** : Utilisez l'interface graphique avec du texte court ("ABC")
2. **Polices recommandées** : DejaVu Sans, Liberation Sans (sans-serif fonctionnent mieux)
3. **Taille standard** : 20-30mm pour commencer
4. **Épaisseur** : 2-3mm pour la plupart des applications
5. **Testez dans le slicer** : Vérifiez toujours le SVG avant d'imprimer

---

## 🚀 Prêt à Commencer ?

### Je veux l'interface graphique (plus facile) :
👉 Voir **[INSTALLATION-COMPLETE.md](INSTALLATION-COMPLETE.md)**

### Je préfère la ligne de commande :
👉 Voir **[QUICKSTART.md](QUICKSTART.md)**

### J'ai besoin d'aide :
👉 Voir **[README.md](README.md)**

---

**Bon amusement avec vos créations 3D ! 🎨🖨️**
