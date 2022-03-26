import dicteng
import os

while True:
    os.system("cls")
    print("== Kaseiisch Wörterbuch ==\nZu suchendes Wort eingeben!")
    term = input("> ")
    os.system("cls")
    print(dicteng.search(term))
    input()
