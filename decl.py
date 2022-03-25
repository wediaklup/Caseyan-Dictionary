import logging

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


dictionary = {}


def dekl(mode, inflekativ, arg1="0", arg2="0", arg3="0"):
    if mode == "subst":
        # arg1 = Kasus
        # arg2 = Numerus
        if arg1 == "0" and arg2 == "0":
            result = Kasus.sg.dekl(inflekativ)
            tmp = Kasus.pl.dekl(inflekativ)
            for i in range(len(tmp)):
                result.append(tmp[i])
            return result
        elif arg1 == "0" or arg2 == "0":
            logging.warning("Deklinieren: Unzureichende Parameter")
        else:
            pass


def fullformat(mode, liste):
    if mode == "subst":
        resultsg = f"Singular\nNominativ: {liste[0]}\nAkkusativ: {liste[1]}\nLokativ: {liste[2]}\nOrginativ: {liste[3]}\nDirektativ: {liste[4]}\nInstrumentativ: {liste[5]}\nPossessiv: {liste[6]}\nTotalitiv: {liste[7]}\n\n"
        resultpl = f"Plural\nNominativ: {liste[8]}\nAkkusativ: {liste[9]}\nLokativ: {liste[10]}\nOrginativ: {liste[11]}\nDirektativ: {liste[12]}\nInstrumentativ: {liste[13]}\nPossessiv: {liste[14]}\nTotalitiv: {liste[15]}"
        return (resultsg + resultpl)


class Kasus:
    class sg:
        nom = "энзу"
        akk = "энио"
        lok = "эногōрт"
        org = "эногōиаλ"
        dir = "эногōиоλ"
        ins = "эногōба"
        pos = "эногōрy"
        tot = "эногōга"

        @staticmethod
        def dekl(wort):
            res = [wort + Kasus.sg.nom,
                   wort + Kasus.sg.akk,
                   wort + Kasus.sg.lok,
                   wort + Kasus.sg.org,
                   wort + Kasus.sg.dir,
                   wort + Kasus.sg.ins,
                   wort + Kasus.sg.pos,
                   wort + Kasus.sg.tot]
            return res

    class pl:
        nom = "казу"
        akk = "каио"
        lok = "каогōрт"
        org = "каогōиаλ"
        dir = "каогōиоλ"
        ins = "каогōба"
        pos = "каогōрy"
        tot = "каогōга"

        @staticmethod
        def dekl(wort):
            res = [wort + Kasus.pl.nom,
                   wort + Kasus.pl.akk,
                   wort + Kasus.pl.lok,
                   wort + Kasus.pl.org,
                   wort + Kasus.pl.dir,
                   wort + Kasus.pl.ins,
                   wort + Kasus.pl.pos,
                   wort + Kasus.pl.tot]
            return res


class Wort:
    def __init__(self, wort, wortart):
        pass


class Substantiv:
    def __init__(self, inflekativ, wortart, ipa, definition, deklination):
        pass


def load():
    """with open("liste.kaz", "r") as f:
        for lines in f:
            pass"""
    f = open("liste.kaz", "r")
    data = f.read()
    f.close()
    data = data.split("\n")
    return data

if __name__ == '__main__':
    while True:
        wrt = input("Zu deklinieren> ")
        print(fullformat("subst", dekl("subst", wrt)) + "\n")