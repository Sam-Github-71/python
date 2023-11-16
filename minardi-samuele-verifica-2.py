tupla2 = (
            (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
            (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
            (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
            (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
            (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
            (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
            (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
            (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
        )

tupla=tupla2

def media_globale(tupla):
    mediag=0
    tupla=[]
    for *Reparto, *Prodotto in tupla2:
        for tipoprodotto, *Pagamento in Prodotto:
            for tipopagamento, prezzo in Pagamento:
                mediag+=prezzo
                tupla=(mediag)
    return tupla


def media(tupla, categoria, metodopagamento):
    media=0
    tupla=[]
    for *Reparto, *Prodotto in tupla2:
        for tipoprodotto, *Pagamento in Prodotto:
            for tipopagamento, prezzo in Pagamento:
                for reparto, tiporeparto in Reparto:
                    if (tipopagamento==metodopagamento) and (tiporeparto==categoria):
                        media+=prezzo
                        tupla=(media)

    return tupla

def venditaMax(tupla):
    Max=0
    pMax=[]
    tupla=[]
    for *Reparto, *Prodotto in tupla2:
        for tipoprodotto, *Pagamento in Prodotto:
             for tipopagamento, prezzo in Pagamento:
                 if prezzo>=Max:
                     Max=prezzo
                     pMax=tipoprodotto
                     tupla=(pMax, Max)
    return tupla
                 

def venditaMin(tupla):
    Min=9999
    tupla=[]
    for *Reparto, *Prodotto in tupla2:
        for tipoprodotto, *Pagamento in Prodotto:
             for tipopagamento, prezzo in Pagamento:
                 for reparto, tiporeparto in Reparto:
                    if prezzo<=Min and reparto=="RepartoA":
                         Min=prezzo
                         tupla=(Min)
    return tupla
                     
                 
#svolgimento della funzionalità venditaPer non richiesto
#def venditaPer(tupla)


scelta=int(input("1=media_globale, 2=media, 3=venditaMax, 4=venditaMin"))
if (scelta==1):
    tupla=media_globale(tupla)
elif (scelta==2):
    categoria=input("inserisci la categoria/tipo di reparto")
    metodopagamento=input("inserisci il metodo di pagamento")
    tupla=media(tupla, categoria, metodopagamento)
