import decl

wörter = {}

class Wort:
    def __init__(self, kaz: str, ipa: str, deu: list, wortart: str, definition: str, tags: list, inflekativ: str):
        self.kaz = kaz
        self.deu = deu
        self.ipa = ipa
        self.wortart = wortart
        self.definition = definition
        self.tags = tags
        self.inflekativ = inflekativ

def load():
    tmp_return = {}
    f = open("liste.kaz", "r")
    data = f.read().split("\n")
    f.close()
    print(f"Inital\t{data}")
    for word in range(len(data)):
        tmp_return[getattr(data[word], 'kaz')] = data[word]
    print(tmp_return)
            

# Init

#wörter = load()
load()

#Wort('èзyнэнзy', '[ɛzuːnənzu]', 'subst', ['Monster'], 'Räumlichkeit, in der ein Handelsunternehmen, ein gewerbliches Unternehmen Waren ausstelt und zum Verkauf anbietet', ['P1'], 'èзyн')
#Wort('èзyнÿтно', '[ɛzuːnytnɔ]', 'verb', ['kaufen'], 'etwas gegen Bezahlung erwerben', ['Q1'], 'èзyн')
#Wort('èзyнλи', '[ɛzuːnli]', 'adj', ['käuflich', 'bestechlich'], '[1] gegen Geld erhältlich;\n[2] bestechlich', ['R1'], 'èзyн')
#Wort('монэнзy', '[ˈmɔnˌənzu]', 'subst', ['Monster'], 'furchterregendes, hässliches Fabelwesen, Ungeheuer von fantastischer, meist riesenhafter Gestalt', ['P2'], 'мон')
#Wort('монÿтно', '[ˈmɔnˌytnɔ]', 'verb', ['etwas fürchten'], '[1] vor jemandem, etwas Angst haben;\n[2] Unangenehmes ahnen, befürchten;\n[3] Furcht empfinden, Angst haben', ['Q2'], 'мон')
#Wort('монλи', '[ˈmɔnˌli]', 'adj', ['gruselig'], 'sich vor etwas Unheimlichem, Makabrem o. Ä. fürchten; Grausen, Furcht empfinden', ['R3'], 'мон')
