import decl
import os


class Wort:
    def __init__(self, kaz: str, stransc: str, wortart: str, deu: list, definition: str, tags: list, inflekativ: str):
        self.kaz = kaz
        self.deu = deu
        self.stransc = stransc
        self.wortart = wortart
        self.definition = definition
        self.tags = tags
        self.inflekativ = inflekativ

    def __str__(self):
        return f"Wort('{self.kaz}', '{self.stransc}', '{self.wortart}', {self.deu}, '{self.definition}', {self.tags}, '{self.inflekativ}')"

    def wortart_format(self):
        if self.wortart == 'subst':
            return 'Substantiv'
        elif self.wortart == 'verb':
            return 'Verb'
        elif self.wortart == 'adj':
            return 'Adjektiv'

    def fullformat(self):
        trans = str(self.deu)
        trans = trans.strip("[")
        trans = trans.strip("]")
        return f"{self.kaz}\n{self.stransc}\n{self.wortart_format()}\nvon {self.inflekativ}\n\n{trans}\n{self.definition}"


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


def save():
    f = open("liste.kaz", "wb")
    for wr in worter:
        f.write(str(worter[wr]).encode("utf8"))
        f.write(b"\n")
    f.close()


worter = load()
print(worter)
            

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
            a_deu.append(a_deuraw)
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
    print(f"= Ist das korrekt? =\n{a_kaz}\n{a_stransc}\n{a_wortart}; {a_tags}\n\n{a_deu}\n{a_definition}\n{a_infl}\n\n{worter}\n\n")
    x = input("Y/n> ")
    if x.upper() == 'Y':
        worter[a_kaz] = Wort(a_kaz, a_stransc, a_wortart, a_deu, a_definition, a_tags, a_infl)
        save()
        os.system("cls")


def search(inp):
    e_wortart = ''
    e_genusverbi = ''
    e_fall = ''
    e_numerus = ''
    e_tempus = ''
    inflekativ = ''
    # Ermitteln des Inflekativs/Wortstammes
    # Substantive
    if inp[-4:] == 'энзy':
        e_wortart = 'subst'
        e_fall = 'Nominativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-4]
    elif inp[-4:] == 'энио':
        e_wortart = 'subst'
        e_fall = 'Akkusativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-4]
    elif inp[-7:] == 'эногōрт':
        e_wortart = 'subst'
        e_fall = 'Lokativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-7]
    elif inp[-8:] == 'эногōиаλ':
        e_wortart = 'subst'
        e_fall = 'Orginativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-8]
    elif inp[-8:] == 'эногōиоλ':
        e_wortart = 'subst'
        e_fall = 'Direktativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-8]
    elif inp[-7:] == 'эногōба':
        e_wortart = 'subst'
        e_fall = 'Instrumentativ'
        e_numerus = 'Singular'
        inflekativ = inp[:-7]
    elif inp[-7:] == 'эногōрy':
        e_wortart = 'subst'
        e_fall = 'Possessiv'
        e_numerus = 'Singular'
        inflekativ = inp[:-7]
    elif inp[-7:] == 'эногōга':
        e_wortart = 'subst'
        e_fall = 'Totalitiv'
        e_numerus = 'Singular'
        inflekativ = inp[:-7]
    elif inp[-4:] == 'казy':
        e_wortart = 'subst'
        e_fall = 'Nominativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-4]
    elif inp[-4:] == 'каио':
        e_wortart = 'subst'
        e_fall = 'Akkusativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-4]
    elif inp[-7:] == 'каогōрт':
        e_wortart = 'subst'
        e_fall = 'Lokativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-7]
    elif inp[-8:] == 'каогōиаλ':
        e_wortart = 'subst'
        e_fall = 'Orginativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-8]
    elif inp[-8:] == 'каогōиоλ':
        e_wortart = 'subst'
        e_fall = 'Direktativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-8]
    elif inp[-7:] == 'каогōба':
        e_wortart = 'subst'
        e_fall = 'Instrumentativ'
        e_numerus = 'Plural'
        inflekativ = inp[:-7]
    elif inp[-7:] == 'каогōрy':
        e_wortart = 'subst'
        e_fall = 'Possessiv'
        e_numerus = 'Plural'
        inflekativ = inp[:-7]
    elif inp[-7:] == 'каогōга':
        e_wortart = 'subst'
        e_fall = 'Totalitiv'
        e_numerus = 'Plural'
        inflekativ = inp[:-7]
    # Verben
    elif inp[-4:] == 'ÿтно':
        e_wortart = 'verb'
        e_genusverbi = 'Aktiv'
        e_tempus = 'Präsens'
        inflekativ = inp[:-4]
    elif inp[-4:] == 'ÿтйе':
        e_wortart = 'verb'
        e_genusverbi = 'Aktiv'
        e_tempus = 'Vergangenheit'
        inflekativ = inp[:-4]
    elif inp[-5:] == 'ÿтшλи':
        e_wortart = 'verb'
        e_genusverbi = 'Aktiv'
        e_tempus = 'Zukunft'
        inflekativ = inp[:-5]
    elif inp[-4:] == 'евно':
        e_wortart = 'verb'
        e_genusverbi = 'Passiv'
        e_tempus = 'Präsens'
        inflekativ = inp[:-4]
    elif inp[-4:] == 'евйе':
        e_wortart = 'verb'
        e_genusverbi = 'Passiv'
        e_tempus = 'Vergangenheit'
        inflekativ = inp[:-4]
    elif inp[-5:] == 'евшλи':
        e_wortart = 'verb'
        e_genusverbi = 'Passiv'
        e_tempus = 'Zukunft'
        inflekativ = inp[:-5]

    form = ""
    if e_wortart == 'subst':
        form = f"{e_fall} {e_numerus}"
    elif e_wortart == 'verb':
        form = f"{e_tempus} {e_genusverbi}"

    infls = []
    fin = ""
    for wr in worter:
        if worter[wr].inflekativ == inflekativ:
            infls.append(wr)

    for il in infls:
        if worter[il].wortart == e_wortart:
            fin = worter[il]

    print(f"{inp} ist {form} von:\n")
    return fin.fullformat()


# Init

#wörter = load()

if __name__ == '__main__':
    os.system("cls")
    while True:
        add()


