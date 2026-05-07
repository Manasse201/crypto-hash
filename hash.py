def mb64_hash(message):
    h = (77 << 56) | (66 << 48) | 0xABCDEF123456
    MASK_64 = 0xFFFFFFFFFFFFFFFF
    PRIME = 0x100000001B3
    
    for char in message:
        val = ord(char)

        h ^= val
        h = (h * PRIME) & MASK_64
        h = ((h << 13) | (h >> 51)) & MASK_64
        h = (h + (val << 5)) & MASK_64

    h ^= (h >> 33)
    h = (h * 0xFF51AFD7ED558CCD) & MASK_64
    h ^= (h >> 33)

    return h

entree = "MANASSE"
resultat_decimal = mb64_hash(entree)
resultat_hex = hex(resultat_decimal)

print(f"Message : {entree}")
print(f"Hash (Décimal) : {resultat_decimal}")
print(f"Hash (Hexa 64-bit): {resultat_hex}")
print(f"Nombre de bits : {resultat_decimal.bit_length()} bits")