import tkinter as tk
import tkinter.messagebox

#siia teen akna
aken =  tk.Tk()
aken.title("Akvaariumi kalkulaator")
aken.geometry("800x300")
aken.resizable(0,0)

nr=0
pikkus=0
laius=5
korgus=10

def kuvaInfo():
    global nr
    pikkus=int(pikkuseVali.get())
    laius=int(laiuseVali.get())
    korgus=int(korguseVali.get())
    nr=pikkus*laius*korgus #siin teen tehte
    if var.get()==2:
        nr=nr/1000
    if nr>0: #siin teen kontrolli   
        tekstikast.config(text=nr)
    else:
        tk.messagebox.showerror("Viga!", "Sul on üks mõõtudest sisestatud valesti!") #siit tuleb veateade
       
    print(nr) 
    

#need on kolm sisestusvälja   
pikkusLabel = tk.Label(aken, text="pikkus", width=20)
pikkusLabel.grid(row=0, column=0)
    
pikkuseVali = tk.Entry(aken, width=20)
pikkuseVali.grid(row=0, column=1)




laiusLabel = tk.Label(aken, text="laius", width=20)
laiusLabel.grid(row=1, column=0)
    
laiuseVali = tk.Entry(aken, width=20)
laiuseVali.grid(row=1, column=1)



korgusLabel = tk.Label(aken, text="korgus", width=20)
korgusLabel.grid(row=2, column=0)
    
korguseVali = tk.Entry(aken, width=20)
korguseVali.grid(row=2, column=1)

#funktsioonid
def naita_valikut():

    if var.get()==1:
        moodud.config(text="mõõdud on kuupsentimeetrites")
        
        print("mõõdud on kuupsentimeetrites")
    else:
        moodud.config(text="mõõdud on liitrites")

        print("mõõdud on liitrites")

#valikukast
var = tk.IntVar()
valikukast = tk.Radiobutton(aken,text="kuupsentimeetrit", variable=var, value=1, command=naita_valikut)
valikukast.grid(row=3, column=0)
valikukast = tk.Radiobutton(aken,text="liitrit", variable=var, value=2, command=naita_valikut)
valikukast.grid(row=3, column=1)
#valiku väli
moodud = tk.Label(aken, text="valik", width=60)
moodud.grid(row=5, column=0)
#arvuta nupp
B = tk.Button(aken, text ="Arvuta", command = kuvaInfo)

B.grid(row=6, column=0)
#tulemus väli
tekstikast = tk.Label(aken, text="vastus", width=60)
tekstikast.grid(row=7, column=0)






aken.mainloop()