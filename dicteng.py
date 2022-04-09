from click import pass_context
import decl
import os
from colorama import init, Fore as F, Back as B, Style as S
import gspread

sa = gspread.service_account()
sh = sa.open("кăзèйски езык API Access 2022-04-08")

wks = sh.worksheet("Grammatik")

DEBUG = False
init()


def lst_to_str(lst, join=' '):
    result = join.join(lst)
    return result


def error_msg(exception, title=""):
    print(f"{B.RED}{F.BLACK} == ERROR {title.upper()} == {S.RESET_ALL}\n{F.LIGHTRED_EX}{exception}{S.RESET_ALL}\n")


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
        elif self.wortart == 'pron':
            return 'Pronomen'
        elif self.wortart == 'conj':
            return 'Konjunktion'
        elif self.wortart == 'adv':
            return 'Adverb'
        elif self.wortart == 'prepo':
            return 'Präposition'

    def fullformat(self):
        trans = lst_to_str(self.deu, ", ")
        if self.wortart == 'subst' or self.wortart == 'verb' or self.wortart == 'adj' or self.wortart == 'pron':
            return f" {F.LIGHTGREEN_EX}{self.kaz}\n {self.stransc}{S.RESET_ALL}\n {self.wortart_format()}\n {F.LIGHTBLUE_EX}von {self.inflekativ}{S.RESET_ALL}\n\n{trans}\n{self.definition}"
        else:
            return f" {F.LIGHTGREEN_EX}{self.kaz}\n {self.stransc}{S.RESET_ALL}\n {self.wortart_format()}\n\n{trans}\n{self.definition}"

    def rowformat(self):
        trans = lst_to_str(self.deu, ", ")
        if self.wortart == 'subst' or self.wortart == 'verb' or self.wortart == 'adj' or self.wortart == 'pron':
            return f" {F.LIGHTGREEN_EX}{self.kaz}{S.RESET_ALL} ({F.LIGHTGREEN_EX}{self.stransc}{S.RESET_ALL}, {self.wortart_format()}): {trans} {F.LIGHTBLACK_EX}<- {self.inflekativ}{S.RESET_ALL}"
        else:
            return f" {F.LIGHTGREEN_EX}{self.kaz}{S.RESET_ALL} ({F.LIGHTGREEN_EX}{self.stransc}{S.RESET_ALL}, {self.wortart_format()}): {trans}"


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

with open("debug.ini", "r") as dbg:
    try:
        DEBUG = dbg.read()
    except Exception as e:
        with open("errors.log", "w") as er:
            er.write(f"Couldn't read debug.ini: {e}")


def add():
    os.system("cls")
    a_tags = []
    a_deu = []
    print("# Add or modify #")
    print("Daten ausfüllen")
    a_kaz = input("Name (Kaseiisch)>\t\t\t\t\t")
    a_deuraw = input("Deutsche Übersetzungen (mit 'BREAK' fortfahren)>\t")
    a_deu.append(a_deuraw)
    while a_deuraw != 'BREAK':
        a_deuraw = input("Deutsche Übersetzungen (mit 'BREAK' fortfahren)>\t")
        if a_deuraw != 'BREAK':
            a_deu.append(a_deuraw)
    a_stransc = input("Wiss. Transkription>\t\t\t\t\t")
    a_wortart = input("Wortart>\t\t\t\t\t\t")
    a_definition = input("Definition(en)>\t\t\t\t\t\t")
    a_tagsraw = input("Tags (mit 'BREAK' fortfahren)>\t\t\t\t")
    a_tags.append(a_tagsraw)
    while a_tagsraw != 'BREAK':
        a_tagsraw = input("Tags (mit 'BREAK' fortfahren)>\t\t\t\t")
        if a_tagsraw != 'BREAK':
            a_tags.append(a_tagsraw)
    a_infl = input("Inflekativ>\t\t\t\t\t\t")
    os.system("cls")
    print(
        f"= Ist das korrekt? =\n{a_kaz}\n{a_stransc}\n{a_wortart}; {a_tags}\n\n{a_deu}\n{a_definition}\n{a_infl}\n\n{worter}\n\n")
    x = input("Y/n> ")
    if x.upper() == 'Y':
        worter[a_kaz] = Wort(a_kaz, a_stransc, a_wortart, a_deu, a_definition, a_tags, a_infl)
        save()
        os.system("cls")


