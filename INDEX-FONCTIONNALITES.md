# Index des Fonctionnalités - text2svg3d

## 📚 Guide de Référence Complet

Bienvenue ! Ce document liste toutes les fonctionnalités disponibles et leur documentation.

---

## 🚀 Démarrage Rapide

### Première Installation

```bash
# Installer les dépendances
pip3 install --user fonttools freetype-py svgwrite

# Installer le support graphique (si nécessaire)
sudo apt install python3-tk

# Lancer l'interface graphique
./LANCER-GUI.sh
```

### Utilisation Basique

1. **Double-cliquez** sur l'icône `text2svg3d` sur votre bureau
2. **Tapez** votre texte
3. **Choisissez** une police
4. **Ajustez** les paramètres
5. **Cliquez** "Générer le SVG"
6. Le fichier est créé dans `/home/seb/Bureau/ready to blender/`

---

## 📖 Documentation Disponible

### 1. Interface Graphique
**Fichier** : `GUI_GUIDE.md`

**Contenu** :
- Lancement de l'interface
- Sélection de police
- Paramètres de base
- Génération du SVG

**Pour qui** : Débutants et utilisateurs qui préfèrent une interface visuelle

---

### 2. Raccourci Bureau
**Fichier** : `RACCOURCI-BUREAU.md`

**Contenu** :
- Emplacement du raccourci
- Comment l'utiliser
- Personnalisation de l'icône
- Ajout au menu Applications
- Dépannage

**Pour qui** : Tous les utilisateurs qui veulent un accès rapide

---

### 3. Nom de Fichier Automatique
**Fichier** : `MISE-A-JOUR.md`

**Contenu** :
- Génération automatique du nom de fichier
- Règles de nommage (espaces, caractères spéciaux)
- Exemples pratiques
- Modification manuelle

**Pour qui** : Utilisateurs qui génèrent beaucoup de fichiers différents

**Exemple** :
```
Vous tapez "LOGO" → Le fichier s'appelle "LOGO.svg"
Vous tapez "Mon Texte" → Le fichier s'appelle "Mon_Texte.svg"
```

---

### 4. Saisie Manuelle des Paramètres
**Fichier** : `SAISIE-MANUELLE.md`

**Contenu** :
- Utilisation des curseurs
- Saisie au clavier pour plus de précision
- Utilisation des flèches ▲▼
- Exemples pour chaque paramètre :
  - Taille (5 à 100 mm)
  - Espacement (0 à 10 mm)
  - Épaisseur (1 à 10 mm)

**Pour qui** : Utilisateurs qui ont besoin de valeurs précises

**Exemple** :
```
Besoin de 35.5 mm exactement ?
→ Cliquez dans le champ
→ Tapez "35.5"
→ Appuyez sur Entrée
✅ Précision parfaite !
```

---

### 5. Contour pour Impression Multi-Couleur
**Fichier** : `CONTOUR-3D.md` ⭐

**Contenu** :
- Génération de fichier de contour séparé
- Réglage de l'épaisseur (0.5 à 5 mm)
- Guide d'importation dans le slicer
- Combinaisons de couleurs recommandées
- Exemples pratiques (logo, badge, enseigne)
- Conseils d'impression

**Pour qui** : Utilisateurs qui veulent des impressions en deux couleurs

**Résultat** :
```
Génération de deux fichiers :
- LOGO.svg (texte principal)
- LOGO_contour.svg (bordure)

Dans le slicer :
- Importer le contour → Couleur 1 (ex: blanc)
- Importer le texte → Couleur 2 (ex: noir)
→ Impression multi-couleur automatique ! 🎨
```

---

### 6. Lettres Séparées pour Arc-en-Ciel
**Fichier** : `LETTRES-SEPAREES.md` ⭐ **NOUVEAU !**

**Contenu** :
- Un fichier SVG par lettre
- Chaque lettre dans une couleur différente
- Combinaison possible avec les contours
- Guide d'importation dans le slicer
- Idées de combinaisons de couleurs (arc-en-ciel, dégradés)
- Exemples pratiques détaillés

**Pour qui** : Utilisateurs qui veulent des impressions multicolores (3+ couleurs)

**Résultat** :
```
Texte "LOGO" génère 4 fichiers :
- LOGO_lettre_1_L.svg
- LOGO_lettre_2_O.svg
- LOGO_lettre_3_G.svg
- LOGO_lettre_4_O.svg

Dans le slicer :
- Importer L → 🔴 Rouge
- Importer O → 🟡 Jaune
- Importer G → 🟢 Vert
- Importer O → 🔵 Bleu
→ Arc-en-ciel ! 🌈
```

---

## 🎯 Fonctionnalités par Cas d'Usage

