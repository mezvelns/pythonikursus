fail = open("konto.txt", encoding="UTF-8")
sissetulek = []
for rida in fail:
    if float(rida) > 0:
        sissetulek.append(float(rida))
fail.close()

for posArv in sissetulek:
    print(posArv)
