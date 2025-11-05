# Démarrage Rapide - Contour Multi-Couleur

## 🚀 En 3 Minutes : Votre Premier Texte Multi-Couleur

---

## 📋 Ce dont vous avez besoin

- ✅ text2svg3d installé
- ✅ Une imprimante 3D multi-matériaux OU possibilité de changer de filament
- ✅ 2 couleurs de filament

---

## 🎯 Objectif

Créer ce résultat :

```
┌────────────────────────────────┐
│                                │
│   ╔══════╗                     │
│   ║ LOGO ║  ← Texte noir       │
│   ╚══════╝  ← Contour blanc    │
│                                │
└────────────────────────────────┘
```

---

## 🔢 Étapes Simples

### Étape 1 : Ouvrir l'Application (5 secondes)

Double-cliquez sur l'icône **text2svg3d** sur votre bureau.

---

### Étape 2 : Entrer le Texte (10 secondes)

```
┌─────────────────────────────┐
│ Texte à convertir :         │
│ [LOGO________________]  🔍  │
└─────────────────────────────┘
```

Tapez : **LOGO**

---

### Étape 3 : Choisir la Police (10 secondes)

```
┌─────────────────────────────┐
│ Police :                    │
│ [Arial____________] ▼       │
└─────────────────────────────┘
```

Choisissez : **Arial** (ou celle que vous voulez)

---

### Étape 4 : Régler la Taille (15 secondes)

```
┌─────────────────────────────┐
│ Taille (mm) :               │
│ [=======o========] [30.0]   │
└─────────────────────────────┘
```

Ajustez : **30 mm** (ou tapez directement dans le champ)

---

### Étape 5 : Activer le Contour ⭐ (10 secondes)

```
┌────────────────────────────────────┐
│ Options de Contour                 │
├────────────────────────────────────┤
│ ☑ Générer un fichier de contour   │  ← COCHEZ ICI !
│   séparé                           │
│                                    │
│ Épaisseur du contour (mm) :       │
│ [===o=============] [2.0]          │
└────────────────────────────────────┘
```

1. **Cochez** la case
2. **Réglez** l'épaisseur à **2.0 mm**

---

### Étape 6 : Générer ! (5 secondes)

Cliquez sur :

```
┌──────────────────────┐
│   Générer le SVG     │
└──────────────────────┘
```

---

### Étape 7 : Vérifier les Fichiers (10 secondes)

Allez dans : `/home/seb/Bureau/ready to blender/`

Vous devez voir :

```
📁 ready to blender/
   📄 LOGO.svg           ← Texte principal
   📄 LOGO_contour.svg   ← Contour
```

✅ **Deux fichiers créés avec succès !**

---

## 🎨 Impression 3D (Dans votre Slicer)

### Étape 8 : Importer le Contour

1. Ouvrez votre slicer (PrusaSlicer, Cura, etc.)
2. **Importez** `LOGO_contour.svg`
3. Configurez :
   - Hauteur : **0.4 mm** (2 couches)
   - Filament : **Blanc** (ou couleur 1)

---

### Étape 9 : Importer le Texte

1. **Importez** `LOGO.svg`
2. Configurez :
   - Hauteur : **0.4 mm** (2 couches)
   - Filament : **Noir** (ou couleur 2)
3. **Alignez** avec le contour (normalement automatique)

---

### Étape 10 : Lancer l'Impression

1. **Slicez** le projet
2. **Vérifiez** l'aperçu des couches
3. **Lancez** l'impression !

---

## ✅ Résultat Final

```
┌─────────────────────────────────────┐
│                                     │
│    Votre Texte Multi-Couleur !      │
│                                     │
│   ╔════════════╗                    │
│   ║  L O G O   ║                    │
│   ╚════════════╝                    │
│    ↑          ↑                     │
│  Blanc      Noir                    │
│                                     │
└─────────────────────────────────────┘
```

**Félicitations ! 🎉**

---

## 💡 Conseils Rapides

### Pour un Meilleur Contraste

| Texte | Contour | Effet |
|-------|---------|-------|
| Noir | Blanc | ⭐⭐⭐⭐⭐ Parfait |
| Blanc | Noir | ⭐⭐⭐⭐⭐ Parfait |
| Rouge | Blanc | ⭐⭐⭐⭐ Très bien |
| Bleu | Jaune | ⭐⭐⭐⭐ Très bien |
| Bleu foncé | Bleu clair | ⭐⭐⭐ Bien |

