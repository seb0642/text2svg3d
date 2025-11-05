# Contour pour Impression 3D Multi-Couleur

## ✨ Nouvelle Fonctionnalité : Génération de Contour

Vous pouvez maintenant **générer un fichier de contour séparé** pour créer des impressions 3D multi-couleur !

## 🎯 À quoi ça sert ?

### Le Problème
Quand vous imprimez du texte 3D en une seule couleur, il peut être difficile à lire selon l'angle et l'éclairage.

### La Solution
Générez **deux fichiers SVG** :
1. **Le texte principal** (ex: `LOGO.svg`)
2. **Le contour** (ex: `LOGO_contour.svg`)

Dans votre slicer 3D, importez les deux fichiers avec **des couleurs différentes** pour un effet visuel spectaculaire !

## 🎨 Exemple Visuel

```
┌─────────────────────────────────┐
│                                 │
│   Sans contour (1 couleur) :   │
│   ┌─────┐                       │
│   │HELLO│  ← Texte noir simple  │
│   └─────┘                       │
│                                 │
│   Avec contour (2 couleurs) :  │
│   ┌─────┐                       │
│   │█████│  ← Contour blanc      │
│   │█HEL█│  ← Texte noir         │
│   │█████│  ← + effet de bordure │
│   └─────┘                       │
│                                 │
└─────────────────────────────────┘
```

## 🔧 Comment l'utiliser

### 1. Activer l'Option

Dans la section **"Options de Contour"** :
```
┌───────────────────────────────────────┐
│ Options de Contour                    │
├───────────────────────────────────────┤
│ ☑ Générer un fichier de contour      │
│   séparé                              │
│                                       │
│ Épaisseur du contour (mm) :          │
│ [====o===========] [1.5]             │
│       ↑               ↑              │
│    Curseur        Saisie             │
└───────────────────────────────────────┘
```

**Étapes :**
1. ✅ **Cochez** "Générer un fichier de contour séparé"
2. 🎚️ **Ajustez** l'épaisseur du contour (0.5 à 5 mm)
3. 🖱️ **Cliquez** "Générer le SVG"

### 2. Résultat

Vous obtiendrez **deux fichiers** :

```
/home/seb/Bureau/ready to blender/
├── LOGO.svg          ← Texte principal
└── LOGO_contour.svg  ← Contour
```

### 3. Importation dans le Slicer 3D

#### Dans PrusaSlicer / Cura / Autres :

1. **Importez le fichier de contour** (`LOGO_contour.svg`)
   - Réglez la hauteur (ex: 0.2 mm pour la première couche)
   - Choisissez la couleur 1 (ex: blanc)

2. **Importez le fichier principal** (`LOGO.svg`)
   - Réglez la même hauteur que le contour
   - Choisissez la couleur 2 (ex: noir)

3. **Alignez les deux fichiers** (ils doivent se superposer parfaitement)

4. **Lancez l'impression** !

## 📐 Réglage de l'Épaisseur

### Avec le Curseur
- **Déplacez** le curseur de 0.5 à 5 mm
- Parfait pour tester rapidement

### Avec la Saisie Manuelle
- **Cliquez** dans le champ
- **Tapez** la valeur exacte (ex: `1.5`)
- **Appuyez** sur Entrée

### Recommandations

| Taille du texte | Épaisseur contour recommandée |
|-----------------|-------------------------------|
| 10-20 mm        | 0.5 - 1.0 mm                  |
| 20-40 mm        | 1.0 - 2.0 mm                  |
| 40-60 mm        | 2.0 - 3.0 mm                  |
| 60+ mm          | 3.0 - 5.0 mm                  |

**Astuce** : Plus le texte est grand, plus le contour peut être épais !

## 💡 Exemples Pratiques

### Exemple 1 : Logo en Relief

**Objectif** : Logo noir avec bordure blanche

