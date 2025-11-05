# Lettres Séparées - Impression Multi-Couleur

## ✨ Fonctionnalité : Un Fichier par Lettre

Générez **un fichier SVG distinct pour chaque lettre** de votre texte pour créer des impressions 3D aux couleurs de l'arc-en-ciel ! 🌈

---

## 🎯 À Quoi Ça Sert ?

### Le Problème

Quand vous générez `LOGO.svg`, toutes les lettres sont dans **un seul fichier**. Dans le slicer, c'est **un seul objet** → donc **une seule couleur**.

### La Solution

Avec l'option **"Séparer chaque lettre"**, vous obtenez :

```
📁 ready to blender/
├── LOGO_lettre_1_L.svg  ← L seule
├── LOGO_lettre_2_O.svg  ← O seule
├── LOGO_lettre_3_G.svg  ← G seule
└── LOGO_lettre_4_O.svg  ← O seule
```

**Dans le slicer :**
- Importez `LOGO_lettre_1_L.svg` → 🔴 Rouge
- Importez `LOGO_lettre_2_O.svg` → 🟡 Jaune
- Importez `LOGO_lettre_3_G.svg` → 🟢 Vert
- Importez `LOGO_lettre_4_O.svg` → 🔵 Bleu

**Résultat : LOGO en 4 couleurs ! 🌈**

---

## 🔧 Comment l'utiliser

### Étape 1 : Ouvrir l'Application

Double-cliquez sur **text2svg3d** sur votre bureau.

---

### Étape 2 : Entrer le Texte

```
┌─────────────────────────────┐
│ Texte à convertir :         │
│ [LOGO________________]  🔍  │
└─────────────────────────────┘
```

