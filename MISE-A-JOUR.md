# Mise à Jour - Nom de Fichier Automatique

## ✨ Nouvelle Fonctionnalité

Le nom du fichier de sortie est maintenant **automatiquement généré** à partir du texte que vous tapez !

## 🎯 Comment ça marche

### Avant :
- Tous les fichiers s'appelaient `output.svg`
- Il fallait renommer manuellement

### Maintenant :
- **Tapez "HELLO"** → Le fichier s'appelle automatiquement **`HELLO.svg`**
- **Tapez "Mon Logo"** → Le fichier s'appelle **`Mon_Logo.svg`**
- **Tapez "ABC 123"** → Le fichier s'appelle **`ABC_123.svg`**

## 📁 Emplacement

Le fichier est toujours créé dans :
```
/home/seb/Bureau/ready to blender/
```

Mais maintenant avec le nom basé sur votre texte !

## 🔧 Règles de Nommage

Pour éviter les problèmes avec les noms de fichiers :

1. **Espaces** → Remplacés par des **underscores** `_`
   - "Mon Texte" → `Mon_Texte.svg`

2. **Caractères invalides** → Remplacés par `_`
   - Les caractères `< > : " / \ | ? *` ne sont pas autorisés
   - "Texte/Test" → `Texte_Test.svg`

3. **Longueur maximale** → 50 caractères
   - Les noms trop longs sont tronqués

4. **Texte vide** → Utilise `output.svg` par défaut

## 📝 Exemples

| Vous tapez | Nom du fichier |
|------------|----------------|
| `HELLO` | `HELLO.svg` |
| `Mon Logo` | `Mon_Logo.svg` |
| `ABC 123` | `ABC_123.svg` |
| `Texte-Test` | `Texte-Test.svg` |
| `Logo@2024` | `Logo_2024.svg` |
| `Texte/Test` | `Texte_Test.svg` |
| *(vide)* | `output.svg` |

## 🎨 Utilisation

1. **Ouvrez l'application**
2. **Tapez votre texte** : Par exemple "LOGO"
3. **Regardez le champ "Fichier de sortie"** :
   - Il affiche automatiquement : `/home/seb/Bureau/ready to blender/LOGO.svg`
4. **Cliquez "Générer le SVG"**
5. **Le fichier est créé** avec le bon nom !

## 💡 Astuce

Vous pouvez toujours **modifier manuellement** le nom du fichier :
- Cliquez sur "Parcourir..."
- Ou éditez directement le champ "Fichier de sortie"

Le nom se met à jour automatiquement quand vous tapez, mais vous gardez le contrôle !

## ✅ Avantages

- ✅ **Plus besoin de renommer** les fichiers après génération
- ✅ **Organisation facile** : chaque texte a son propre fichier
- ✅ **Pas de confusion** : vous savez directement quel fichier contient quel texte
- ✅ **Gain de temps** : tout est automatique !

## 🚀 Workflow Complet

```
1. Double-clic sur l'icône text2svg3d
         ↓
2. Tapez "LOGO" dans le champ texte
         ↓
3. Le fichier de sortie devient automatiquement :
   /home/seb/Bureau/ready to blender/LOGO.svg
         ↓
4. Choisissez votre police
         ↓
5. Cliquez "Générer le SVG"
         ↓
6. Fichier créé : LOGO.svg dans ready to blender/
         ↓
7. Tapez maintenant "ABC"
         ↓
8. Le fichier de sortie devient automatiquement :
   /home/seb/Bureau/ready to blender/ABC.svg
         ↓
9. Génération → Nouveau fichier ABC.svg créé !
```

---

## 📋 Résumé des Changements

### Interface Complète en Français ✅
- Tous les labels, boutons et messages traduits

### Aperçu Visuel de la Police ✅
- Zone d'aperçu qui montre votre texte avec la police choisie

### Chemin de Sortie Personnalisé ✅
- Dossier par défaut : `~/Bureau/ready to blender/`

### Nom de Fichier Automatique ✅ **NOUVEAU !**
- Le nom est basé sur le texte tapé
- Mise à jour automatique en temps réel

---

**Profitez de cette nouvelle fonctionnalité ! 🎉**