```
Configuration :
- Texte : "LOGO"
- Taille : 30 mm
- Contour : ✅ Activé
- Épaisseur contour : 2.0 mm

Résultat :
- LOGO.svg (texte noir)
- LOGO_contour.svg (bordure blanche)

Dans le slicer :
1. Importer LOGO_contour.svg → Filament blanc
2. Importer LOGO.svg → Filament noir
3. Hauteur totale : 3 mm
```

### Exemple 2 : Badge Nominatif

**Objectif** : Nom lisible de loin

```
Configuration :
- Texte : "JEAN"
- Taille : 25 mm
- Contour : ✅ Activé
- Épaisseur contour : 1.5 mm

Résultat :
- JEAN.svg (texte)
- JEAN_contour.svg (bordure)

Impression :
- Contour rouge
- Texte blanc
- Effet : Texte blanc sur fond rouge !
```

### Exemple 3 : Enseigne de Magasin

**Objectif** : Grande enseigne visible

```
Configuration :
- Texte : "OUVERT"
- Taille : 80 mm
- Contour : ✅ Activé
- Épaisseur contour : 4.0 mm

Résultat :
- OUVERT.svg (texte principal)
- OUVERT_contour.svg (contour large)

Impression :
- Contour vert foncé
- Texte vert clair
- Hauteur : 5 mm
```

## 🎨 Combinaisons de Couleurs

### Contraste Fort (Recommandé)
- ✅ Noir + Blanc
- ✅ Rouge + Blanc
- ✅ Bleu + Jaune
- ✅ Vert foncé + Blanc

### Dégradés Subtils
- 🟦 Bleu foncé + Bleu clair
- 🟩 Vert foncé + Vert clair
- 🟥 Rouge foncé + Rouge clair

### Effet Néon
- 💜 Violet + Rose
- 🔵 Bleu + Cyan
- 🟠 Orange + Jaune

## ⚙️ Détails Techniques

### Comment ça marche ?

Le fichier de contour utilise la propriété SVG `stroke` (trait) :
- Le texte principal : `fill` seulement
- Le contour : `fill` + `stroke` avec épaisseur ajustable

### Dimensions

Quand le contour est activé :
- **Padding automatique** : L'épaisseur du contour est ajoutée de chaque côté
- **Canvas agrandi** : Pour que le contour ne soit pas coupé

**Exemple :**
```
Texte : 50 mm × 20 mm
Contour : 2 mm

Dimensions fichier texte :
- Largeur : 50 mm
- Hauteur : 20 mm

Dimensions fichier contour :
- Largeur : 54 mm (50 + 2×2)
- Hauteur : 24 mm (20 + 2×2)
```

### Propriétés SVG du Contour

```svg
<path
  d="..."
  fill="black"
  stroke="black"
  stroke-width="2.0mm"
  stroke-linejoin="round"
  stroke-linecap="round"
  fill-rule="evenodd"
/>
```

**Avantages** :
- `stroke-linejoin="round"` : Angles arrondis pour meilleure impression
- `stroke-linecap="round"` : Extrémités arrondies
- Pas de coins pointus difficiles à imprimer

## 📋 Workflow Complet

```
1. Ouvrez text2svg3d
         ↓
2. Tapez votre texte (ex: "LOGO")
         ↓
3. Choisissez la police
         ↓
4. Réglez la taille (ex: 30 mm)
         ↓
5. ✅ Cochez "Générer un fichier de contour séparé"
         ↓
6. Ajustez l'épaisseur (ex: 2.0 mm)
         ↓
7. Cliquez "Générer le SVG"
         ↓
8. Deux fichiers créés :
   - LOGO.svg
   - LOGO_contour.svg
         ↓
9. Ouvrez votre slicer 3D
         ↓
10. Importez LOGO_contour.svg → Couleur 1
         ↓
11. Importez LOGO.svg → Couleur 2
         ↓
12. Alignez les deux fichiers
         ↓
13. Réglez les hauteurs
         ↓
14. Lancez l'impression ! 🚀
```

## ✅ Avantages