### Épaisseur Recommandée

| Taille texte | Épaisseur contour |
|--------------|-------------------|
| 10-20 mm | 0.5-1.0 mm |
| 20-40 mm | 1.0-2.0 mm |
| 40-60 mm | 2.0-3.0 mm |
| 60+ mm | 3.0-5.0 mm |

---

## 🔄 Alternatives Rapides

### Option 1 : Changement de Filament Manuel

Si vous n'avez qu'un extrudeur :

1. **Imprimez** le contour en blanc
2. **Pausez** l'imprimante
3. **Changez** le filament pour noir
4. **Relancez** l'impression
5. **Imprimez** le texte

### Option 2 : Deux Impressions Séparées

1. **Imprimez** le contour (blanc)
2. Laissez refroidir
3. **Imprimez** le texte (noir) par dessus
4. **Collez** avec de la colle chaude si nécessaire

---

## 🚨 Dépannage Express

### Le contour ne s'affiche pas ?

✅ **Vérifiez** que vous avez coché la case dans l'interface

### Les deux fichiers ne s'alignent pas ?

✅ **Importez** d'abord le contour, puis le texte
✅ **Vérifiez** que les coordonnées X, Y sont identiques

### Le contour est trop épais ?

✅ **Régénérez** avec une épaisseur plus faible (ex: 1.0 mm)

### Je ne vois qu'une couleur ?

✅ **Vérifiez** que vous avez bien importé les DEUX fichiers
✅ **Vérifiez** que vous avez assigné des couleurs différentes

---

## 📊 Temps Total

| Étape | Durée |
|-------|-------|
| Configuration dans text2svg3d | 1 min |
| Génération des fichiers | 5 sec |
| Import dans le slicer | 2 min |
| Slicing | 30 sec |
| **Total avant impression** | **~4 min** |
| Impression (varie selon taille) | 10-30 min |

**Temps total de l'idée au résultat : ~15-35 minutes !**

---

## 🎓 Et Après ?

Maintenant que vous maîtrisez la base :

### Pour aller plus loin :

📖 **[CONTOUR-3D.md](CONTOUR-3D.md)**
- Guide complet
- Exemples avancés
- Combinaisons de couleurs
- Astuces pro

📖 **[INDEX-FONCTIONNALITES.md](INDEX-FONCTIONNALITES.md)**
- Toutes les fonctionnalités
- Documentation complète

---

## 🎨 Projets Inspirants

### Facile
- **Badge nominatif** : Nom + cadre
- **Porte-clés** : Initiales en relief
- **Étiquette** : Nom de tiroir/boîte

### Moyen
- **Logo d'entreprise** : Avec contour épais
- **Plaque de porte** : Texte + bordure
- **Magnet frigo** : Message personnalisé

### Avancé
- **Enseigne lumineuse** : Grande taille
- **Lettres 3D décoratives** : Pour mur
- **Cadeau personnalisé** : Prénom artistique

---

## 🏁 Checklist Finale

Avant de lancer votre première impression :

- [ ] Deux fichiers SVG générés (texte + contour)
- [ ] Fichiers importés dans le slicer
- [ ] Couleurs différentes assignées
- [ ] Fichiers alignés correctement
- [ ] Hauteur configurée (0.2-0.4 mm recommandé)
- [ ] Aperçu vérifié dans le slicer
- [ ] Plateau d'impression propre
- [ ] Filaments chargés et prêts

**Tout est OK ? Lancez l'impression ! 🚀**

---

## 🎉 Félicitations !

Vous savez maintenant créer des textes 3D multi-couleur en quelques minutes !

**Amusez-vous bien avec text2svg3d ! 🎨🖨️**

---

## 🔗 Liens Utiles

- **Documentation complète** : [CONTOUR-3D.md](CONTOUR-3D.md)
- **Interface graphique** : [GUI_GUIDE.md](GUI_GUIDE.md)
- **Saisie manuelle** : [SAISIE-MANUELLE.md](SAISIE-MANUELLE.md)
- **Index complet** : [INDEX-FONCTIONNALITES.md](INDEX-FONCTIONNALITES.md)

---

**text2svg3d - Des textes 3D colorés en quelques clics ! 🎯**
