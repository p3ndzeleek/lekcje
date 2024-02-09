import os

dlugosc = int(input("Podaj długość piekielnika: "))
powiekszenie = input("Czy chcesz powiększyć swojego piekielnik? (tak/nie): ")
wartosc = 0
if powiekszenie.lower() == "tak":
    wartosc = int(input("O ile chcesz zwiększyć piekielnik? "))
    dlugosc += wartosc
file_path = "pliki/piekielnik.txt"
with open(file_path, "w") as file:
    file.write(f"Długość: {dlugosc}, Powiększenie: {wartosc}")

with open(file_path, "r") as file:
    print(file.read())

os.system("pause")