Tapez : **LOGO** (ou n'importe quel texte)

---

### Étape 3 : Activer la Séparation ⭐

```
┌────────────────────────────────────────────────────┐
│ Options de Contour                                 │
├────────────────────────────────────────────────────┤
│ ☐ Générer un fichier de contour séparé            │
│                                                    │
│ ☑ Séparer chaque lettre (un fichier par lettre    │  ← COCHEZ ICI !
│   pour multi-couleur)                              │
└────────────────────────────────────────────────────┘
```

**Cochez** : "Séparer chaque lettre"

---

### Étape 4 : Générer !

Cliquez sur **"Générer le SVG"**

---

### Étape 5 : Vérifier les Fichiers

Allez dans : `/home/seb/Bureau/ready to blender/`

Pour le texte **"LOGO"**, vous verrez :

```
📁 ready to blender/
├── LOGO_lettre_1_L.svg
├── LOGO_lettre_2_O.svg
├── LOGO_lettre_3_G.svg
└── LOGO_lettre_4_O.svg
```

✅ **4 fichiers créés ! Un par lettre !**

---

## 🎨 Importation dans le Slicer

### Configuration Recommandée

#### Pour "LOGO" (4 lettres) :

1. **Ouvrez** votre slicer (PrusaSlicer, Cura, etc.)

2. **Importez la première lettre** :
   - Fichier : `LOGO_lettre_1_L.svg`
   - Couleur : 🔴 **Rouge**
   - Hauteur : 3 mm

3. **Importez la deuxième lettre** :
   - Fichier : `LOGO_lettre_2_O.svg`
   - Couleur : 🟡 **Jaune**
   - Hauteur : 3 mm

4. **Importez la troisième lettre** :
   - Fichier : `LOGO_lettre_3_G.svg`
   - Couleur : 🟢 **Vert**
   - Hauteur : 3 mm

5. **Importez la quatrième lettre** :
   - Fichier : `LOGO_lettre_4_O.svg`
   - Couleur : 🔵 **Bleu**
   - Hauteur : 3 mm

6. **Alignez** toutes les lettres (normalement déjà alignées)

7. **Lancez** l'impression !

---

## 🌈 Résultat Final

```
┌─────────────────────────────────────┐
│                                     │
│    Votre Texte Arc-en-Ciel !        │
│                                     │
│   🔴 🟡 🟢 🔵                        │
│   L  O  G  O                        │
│                                     │
└─────────────────────────────────────┘
```

**Chaque lettre a sa propre couleur ! 🎉**

---

## 💡 Exemples Pratiques

### Exemple 1 : Logo Arc-en-Ciel

**Texte** : `HELLO`

**Configuration** :
```
☑ Séparer chaque lettre
☐ Contour (pas nécessaire)
```

**Résultat** :
```
5 fichiers créés :
- HELLO_lettre_1_H.svg
- HELLO_lettre_2_E.svg
- HELLO_lettre_3_L.svg
- HELLO_lettre_4_L.svg
- HELLO_lettre_5_O.svg
```

**Couleurs suggérées** :
- H → 🔴 Rouge
- E → 🟠 Orange
- L → 🟡 Jaune
- L → 🟢 Vert
- O → 🔵 Bleu

---

### Exemple 2 : Prénom Personnalisé

**Texte** : `JULES`

**Configuration** :
```
☑ Séparer chaque lettre
☐ Contour
Taille : 35 mm
```

**Résultat** :
```
5 fichiers de lettres
```

**Utilisation** :
- Cadeau personnalisé
- Décoration de chambre
- Porte-clés unique

---

### Exemple 3 : Initiales Élégantes

**Texte** : `ABC`

**Configuration** :
```
☑ Séparer chaque lettre
☑ Générer un fichier de contour
Épaisseur contour : 2.0 mm
```

**Résultat** :
```
6 fichiers créés :
- ABC_lettre_1_A.svg
- ABC_lettre_1_A_contour.svg
- ABC_lettre_2_B.svg
- ABC_lettre_2_B_contour.svg
- ABC_lettre_3_C.svg
- ABC_lettre_3_C_contour.svg
```

**Dans le slicer** :
- A (lettre) → Blanc | A (contour) → Noir
- B (lettre) → Blanc | B (contour) → Noir
- C (lettre) → Blanc | C (contour) → Noir

**Résultat** : 3 lettres avec contours, chacune pouvant avoir sa combinaison de couleurs !

---

## 🎨 Idées de Combinaisons de Couleurs

### Arc-en-Ciel Classique 🌈
```
1ère lettre : 🔴 Rouge
2ème lettre : 🟠 Orange
3ème lettre : 🟡 Jaune
4ème lettre : 🟢 Vert
5ème lettre : 🔵 Bleu
6ème lettre : 🟣 Violet
```

### Dégradé Chaud 🔥
```
🔴 Rouge → 🟠 Orange → 🟡 Jaune
```

### Dégradé Froid ❄️
```
🔵 Bleu → 🟢 Cyan → 💚 Vert clair
```

### Alternance Contrastée
```
⚫ Noir → ⚪ Blanc → ⚫ Noir → ⚪ Blanc
```

### Ton sur Ton
```
🟦 Bleu foncé → 🔵 Bleu → 🩵 Bleu clair
```

### Effet Néon
```
💜 Violet → 🩷 Rose → 🟡 Jaune → 🟢 Vert fluo
```

---

## ⚙️ Combinaison avec le Contour

### Option Ultime : Lettres Séparées + Contours

Vous pouvez **combiner** les deux options !

**Configuration** :
```
☑ Séparer chaque lettre
☑ Générer un fichier de contour
Épaisseur contour : 1.5 mm
```

**Pour "LOGO" (4 lettres), vous obtenez** :
```
8 fichiers créés :

Lettres :
- LOGO_lettre_1_L.svg
- LOGO_lettre_2_O.svg
- LOGO_lettre_3_G.svg
- LOGO_lettre_4_O.svg

Contours :
- LOGO_lettre_1_L_contour.svg
- LOGO_lettre_2_O_contour.svg
- LOGO_lettre_3_G_contour.svg
- LOGO_lettre_4_O_contour.svg
```

**Possibilités créatives** :
1. **Lettres multicolores + contours noirs** :
   - L → Rouge + contour noir
   - O → Jaune + contour noir
   - G → Vert + contour noir
   - O → Bleu + contour noir

2. **Lettres blanches + contours colorés** :
   - L → Blanc + contour rouge
   - O → Blanc + contour jaune
   - G → Blanc + contour vert
   - O → Blanc + contour bleu

3. **Chaque lettre avec son duo de couleurs** :
   - L → Rouge + contour orange
   - O → Jaune + contour vert
   - G → Bleu + contour cyan
   - O → Violet + contour rose

**Les possibilités sont infinies ! 🎨**

---

## 📐 Détails Techniques

### Nomenclature des Fichiers

Le format est : `[TEXTE]_lettre_[POSITION]_[CARACTÈRE].svg`

**Exemples** :
- `HELLO_lettre_1_H.svg` → 1ère lettre (H)
- `HELLO_lettre_2_E.svg` → 2ème lettre (E)
- `HELLO_lettre_5_O.svg` → 5ème lettre (O)

### Caractères Spéciaux

Les caractères spéciaux sont transformés pour les noms de fichiers :

| Caractère | Nom dans fichier |
|-----------|------------------|
| espace | `space` |
| ! | `exclamation` |
| ? | `question` |
| . | `period` |
| - | `hyphen` |

**Exemple** :
- Texte : `A B`
- Fichiers : `A_B_lettre_1_A.svg`, `A_B_lettre_2_space.svg`, `A_B_lettre_3_B.svg`

### Dimensions des Fichiers

Chaque fichier SVG a :
- **Largeur** : Largeur de la lettre uniquement
- **Hauteur** : Hauteur totale du texte (constante pour toutes les lettres)

**Exemple pour "LOGO" :**
```
L.svg : 15 mm × 25 mm
O.svg : 20 mm × 25 mm
G.svg : 18 mm × 25 mm
O.svg : 20 mm × 25 mm
```

**Avantage** : Les lettres sont automatiquement aux bonnes positions quand vous les importez dans l'ordre !

### Position et Alignement

Les fichiers contiennent des **métadonnées** pour faciliter l'alignement :

```xml
<!-- Generated by text2svg3d - LETTER 1/4
     Character: "L" | Font: Arial |
     Size: 30mm | Position in word: 1 | X offset: 0.00mm -->
```

Ces informations vous aident à :
- Vérifier que vous importez les lettres dans le bon ordre
- Connaître la position originale dans le mot
- Retrouver facilement quelle lettre correspond à quel fichier

---

## 🚀 Workflow Complet

### Méthode Simple (Lettres Séparées Seulement)

```
1. Ouvrez text2svg3d
         ↓
2. Tapez "LOGO"
         ↓
3. ☑ Cochez "Séparer chaque lettre"
         ↓
4. Cliquez "Générer le SVG"
         ↓
5. 4 fichiers créés
         ↓
6. Ouvrez votre slicer
         ↓
7. Importez lettre_1_L.svg → Rouge
         ↓
8. Importez lettre_2_O.svg → Jaune
         ↓
9. Importez lettre_3_G.svg → Vert
         ↓
10. Importez lettre_4_O.svg → Bleu
         ↓
11. Vérifiez l'alignement
         ↓
12. Lancez l'impression ! 🌈
```

### Méthode Avancée (Lettres + Contours)

```
1. Ouvrez text2svg3d
         ↓
2. Tapez "LOGO"
         ↓
3. ☑ Cochez "Séparer chaque lettre"
         ↓
4. ☑ Cochez "Générer un fichier de contour"
         ↓
5. Réglez épaisseur contour : 2.0 mm
         ↓
6. Cliquez "Générer le SVG"
         ↓
7. 8 fichiers créés (4 lettres + 4 contours)
         ↓
8. Dans le slicer :
   Pour chaque lettre :
   - Importez le contour → Couleur A
   - Importez la lettre → Couleur B
         ↓
9. Exemple pour L :
   - L_contour.svg → Noir
   - L.svg → Rouge
         ↓
10. Répétez pour O, G, O
         ↓
11. Lancez l'impression ! 🎨
```

---

## 💡 Conseils et Astuces

### Astuce 1 : Ordre d'Importation

Importez les lettres **dans l'ordre** (1, 2, 3, 4...) pour qu'elles s'alignent automatiquement.

### Astuce 2 : Test de Couleurs

Avant la grande impression :
1. Générez en petite taille (15 mm)
2. Testez différentes combinaisons de couleurs
3. Imprimez rapidement
4. Choisissez votre préférée
5. Régénérez en grande taille

### Astuce 3 : Changement de Filament

Si vous n'avez qu'un extrudeur :
1. Importez toutes les lettres dans le slicer
2. Réglez des hauteurs différentes pour chaque lettre :
   - L → 0-3 mm (Rouge)
   - O → 3-6 mm (Jaune)
   - G → 6-9 mm (Vert)
   - O → 9-12 mm (Bleu)
3. L'imprimante vous demandera de changer le filament à chaque palier

### Astuce 4 : Impression Séparée

Alternative simple :
1. Imprimez chaque lettre séparément
2. Peignez ou collez-les après
3. Assemblez sur un support

### Astuce 5 : Réutilisation

Gardez vos lettres individuelles ! Vous pouvez :
- Créer de nouveaux mots avec les mêmes lettres
- Mélanger différentes polices
- Faire des anagrammes

---

## 🎯 Cas d'Usage

### 1. Enseignement
**Lettres de l'alphabet séparées** pour apprendre les couleurs et les lettres

### 2. Décoration
**Prénoms colorés** pour chambres d'enfants

### 3. Événements
**HAPPY** en multicolore pour anniversaires

### 4. Entreprise
**Logo** avec identité visuelle multi-couleur

### 5. Cadeaux
**Initiales** personnalisées et colorées

### 6. Art
**Mots artistiques** avec dégradés de couleurs

---

## ❓ FAQ

### Puis-je séparer les lettres ET avoir des contours ?

✅ **Oui !** Cochez les deux options. Vous obtiendrez un fichier de lettre ET un fichier de contour pour chaque lettre.

### Combien de fichiers seront créés ?

- **Lettres seules** : Nombre de lettres dans votre texte
- **Lettres + contours** : Nombre de lettres × 2

**Exemples** :
- "ABC" → 3 lettres → **3 fichiers**
- "ABC" avec contours → **6 fichiers**
- "HELLO" → 5 lettres → **5 fichiers**
- "HELLO" avec contours → **10 fichiers**

### Les lettres s'alignent-elles automatiquement ?

✅ **Oui !** Les positions sont calculées automatiquement. Importez-les dans l'ordre et elles se placeront correctement.

### Puis-je utiliser cette option avec n'importe quelle police ?

✅ **Oui !** Toutes les polices supportées fonctionnent avec cette option.

### Ça marche avec les espaces et la ponctuation ?

✅ **Oui !** Même les espaces et caractères spéciaux auront leur fichier.

**Exemple** : `A B` → 3 fichiers (A, espace, B)

### Comment savoir quelle lettre correspond à quel fichier ?

Le nom de fichier l'indique :
- `LOGO_lettre_1_L.svg` → C'est la lettre **L**
- `LOGO_lettre_2_O.svg` → C'est la lettre **O**

De plus, les métadonnées à l'intérieur du SVG donnent tous les détails !

---

## 🚨 Dépannage

### Trop de fichiers créés !

**Cause** : Vous avez coché "Lettres séparées" + "Contours"

**Solution** :
- Si vous voulez juste les lettres : Décochez "Contours"
- Si vous voulez les deux : C'est normal !

### Les lettres ne s'alignent pas dans le slicer

**Cause** : Importation dans le désordre

**Solution** :
1. Supprimez tous les objets
2. Ré-importez dans l'ordre : lettre_1, lettre_2, lettre_3...
3. Vérifiez les coordonnées X, Y

### Je ne vois pas de différence entre les fichiers

**Cause** : Normal ! Chaque fichier contient UNE lettre

**Solution** :
- Ouvrez chaque SVG individuellement pour vérifier
- Dans le slicer, chaque fichier apparaîtra à sa position

### Un fichier est vide ou manquant

**Cause** : La police ne supporte pas ce caractère

**Solution** :
- Essayez une police différente (ex: DejaVu Sans)
- Vérifiez que le caractère existe dans la police choisie

---

## 📊 Tableau Récapitulatif

| Option | Fichiers Créés | Utilisation |
|--------|----------------|-------------|
| Aucune | 1 fichier | Texte mono-couleur simple |
| Contour seul | 2 fichiers | Texte bi-couleur (texte + contour) |
| Lettres séparées | N fichiers | Chaque lettre une couleur |
| Lettres + Contours | N×2 fichiers | Maximum de créativité ! |

**N** = Nombre de lettres dans votre texte

---

## 🎉 Résumé

**Avec la séparation des lettres :**
- 🌈 **Multi-couleur** : Chaque lettre sa couleur
- 🎨 **Créativité** : Dégradés, arc-en-ciel, contrastes
- 📁 **Organisation** : Fichiers clairement nommés
- 🚀 **Simplicité** : Une case à cocher !
- ⚡ **Rapidité** : Génération automatique
- 🎯 **Précision** : Alignement automatique

**Créez des textes 3D qui sortent vraiment du lot ! 🌈🖨️**

---

## 🔗 Liens Utiles

- **Guide du contour** : [CONTOUR-3D.md](CONTOUR-3D.md)
- **Démarrage rapide** : [QUICK-START-CONTOUR.md](QUICK-START-CONTOUR.md)
- **Interface graphique** : [GUI_GUIDE.md](GUI_GUIDE.md)
- **Index complet** : [INDEX-FONCTIONNALITES.md](INDEX-FONCTIONNALITES.md)

---

**text2svg3d - Des textes 3D aux couleurs de l'arc-en-ciel ! 🌈🎯**
