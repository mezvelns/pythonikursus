nimi= input("Sisesta nimi")
kiirus= input("Sisesta lubatud kiirus")
tegelik_kiirus= input("Sisesta tegelik kiirus")
esialgne_tulemus= (int(tegelik_kiirus) - int(kiirus)) * 3
trahv= min(190, esialgne_tulemus)

print(nimi+", kiiruse ületamise eest on teie trahv "+str(trahv)+" eurot")
