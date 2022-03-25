import decl

worter = {}


class Wort:
    def __init__(self, kaz: str, deu: list, wortart: str, definition: str, tags: list, inflekativ: str):
        self.kaz = kaz
        self.deu = deu
        self.wortart = wortart
        self.definition = definition
        self.tags = tags
        self.inflekativ = inflekativ


def load():
    tmp_return = {}
    with open("liste.kaz", "r") as f:
        data = f.read()
        data = data.split("\n")
        print(f"Inital\t{data}")
        for word in range(len(data)):
            tmp_return[getattr(data[word], 'kaz')] = data[word]
        print(tmp_return)
            

# Init

#wörter = load()
load()

#Wort('èзyнэнзy', 'subst', ['Monster'], 'Räumlichkeit, in der ein Handelsunternehmen, ein gewerbliches Unternehmen Waren ausstelt und zum Verkauf anbietet', ['P1'], 'èзyн')
#Wort('èзyнÿтно', 'verb', ['kaufen'], 'etwas gegen Bezahlung erwerben', ['Q1'], 'èзyн')
#Wort('èзyнλи', ['käuflich', 'bestechlich'], '[1] gegen Geld erhältlich;\n[2] bestechlich', ['R1'], 'èзyн')
#Wort('монэнзy', 'subst', ['Monster'], 'furchterregendes, hässliches Fabelwesen, Ungeheuer von fantastischer, meist riesenhafter Gestalt', ['P2'], 'мон')
#Wort('монÿтно', 'verb', ['etwas fürchten'], '[1] vor jemandem, etwas Angst haben;\n[2] Unangenehmes ahnen, befürchten;\n[3] Furcht empfinden, Angst haben', ['Q2'], 'мон')
#Wort('монλи', 'adj', ['gruselig'], 'sich vor etwas Unheimlichem, Makabrem o. Ä. fürchten; Grausen, Furcht empfinden', ['R3'], 'мон')
