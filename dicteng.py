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


# Init

#wörter = load()
worter = load()
print(worter)

if __name__ == '__main__':
    os.system("cls")
    while True:
        add()
