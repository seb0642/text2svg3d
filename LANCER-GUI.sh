#!/bin/bash
# Script de lancement simple pour l'interface graphique text2svg3d

echo "======================================"
echo "  text2svg3d - Interface Graphique"
echo "======================================"
echo ""

# Vérifier si les dépendances sont installées
if ! python3 -c "import freetype; import fontTools; import svgwrite" 2>/dev/null; then
    echo "⚠️  Dépendances manquantes détectées"
    echo ""
    echo "Installation des dépendances..."
    pip3 install --user fonttools freetype-py svgwrite
    echo ""
fi

# Vérifier tkinter
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ Erreur: tkinter n'est pas installé"
    echo ""
    echo "Pour installer tkinter, exécutez :"
    echo "  sudo apt install python3-tk"
    echo ""
    exit 1
fi

echo "✅ Lancement de l'interface graphique..."
echo ""

# Lancer l'interface
cd "$(dirname "$0")"
python3 text2svg3d-gui.py

echo ""
echo "Interface fermée."
