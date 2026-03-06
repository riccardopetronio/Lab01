import random


class Domanda:
    def __init__(self, domanda: str, difficolta: int, risp_gius: str, opzione2: str, opzione3: str, opzione4: str):
        self.domanda = domanda
        self.difficolta = difficolta
        self.risp_gius = risp_gius
        self.opzione2 = opzione2
        self.opzione3 = opzione3
        self.opzione4 = opzione4

    def risposte_disponibili(self):
        lista_risposte = [self.risp_gius, self.opzione2, self.opzione3, self.opzione4]
        random.shuffle(lista_risposte)
        return lista_risposte

lista_domande: list[Domanda] = []

with open('domande.txt', 'r', encoding='utf-8') as file:
    righe = file.readlines()

    contatore1 = 0
    contatore2 = 1
    contatore3 = 2
    contatore4 = 3
    contatore5 = 4
    contatore6 = 5

    while contatore5 <= len(righe):
        vTemp = Domanda(righe[contatore1].strip(), int(righe[contatore2].strip()), righe[contatore3].strip(),
                        righe[contatore4].strip(), righe[contatore5].strip(), righe[contatore6].strip())
        lista_domande.append(vTemp)
        contatore1 += 7
        contatore2 += 7
        contatore3 += 7
        contatore4 += 7
        contatore5 += 7
        contatore6 += 7


def domande_per_il_livello_attuale(diff: int):
    risultato: list[Domanda] = []
    for d in lista_domande:
        if d.difficolta == diff:
            risultato.append(d)
    random.shuffle(risultato)
    return risultato


difficolta_attuale = 0
sbagliato = False
risposte_corrette = 0

while sbagliato == False and len(domande_per_il_livello_attuale(difficolta_attuale)) != 0:

    vTemp = domande_per_il_livello_attuale(difficolta_attuale)[0]
    risposte = vTemp.risposte_disponibili()

    print(f"{vTemp.domanda}\n1) {risposte[0]}\n2) {risposte[1]}\n3) {risposte[2]}\n4) {risposte[3]}\n")
    scelta_utente = risposte[int(input("quale numero scegli?  "))-1]
    print("")

    if scelta_utente == vTemp.risp_gius:
        difficolta_attuale += 1
        risposte_corrette += 1
    else:
        sbagliato = True

print(f"il tuo punteggio è: {risposte_corrette}")
nikname = input("nikneme: ")

punteggi = []
punteggi.append([nikname, str(risposte_corrette)])
with open('punti.txt', 'r', encoding='utf-8') as file:
    for riga in file:
        vTemp = riga.strip().split(" ")
        punteggi.append(vTemp)
punteggi.sort(key=lambda x: x[1], reverse=True)

with open('punti.txt', 'w', encoding='utf-8') as file:
    for r in punteggi:
        file.write(f"{r[0]} {r[1]}\n")