### Je veux créer un texte simple
📖 Lisez : `GUI_GUIDE.md`
- Lancement
- Sélection police
- Génération basique

---

### Je veux des valeurs précises
📖 Lisez : `SAISIE-MANUELLE.md`
- Saisie au clavier
- Valeurs exactes (25.5 mm, 1.8 mm, etc.)

---

### Je veux organiser mes fichiers
📖 Lisez : `MISE-A-JOUR.md`
- Noms de fichiers automatiques
- Organisation dans "ready to blender"

---

### Je veux une impression multi-couleur (2 couleurs)
📖 Lisez : `CONTOUR-3D.md`
- Génération de contour
- Importation dans le slicer
- Combinaisons de couleurs

---

### Je veux une impression arc-en-ciel (3+ couleurs)
📖 Lisez : `LETTRES-SEPAREES.md` ⭐ NOUVEAU
- Séparation automatique des lettres
- Un fichier par lettre
- Chaque lettre dans une couleur différente

---

### Je veux un accès rapide
📖 Lisez : `RACCOURCI-BUREAU.md`
- Double-clic depuis le bureau
- Ajout au menu Applications

---

## ⚙️ Fonctionnalités Principales

### ✅ Interface Graphique Complète
- [x] Interface en français
- [x] Aperçu visuel de la police
- [x] Curseurs + saisie manuelle
- [x] Affichage des dimensions
- [x] Messages de succès détaillés

### ✅ Gestion des Fichiers
- [x] Chemin de sortie personnalisé
- [x] Nom de fichier automatique basé sur le texte
- [x] Sanitisation des caractères spéciaux
- [x] Création automatique du dossier de sortie

### ✅ Paramètres Ajustables
- [x] Taille : 5 à 100 mm
- [x] Espacement : 0 à 10 mm
- [x] Épaisseur : 1 à 10 mm
- [x] Saisie au clavier ou curseur
- [x] Valeurs décimales supportées

### ✅ Contour Multi-Couleur ⭐ NOUVEAU
- [x] Génération de fichier de contour séparé
- [x] Épaisseur ajustable : 0.5 à 5 mm
- [x] Padding automatique
- [x] Angles arrondis pour meilleure impression
- [x] Nomenclature automatique (_contour)

### ✅ Aperçu et Visualisation
- [x] Aperçu visuel de la police choisie
- [x] Affichage des dimensions en temps réel
- [x] Barre de statut avec informations

### ✅ Facilité d'Accès
- [x] Raccourci bureau
- [x] Script de lancement (.sh)
- [x] Vérification automatique des dépendances

---

## 🔄 Workflow Complet Recommandé

### Projet Simple (1 couleur)

```
1. Double-clic sur "text2svg3d"
         ↓
2. Tapez votre texte (ex: "LOGO")
         ↓
3. Choisissez la police
         ↓
4. Ajustez la taille avec le curseur
         ↓
5. Affinez avec la saisie manuelle si besoin
         ↓
6. Cliquez "Générer le SVG"
         ↓
7. Importez LOGO.svg dans votre slicer
         ↓
8. Imprimez ! 🚀
```

### Projet Multi-Couleur (avec contour)

```
1. Double-clic sur "text2svg3d"
         ↓
2. Tapez votre texte (ex: "LOGO")
         ↓
3. Choisissez la police
         ↓
4. Ajustez la taille (ex: 30 mm)
         ↓
5. ✅ Cochez "Générer un fichier de contour séparé"
         ↓
6. Ajustez l'épaisseur du contour (ex: 2 mm)
         ↓
7. Cliquez "Générer le SVG"
         ↓
8. Deux fichiers créés :
   - LOGO.svg
   - LOGO_contour.svg
         ↓
9. Dans le slicer :
   - Importer LOGO_contour.svg → Couleur 1
   - Importer LOGO.svg → Couleur 2
         ↓
10. Alignez les fichiers
         ↓
11. Imprimez en multi-couleur ! 🎨
```

---

## 📐 Spécifications Techniques

### Formats Supportés
- **Entrée** : Polices TrueType (.ttf) et OpenType (.otf)
- **Sortie** : SVG optimisé pour impression 3D

### Optimisations SVG
- Chemins fermés (commande Z)
- Coordonnées absolues
- Unités en millimètres
- fill-rule="evenodd" pour lettres avec trous (O, A, B)
- Pas de transformations (tout est calculé)

### Contour Technique
- Propriété `stroke` pour le contour
- `stroke-linejoin="round"` (angles arrondis)
- `stroke-linecap="round"` (extrémités arrondies)
- Padding automatique basé sur l'épaisseur
- Canvas agrandi pour inclure le contour

---

## 🛠️ Dépannage Rapide

