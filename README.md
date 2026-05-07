# mb64_hash — Lecture et utilisation

Ce dépôt contient une petite implémentation d'une fonction de hachage 64 bits dans `hash.py` nommée `mb64_hash`.

Description de l'algorithme
- Initialisation : la variable `h` est initialisée avec les octets `M` et `B` (via `77 << 56` et `66 << 48`) et une constante `0xABCDEF123456`.
- Boucle principale : pour chaque caractère du message on :
  1. récupère sa valeur Unicode (`val = ord(char)`),
  2. applique un XOR : `h ^= val`,
  3. multiplie par la constante `PRIME = 0x100000001B3` (primitif inspiré du FNV),
  4. effectue une rotation gauche de 13 bits sur les 64 bits,
  5. ajoute `val << 5` au haché.
- Finalisation (avalanche) : on applique une séquence de mélange similaire au finalizer de MurmurHash3 :
  - `h ^= (h >> 33)`,
  - `h = h * 0xFF51AFD7ED558CCD` (mod 2^64),
  - `h ^= (h >> 33)`.

Propriétés et usages
- Taille : produit un entier 64 bits (valeur Python entière limitée uniquement par l'implantation, mais restreinte par masque 64 bits dans la fonction).
- Non cryptographique : ce n'est PAS un algorithme sécurisé pour la cryptographie. Utilisez-le pour des usages comme tables de hachage, checksums légers, ou déduplication, mais pas pour la sécurité.
- Collisions : comme tout hachage 64 bits, des collisions existent (pigeonhole). Ne pas l'utiliser là où l'unicité garantie est requise.

Exemple
- Exécuter :

```powershell
python hash.py
```

- `hash.py` affiche le message testé (`MANASSE` par défaut), la valeur décimale et la valeur hexadécimale 64-bit du haché.

Modifications
- Le code source principal se trouve dans `hash.py`.