### Pour la Lisibilité
- ✅ **Meilleur contraste** : Le contour fait ressortir le texte
- ✅ **Visible de loin** : Effet visuel marqué
- ✅ **Moins de reflets** : Deux couleurs différentes

### Pour l'Esthétique
- ✅ **Effet professionnel** : Look premium
- ✅ **Personnalisation** : Choix illimité de combinaisons
- ✅ **Créativité** : Expérimentez avec les couleurs

### Pour l'Impression
- ✅ **Angles arrondis** : Meilleure adhérence des couches
- ✅ **Pas de supports** : Impression directe sur le plateau
- ✅ **Rapide** : Quelques millimètres de hauteur suffisent

## 🚨 Conseils Importants

### ⚠️ À Faire
- ✅ Tester d'abord avec une petite taille
- ✅ Vérifier l'alignement dans le slicer
- ✅ Utiliser des couleurs contrastées
- ✅ Adapter l'épaisseur à la taille du texte

### ❌ À Éviter
- ❌ Contour trop épais pour petit texte (illisible)
- ❌ Contour trop fin pour grand texte (invisible)
- ❌ Couleurs trop similaires (pas de contraste)
- ❌ Oublier d'aligner les deux fichiers dans le slicer

## 🛠️ Dépannage

### Le contour dépasse du texte
**Cause** : Épaisseur trop élevée

**Solution** :
- Réduisez l'épaisseur du contour
- Essayez 0.5 ou 1.0 mm pour commencer

### Les fichiers ne s'alignent pas dans le slicer
**Cause** : Importation incorrecte

**Solution** :
1. Importez d'abord le contour
2. Puis le texte principal
3. Vérifiez que les coordonnées X,Y sont identiques
4. Utilisez la fonction "Centrer" du slicer si nécessaire

### Le contour cache le texte
**Cause** : Ordre d'impression incorrect

**Solution** :
- Dans le slicer, vérifiez l'ordre des objets
- Le contour doit être EN DESSOUS du texte
- Ou bien imprimez-les à la même hauteur avec changement de filament

## 💡 Astuces Pro

### Astuce 1 : Test Rapide
Avant d'imprimer grand :
1. Générez avec taille 20 mm
2. Testez différentes épaisseurs (0.5, 1.0, 2.0)
3. Imprimez les trois versions
4. Choisissez celle qui rend le mieux

### Astuce 2 : Multi-Matériaux
Si votre imprimante a plusieurs extrudeurs :
1. Assignez le contour à l'extrudeur 1
2. Assignez le texte à l'extrudeur 2
3. Impression automatique en deux couleurs !

### Astuce 3 : Effet 3D
Pour un effet de profondeur :
1. Imprimez le contour (2 couches, 0.4 mm)
2. Imprimez le texte (4 couches, 0.8 mm)
3. Le texte ressort en relief !

### Astuce 4 : Réutilisation
Gardez vos fichiers :
- `LOGO.svg` → Texte en bleu, rouge, vert...
- `LOGO_contour.svg` → Toujours en blanc
- Réimprimez avec différentes couleurs sans régénérer !

## 🎉 Résumé

**Avec la fonctionnalité de contour :**
- 🎨 **Créativité** : Impressions multi-couleur facilement
- 📐 **Précision** : Épaisseur ajustable de 0.5 à 5 mm
- 🚀 **Simplicité** : Une case à cocher, c'est tout !
- 💪 **Résultat pro** : Textes qui sortent du lot

**Essayez maintenant ! Activez l'option de contour et créez vos premiers textes multi-couleur ! 🚀**

---

## 📖 Documentation Associée

- **SAISIE-MANUELLE.md** : Saisie précise des paramètres au clavier
- **MISE-A-JOUR.md** : Nom de fichier automatique basé sur le texte
- **RACCOURCI-BUREAU.md** : Lancer l'application depuis le bureau

---

**text2svg3d** - Convertissez du texte en SVG pour impression 3D ! 🎯