### L'application ne se lance pas
📖 **Solution** : `RACCOURCI-BUREAU.md` section "Dépannage"
```bash
./LANCER-GUI.sh  # Affiche les erreurs détaillées
```

### Je ne trouve pas ma police
📖 **Solution** : `GUI_GUIDE.md` section "Polices"
- Utilisez la barre de recherche
- Les polices système sont automatiquement détectées

### Le nom de fichier contient des caractères bizarres
📖 **Solution** : `MISE-A-JOUR.md` section "Règles de Nommage"
- Les espaces deviennent des underscores
- Les caractères spéciaux sont remplacés

### Le contour est trop épais
📖 **Solution** : `CONTOUR-3D.md` section "Réglage de l'Épaisseur"
- Réduisez l'épaisseur du contour
- Consultez le tableau des recommandations

### Les fichiers ne s'alignent pas dans le slicer
📖 **Solution** : `CONTOUR-3D.md` section "Dépannage"
- Importez d'abord le contour, puis le texte
- Vérifiez les coordonnées X,Y

---

## 💡 Astuces Générales

### Astuce 1 : Organisation des Fichiers
Le dossier de sortie est :
```
/home/seb/Bureau/ready to blender/
```
Tous vos SVG sont créés ici automatiquement !

### Astuce 2 : Valeurs Favorites
Créez un petit pense-bête avec vos valeurs préférées :
- Logo : 30 mm, espacement 2 mm, épaisseur 3 mm
- Badge : 25 mm, espacement 1.5 mm, épaisseur 2.5 mm
- Enseigne : 80 mm, espacement 4 mm, épaisseur 5 mm

### Astuce 3 : Test Avant Impression
1. Générez en petit (20 mm)
2. Testez différentes épaisseurs de contour
3. Imprimez les tests
4. Choisissez la meilleure combinaison
5. Régénérez en grand

### Astuce 4 : Réutilisation
Les fichiers SVG sont réutilisables :
- Gardez vos SVG favoris
- Réimprimez avec différentes couleurs
- Pas besoin de régénérer !

---

## 📊 Tableau de Référence Rapide

| Paramètre | Min | Max | Unité | Recommandé |
|-----------|-----|-----|-------|------------|
| Taille | 5 | 100 | mm | 20-30 |
| Espacement | 0 | 10 | mm | 0-2 |
| Épaisseur | 1 | 10 | mm | 2-3 |
| Contour | 0.5 | 5 | mm | 1-2 |

---

## 🎓 Parcours d'Apprentissage

### Débutant
1. ✅ Lisez `GUI_GUIDE.md`
2. ✅ Créez votre premier SVG simple
3. ✅ Lisez `RACCOURCI-BUREAU.md`

### Intermédiaire
4. ✅ Lisez `SAISIE-MANUELLE.md`
5. ✅ Expérimentez avec les valeurs précises
6. ✅ Lisez `MISE-A-JOUR.md`

### Avancé
7. ✅ Lisez `CONTOUR-3D.md`
8. ✅ Créez votre première impression multi-couleur
9. ✅ Maîtrisez les combinaisons de couleurs

---

## 🆕 Quoi de Neuf ?

### Version Actuelle

#### ⭐ Fonctionnalité de Contour (NOUVEAU !)
- Génération de fichier de contour séparé
- Épaisseur ajustable 0.5-5 mm
- Padding automatique
- Documentation complète

#### ✅ Fonctionnalités Précédentes
- Interface graphique en français
- Saisie manuelle des paramètres
- Nom de fichier automatique
- Aperçu visuel de la police
- Raccourci bureau

---

## 📞 Besoin d'Aide ?

### Documentation Complète
Tous les fichiers de documentation sont dans :
```
/home/seb/projet/fonts to svg/text2svg3d/
```

### Liste des Fichiers
- `README.md` - Documentation générale (anglais)
- `GUI_GUIDE.md` - Guide de l'interface graphique
- `SAISIE-MANUELLE.md` - Saisie précise au clavier
- `MISE-A-JOUR.md` - Nom de fichier automatique
- `RACCOURCI-BUREAU.md` - Raccourci et lancement
- `CONTOUR-3D.md` - Impression multi-couleur ⭐
- `INDEX-FONCTIONNALITES.md` - Ce fichier !

---

## 🎉 Résumé

**text2svg3d** est maintenant un outil complet pour convertir du texte en SVG pour impression 3D :

✅ **Interface intuitive** en français
✅ **Saisie précise** au clavier
✅ **Organisation automatique** des fichiers
✅ **Aperçu visuel** en temps réel
✅ **Accès rapide** depuis le bureau
✅ **Impression multi-couleur** avec contours ⭐

**Bonne impression 3D ! 🚀**

---

**text2svg3d** - Transformez vos idées en objets 3D ! 🎯
