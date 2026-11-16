import collections

# Pra cada símbolo, existem 13 cartas
# Símbolo = naipe

carta = collections.namedtuple("Carta", ["rank", "naipe"])


class Deck:
    rank = [number for number in range(1, 11)] + list("JQK")
    naipe = "Paus,", "Ouros,", "Copas,", ["Espadas"]

    def __init__(self):
        self._cards = [carta(rank, naipe) for rank in self.rank for naipe in self.naipe]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


baralho_1 = Deck()

print(len(baralho_1))
print(baralho_1[15])
