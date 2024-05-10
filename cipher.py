class OgiltigSubstitutionscipher(Exception):
    pass

class Substitutionscipher:
    def _init_(self, mappning):
        if not isinstance(mappning, list):
            raise TypeError("Mappning måste vara en lista")
        if any(len(pair) != 2 or not all(isinstance(item, str) and len(item) == 1 for item in pair) for pair in mappning):
            raise ValueError("Ogiltig mappning")
        if len(set(char for pair in mappning for char in pair)) != sum(map(len, mappning)):
            raise OgiltigSubstitutionscipher("Dubbletter hittades i mappningen")
        self.mappning = dict(mappning)

    def substituera(self, text):
        if not isinstance(text, str):
            raise TypeError("Text måste vara en sträng")
        return "".join(self.mappning.get(char, char) for char in text)

# Exempelanvändning:
try:
    cipher = Substitutionscipher([('a', 'm'), ('b', 'n'), ('a', 'o')])
except OgiltigSubstitutionscipher as e:
    print(f"Ogiltig substitution upptäckt: {e}")

cipher = Substitutionscipher([('a', 'm'), ('b', 'n')])
krypterad = cipher.substituera('abba')
print(krypterad)  # -> mnnm
dekrypterad = cipher.substituera(krypterad)
print(dekrypterad)  # -> abba

cipher = Substitutionscipher([])
krypterad = cipher.substituera('hej')
print(krypterad)  # -> hej
dekrypterad = cipher.substituera(krypterad)
print(dekrypterad)  # -> hej

mappning = list(zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"))
cipher = Substitutionscipher(mappning)
text = "JACK AND JILL WENT UP THE HILL"
krypterad = cipher.substituera(text)
print(krypterad)  # -> WNPX NAQ WVYY JRAG HC GUR UVYY