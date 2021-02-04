transporditavate_inimeste_arv= input("inimeste arv")
uhe_bussi_kohtade_arv= input("kohtade arv")
tais_busse= int(transporditavate_inimeste_arv) // int(uhe_bussi_kohtade_arv)
poolikud_bussid= int(transporditavate_inimeste_arv) % int(uhe_bussi_kohtade_arv)
if poolikud_bussid > 0:
   tais_busse=  tais_busse + 1
else:
   poolikud_bussid= int(transporditavate_inimeste_arv) // tais_busse
print("busse vaja "+ str(tais_busse))
print("viimases bussis inimesi " + str(poolikud_bussid))