def spread():
    # Wort = A
    # NomenBedeutung = C
    # VerbBedeutung = D
    # AdflekativBedeutung = E

    def tostring(lst: list):
        # Converts Google Spreadsheet Cell to str
        tmp = lst[0]
        result = ''.join(tmp)
        return result

    # Getting user values
    os.system("cls")
    start = input("Import starting from Row No. ")
    end = input("Import stopping at Row No. ")
    row_nav = int(start)

    # Creating the word list
    for i in range(int(end) - int(start)):
        try:
            wort = tostring(wks.get(f"A{row_nav}"))
        except Exception as e:
            error_msg(e, "getting word")

        try:
            de_n = tostring(wks.get(f"C{row_nav}"))
        except IndexError:
            de_n = None
        except Exception as e:
            error_msg(e, "getting nominal meaning")

        try:
            de_v = tostring(wks.get(f"D{row_nav}"))
        except IndexError:
            de_v = None
        except Exception as e:
            error_msg(e, "getting verbal meaning")

        try:
            de_a = tostring(wks.get(f"E{row_nav}"))
        except IndexError:
            de_a = None
        except Exception as e:
            error_msg(e, "getting adjectival meaning")

        try:
            voclist = [wort, de_n, de_v, de_a]
            print(voclist)
        except Exception as e:
            error_msg(e)


        formlist = decl.process_infl(wort)
        if de_n != None:
            worter[formlist[0]] = Wort(formlist[0], "SCTRANS", "subst", [de_n], "coming soon", [], wort)
        if de_v != None:
            worter[formlist[1]] = Wort(formlist[1], "SCTRANS", "verb", [de_v], "coming soon", [], wort)
        if de_a != None:
            worter[formlist[2]] = Wort(formlist[2], "SCTRANS", "adj", [de_a], "coming soon", [], wort)
        save()

        row_nav += 1

    input()


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
    # Adjektive
    elif inp[-2:] == 'λи':
        e_wortart = 'adj'
        e_fall = 'Infinitiv'
        inflekativ = inp[:-2]
    elif inp[-2:] == 'зă':
        e_wortart = 'adj'
        e_fall = 'Nominativ'
        inflekativ = inp[:-2]
    elif inp[-2:] == 'их':
        e_wortart = 'adj'
        e_fall = 'Akkusativ'
        inflekativ = inp[:-2]
    elif inp[-4:] == 'ōера':
        e_wortart = 'adj'
        e_fall = 'Lokativ'
        inflekativ = inp[:-4]
    elif inp[-5:] == 'ōеаиа':
        e_wortart = 'adj'
        e_fall = 'Orginativ'
        inflekativ = inp[:-5]
    elif inp[-5:] == 'ōеōиō':
        e_wortart = 'adj'
        e_fall = 'Direktativ'
        inflekativ = inp[:-5]
    elif inp[-4:] == 'ōебö':
        e_wortart = 'adj'
        e_fall = 'Instrumentativ'
        inflekativ = inp[:-4]
    else:
        inflekativ = 'N/A'

    form = ""
    if e_wortart == 'subst':
        form = f"{e_fall} {e_numerus}"
    elif e_wortart == 'verb':
        form = f"{e_tempus} {e_genusverbi}"
    elif e_wortart == 'adj':
        form = f"{e_fall}"

    infls = []
    fin = ""
    for wr in worter:
        if worter[wr].wortart == e_wortart or 'pron' or 'conj' or 'adv':
            if worter[wr].inflekativ == inflekativ:
                infls.append(wr)
        else:
            if wr == inp:
                infls.append(wr)

    print(infls)

    for il in infls:
        if worter[il].wortart == e_wortart or worter[il].wortart == 'pron':
            fin = worter[il]
            print(f"{worter[il].wortart} == {e_wortart} oder 'pron'")
        elif il == inp:
            print(f"{il} == {inp}")
            fin = worter[il]

    print(fin)

    if DEBUG == 'False':
        os.system("cls")

    if e_wortart != '':
        print(f"{F.LIGHTYELLOW_EX}{inp}{S.RESET_ALL} ist {F.LIGHTMAGENTA_EX}{form}{S.RESET_ALL} von:\n")

    return fin.fullformat()


def translate(deu: str, fmt=False):
    try:
        possibilities = []
        for wr in worter:
            if deu in worter[wr].deu:
                possibilities.append(wr)

        if fmt:
            print(f"\n\nKaseiisch:\n{worter[possibilities[0]].kaz}\n\n")
            print("Änhlich:")
            for pos in possibilities:
                print(f"{worter[pos].kaz} - {lst_to_str(worter[pos].deu)}")
        else:
            return possibilities[0]
    except Exception as e:
        os.system("cls")
        print("== Übersetzer ==")
        print(e)
    input("\n\nBeliebige Taste drücken ")




# Init

# wörter = load()

if __name__ == '__main__':
    x = 0

    while True:
        if x == 0:
            os.system("cls")
            print(f"{F.LIGHTYELLOW_EX}What do you want to do?{S.RESET_ALL}\n1) Import Caseyan Google Spreadsheet into Dictionary\n2) Manually add word to Dictionary\n3) List raw Dictionary\n4) List the entire Dictionary (full screen recommended)")
            x = input("> ")

        if int(x) == 1:
            spread()
        elif int(x) == 2:
            add()
        elif int(x) == 3:
            print(worter)
            input()
            x = 0
        elif int(x) == 4:
            for i in worter:
                print(worter[i].rowformat())
            input()
            x = 0
        
