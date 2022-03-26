import decl
import os

worter = {}


class Wort:
    def __init__(self, kaz: str, deu: list, stransc: str, wortart: str, definition: str, tags: list, inflekativ: str):
        self.kaz = kaz
        self.deu = deu
        self.stransc = stransc
        self.wortart = wortart
        self.definition = definition
        self.tags = tags
        self.inflekativ = inflekativ


def load():
    temp = []
    temp_return = {}
    f = open("liste.kaz", "rb")
    data = f.read().decode("utf-8")
    data = data.split("\n")
    for instance in data:
        if len(instance) > 5:
            print("instance\t", instance)
            print("to exec\t", "temp.append({e})".format(e=instance))
            exec("temp.append({e})".format(e=instance))
            print("Temp:")
            print(temp)
            temp_return[getattr(temp[-1], "kaz")] = temp[-1]
            print(instance)
    f.close()
    return temp_return


# Das überarbeiten
def save():
    f = open("liste.kaz", "w")
    for wr in worter:
        f.write(str(worter[wr]))
        f.write("\n")
    f.close()
            

def add():
    a_tags = []
    a_deu = []
    print("# Add or modify #")
    print("Daten ausfüllen")
    a_kaz = input("Name (Kaseiisch)>\t")
    a_deuraw = input("Deutsche Übersetzungen (mit 'BREAK' fortfahren)>\t")
    a_deu.append(a_deuraw)
    while a_deuraw != 'BREAK':
        a_deuraw = input("Deutsche Übersetzungen (mit 'BREAK' fortfahren)>\t")
        if a_deuraw != 'BREAK':
            a_tags.append(a_deuraw)
    a_stransc = input("Wiss. Transkription>\t")
    a_wortart = input("Wortart>\t")
    a_definition = input("Definition(en)>\t")
    a_tagsraw = input("Tags (mit 'BREAK' fortfahren)>\t")
    a_tags.append(a_tagsraw)
    while a_tagsraw != 'BREAK':
        a_tagsraw = input("Tags (mit 'BREAK' fortfahren)>\t")
        if a_tagsraw != 'BREAK':
            a_tags.append(a_tagsraw)
    a_infl = input("Inflekativ>\t")
    os.system("cls")
    print(f"= Ist das korrekt? =\n{a_kaz}\n{a_stransc}\n{a_wortart}; {a_tags}\n\n{a_deu}\n{a_definition}\n{a_infl}\n\n")
    x = input("Y/n> ")
    if x.upper() == 'Y':
        worter[a_kaz] = Wort(a_kaz, a_deu, a_stransc, a_wortart, a_definition, a_tags, a_infl)
        save()
        os.system("cls")


# Init

#wörter = load()
worter = load()
print(worter)

if __name__ == '__main__':
    os.system("cls")
    while True:
        add()

#Wort('èзyнэнзy', 'subst', ['Monster'], 'Räumlichkeit, in der ein Handelsunternehmen, ein gewerbliches Unternehmen Waren ausstelt und zum Verkauf anbietet', ['P1'], 'èзyн')
#Wort('èзyнÿтно', 'verb', ['kaufen'], 'etwas gegen Bezahlung erwerben', ['Q1'], 'èзyн')
#Wort('èзyнλи', ['käuflich', 'bestechlich'], '[1] gegen Geld erhältlich;\n[2] bestechlich', ['R1'], 'èзyн')
#Wort('монэнзy', 'subst', ['Monster'], 'furchterregendes, hässliches Fabelwesen, Ungeheuer von fantastischer, meist riesenhafter Gestalt', ['P2'], 'мон')
#Wort('монÿтно', 'verb', ['etwas fürchten'], '[1] vor jemandem, etwas Angst haben;\n[2] Unangenehmes ahnen, befürchten;\n[3] Furcht empfinden, Angst haben', ['Q2'], 'мон')
#Wort('монλи', 'adj', ['gruselig'], 'sich vor etwas Unheimlichem, Makabrem o. Ä. fürchten; Grausen, Furcht empfinden', ['R3'], 'мон')
