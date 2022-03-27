import dicteng
import os

while True:
    os.system("cls")
    print("== Kaseiisch Wörterbuch ==\nZu suchendes Wort eingeben!")
    term = input("> ")
    try:
        print(dicteng.search(term))
    except Exception as e:
        if dicteng.DEBUG == 'False':
            os.system("cls")
        print("Wort nicht gefunden\n{e}".format(e=e))
    input()
