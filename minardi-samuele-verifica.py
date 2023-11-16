tupla1=(
   ("Milano", [("Gennaio", 1000), ("Febbraio", 500), ("Marzo", 1500), ("Aprile", 2500), ("Maggio", 500), ("Giugno", 600)])
   ("Roma", [("Gennaio", 1000), ("Febbraio", "N/D"), ("Marzo", 1000), ("Aprile", 2500), ("Maggio", "N/D"), ("Giugno", 2500)])
   )

def precipitazioni(cittain):
    media=0
    tupla = []
    pMax=0
    pMin=99
    mMax=[]
    mMin=[]
    count=0
    for Città,*Rilevazione in tupla1:
        if (Città==cittain):
            print (Città)

        for mese, precipitazione in Rilevazione:
            if precipitazione != "N/D":
                media+=precipitazione
                count+=1
            if precipitazione >= pMax and precipitazione != "N/D":
             pMax=precipitazione 
             mMax=mese
            if precipitazione <= pMin and precipitazione != "N/D":
             pMin=precipitazione
             mMin=mese
        tupla = (media/count, (pMax, mMax), (pMin, mMin))

        return tupla
    

cittain=input("inserisci una Città")
tupla=precipitazioni(cittain)
if tupla != []:
    print(f"Nella citta di ", {cittain}, "c'è stata una precipitazione pari a ", tupla[0], "\n la precipitazione massima rilevata è: ", tupla[1][0], "rilevata il mese di ", tupla[1][1], "\n la precipitazione minima rilevata è: ", tupla[2][0], "rilevata il mese di ", tupla[2][1])
else:
   print(f"tupla vuota")


