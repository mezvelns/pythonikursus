fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
fail.close()

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))   
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
opilased = vastuvoetud[aastad.index(aasta)]
print(str(aasta) + ". aastal oli vastuvõetuid" ,opilased)