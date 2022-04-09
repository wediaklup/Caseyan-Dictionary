import dicteng
import os

while True:
    os.system("cls")
    print("== Übersetzer ==")
    inp = input("Deutsch:\n> ")
    dicteng.translate(inp, True)
