import random
mitu_tahab= input("Sisesta mitu tahab: ")
mitu_tahab= int(mitu_tahab)
ounte_jaak= 14

for i in range(0, mitu_tahab):
    yhele= random.randint(1, 2)
    ounte_jaak= ounte_jaak - yhele
    print(yhele)
    print("jargi jai" + str(ounte_jaak))