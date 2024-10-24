
class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self):
    #2 Ritorna una stringa contenente gli attributi dell'articolo
    return str(self.codice) + '' + self.fornitore + '' + self.marca + '' + str(self.prezzo) + '' + str(self.quantita)

  def modifica_scheda(self):
    #3 Permette di modificare gli attributi dell'articolo
    scelta = int(input("cosa vuoi modificare?"))
    if scelta == 1:
      codice = input("reinserici il codice")
    elif scelta == 2:
      fornitore = input("reinserici il fornitore")
    elif scelta == 3:
      marca = input("reinserici la marca")
    elif scelta == 4:
      prezzo = input("reinserici il prezzo")
    elif scelta == 5:
      quantita = input("reinserici la quantità")



class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      #4 Implementa il costruttore
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self):
      #5 Ritorna una stringa contenente gli attributi del televisore
      return str(self.codice) + '' + self.fornitore + '' + self.marca + '' + str(self.prezzo) + '' + str(self.quantita) + '' + str(self.pollici) + '' + self.tipo



class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    #6 Implementa il costruttore
    super().__init__(codice, fornitore, marca, prezzo, quantita)
    self.dimensioni = dimensioni
    self.modello = modello

  def scheda_articolo(self):
    #7 Ritorna una stringa contenente gli attributi del frigorifero
    return str(self.codice) + '' + self.fornitore + '' + self.marca + '' + str(self.prezzo) + '' + str(self.quantita) + '' + str(self.dimensioni) + '' + self.modello



t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())

t1.modifica_scheda()
print(t1.scheda_articolo())



class Ordine(Televisore, Frigorifero):
  def __init__(self,codice,data, piva,indirizzo):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo 
    self.articoli = []
 

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
      self.articoli.append(articolo)
      print("televisore aggiunto alla lista")
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
      self.articoli.append(articolo)
      print("frigorifero aggiunto alla lista")

    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno

  def rimuovi_articolo(self,articolo):
    #10 Implementa il metodo
    if isinstance(articolo, Televisore):
      tipo_articoli="televisore"
      self.articoli.remove(articolo)
      print("televisore rimosso dalla lista")
    elif isinstance(articolo, Frigorifero):
      tipo_articolo="frigorifero"
      self.articoli.remove(articolo)
      print("frigorifero rimosso dalla lista")




    def importo_ordine(self):
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)

  
        importo = self.prezzo*self.quantita
        print("importo: " + importo)
    pass

  def dettaglio_ordine(self):
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...

    return([self.sommaT,self.sommaF,self.sommaT+self.sommaF])

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)

#13 Risposta al Punto 1 : Per un ordine: il numero di articoli presenti e
# l'importo totale senza distinguere il tipo di articolo

ordine1.importo_ordine()

#14 Risposta punto 2.   Per un ordine: il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")

class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio = nome_negozio
    self.codie_negozio = codice_negozio
    self.oridini = []

  def aggiungi_ordine(self,ordine):
    if isinstance(ordine, Ordini):
      self.ordini.append(ordine)
    #17 Implementa il metodo  

  def rimuovi_ordine(self,ordine):
    if isinstance(ordine, Ordini):
      self.ordini.remove(ordine)
    #18 Implementa il metodo
    

  def totale_ordini(self):
    #19 Implementa il metodo
    #...
    return ([self.totT,self.totF,self.tot])

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

# 20 Riposta punto 3: Per tutti gli ordini del negozio mostra
# il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")