
muusikapalad = input(" jukebox.txt\n 80ndad.txt\n eesti_muusika.txt\n edm.txt\nPalun sisestage failinimi: ")

fail = open(muusikapalad, encoding="UTF-8")
laulud = []
i = 1
for rida in fail:
    laulud.append(rida)
    jrk = str(i) + "." + rida
    print(jrk, end="")
    i += 1    
fail.close()

muusikapalad2 = int(input("\n\nValige laulu järjekorranumber: "))
print(laulud[muusikapalad2-1])

